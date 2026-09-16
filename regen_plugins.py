# -*- coding: utf-8 -*-
"""Regenerate multi-host manifests + skills/commands for each brand plugin."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLUGINS = ROOT / "plugins"
VERSION = "1.2.0"

BRANDS = [
    {
        "dir": "real-mcp",
        "key": "real",
        "display": "REAL",
        "domain": "realvip.cc",
        "homepage": "https://realvip.cc",
        "mcp": "https://realvip.cc/api/mcp/v1/jsonrpc",
        "color": "#0B6E4F",
    },
    {
        "dir": "s1mple-mcp",
        "key": "s1mple",
        "display": "s1mple",
        "domain": "s1mple-pro.com",
        "homepage": "https://s1mple-pro.com",
        "mcp": "https://s1mple-pro.com/api/mcp/v1/jsonrpc",
        "color": "#1A56DB",
    },
    {
        "dir": "infinity-labs-mcp",
        "key": "infinity-labs",
        "display": "INFINITY LABS",
        "domain": "infinity-labs.zeabur.app",
        "homepage": "https://infinity-labs.zeabur.app",
        "mcp": "https://infinity-labs.zeabur.app/api/mcp/v1/jsonrpc",
        "color": "#7C3AED",
    },
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", path.relative_to(ROOT))


def write_json(path: Path, data: object) -> None:
    write(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def references_bodies(key: str, disp: str, domain: str) -> dict[str, str]:
    return {
        "write-lifecycle.md": f"""# Write lifecycle ({disp})

## Before any write / proposal tool

1. Restate the intended business outcome in one short sentence (who / what / when).
2. Wait for an explicit user confirmation (yes / 確認 / 可以).
3. Only then call the tool.

Applies to: `memory_upsert`, `contact_add_tag`, `contact_append_note`,
`reservation_update_status`, `reservation_reschedule`, `dispatch_create`,
`escalate_to_human`.

## After the tool returns

- Many writes are **proposals** that still need human approval in the {disp} dashboard.
- Say clearly: may need dashboard approval — do **not** claim the change is live
  unless the tool result says so.
- If the user cancels, do not call the tool.

## Invalidation

If the user changes the intended outcome after confirming, confirm again before calling.
""",
        "brand-isolation.md": f"""# Brand isolation ({disp})

- MCP server id: `{key}`
- Domain: `{domain}` only
- Never call other merchant MCP servers or domains from this plugin's skills.
- Never reuse tokens, grants, or project ids across brands.
- If the user asks about another brand, tell them to install/authenticate that brand's plugin.
""",
        "product-terms.md": f"""# Product terms (zh-TW) — {disp}

Prefer these customer-facing words:

| Prefer | Avoid leading with |
|---|---|
| 專案 | workspace_id（除非使用者要 ID） |
| 聯絡人／客人 | contact row / schema |
| 預約 | reservation entity |
| 派工／派工單 | dispatch job payload |
| 知識庫／FAQ／價目／店規 | knowledge_search raw hits only |
| 記憶（內部） | memory_upsert internals |
| 轉真人 | escalate payload |
| 需後台核准 | “已寫入完成” without evidence |

If the user asks for IDs or API fields, you may disclose non-sensitive mappings.
""",
        "error-recovery.md": f"""# Error recovery ({disp} / `{key}`)

## Auth (`401` / `403` / authentication-required)

Do **not** ask for tokens or paste keys. Guide re-Authenticate:

| Agent | Action |
|---|---|
| Cursor | Plugin → MCPs → `{key}` → Logout（若有）→ Authenticate |
| Claude Code | Uninstall plugin → reinstall |
| Codex | Uninstall → reinstall from marketplace |
| Other | MCP settings for `{key}` → Authenticate |

Then retry with `{key}-session` (`workspace_summary`).

## Network / `5xx` / timeout

Treat as connectivity — do **not** start OAuth recovery first. Retry once; if still failing, say the server may be down.

## Tool missing from `tools/list`

The project allowlist disabled that tool. Tell the user it is turned off for this project in the {disp} MCP settings. Do **not** invent a substitute tool name.

## Rate limit / `429`

Do not hammer retries. Tell the user to wait briefly and try again.
Customer-facing line: `這次操作無法完成，請稍後再試。`
""",
    }


def gen_brand(b: dict) -> None:
    base = PLUGINS / b["dir"]
    name = b["dir"]
    key = b["key"]
    disp = b["display"]
    mcp = b["mcp"]
    home = b["homepage"]
    domain = b["domain"]

    write_json(
        base / ".cursor-plugin" / "plugin.json",
        {
            "name": name,
            "displayName": f"{disp} MCP",
            "version": VERSION,
            "description": (
                f"Workflow skills and hosted MCP for {disp}. "
                "Install, Authenticate via OAuth, then validate with the session skill. "
                "No tokens to paste."
            ),
            "author": {"name": "Community MCP", "email": "plugins@example.com"},
            "homepage": home,
            "license": "MIT",
            "keywords": ["mcp", "oauth", key, "crm", "skills", "authenticate"],
            "category": "Productivity",
            "logo": "assets/logo.svg",
            "skills": "./skills/",
            "commands": "./commands/",
            "mcpServers": "./mcp.json",
        },
    )

    write_json(
        base / ".claude-plugin" / "plugin.json",
        {
            "name": name,
            "displayName": f"{disp} MCP",
            "version": VERSION,
            "description": (
                f"Workflow skills and hosted MCP for {disp}. "
                "Install, then connect the bundled MCP through OAuth."
            ),
            "author": {"name": "Community MCP", "url": home},
            "homepage": home,
            "license": "MIT",
            "keywords": ["mcp", "oauth", key, "crm", "skills"],
            "skills": "./skills/",
            "commands": "./commands/",
            "defaultEnabled": False,
        },
    )

    write_json(
        base / ".codex-plugin" / "plugin.json",
        {
            "name": name,
            "version": VERSION,
            "description": f"Workflow skills and hosted MCP for {disp}.",
            "author": {"name": "Community MCP", "url": home},
            "homepage": home,
            "license": "MIT",
            "keywords": ["mcp", "oauth", key, "crm", "skills"],
            "skills": "./skills/",
            "mcpServers": "./codex.mcp.json",
            "interface": {
                "displayName": f"{disp} MCP",
                "shortDescription": f"Skills and hosted MCP for {disp}.",
                "longDescription": (
                    f"Session validation, contacts, reservations, dispatch, knowledge, "
                    f"and approved write proposals via OAuth. Data stays on {domain}."
                ),
                "developerName": "Community MCP",
                "category": "Productivity",
                "capabilities": ["Read", "Write"],
                "websiteURL": home,
                "brandColor": b["color"],
                "logo": "./assets/logo.svg",
                "defaultPrompt": [
                    f"使用 {key}-session 驗證我的 MCP 設定。確認可用後，簡短說明一下你能幫我做什麼。",
                    f"使用 {key}-contacts 列出最近聯絡人。",
                    f"使用 {key}-reservations 列出近期預約。",
                    f"使用 {key}-knowledge 搜尋知識庫 FAQ。",
                ],
            },
        },
    )

    write_json(base / "mcp.json", {"mcpServers": {key: {"url": mcp}}})
    write_json(
        base / ".mcp.json",
        {"mcpServers": {key: {"type": "http", "url": mcp}}},
    )
    write_json(
        base / "codex.mcp.json",
        {"mcpServers": {key: {"type": "http", "url": mcp}}},
    )

    agents = base / ".agents" / "plugins"
    write_json(
        agents / "marketplace.json",
        {
            "name": name,
            "version": VERSION,
            "interface": {
                "displayName": f"{disp} MCP",
                "logo": "../../assets/logo.svg",
                "defaultPrompt": [
                    f"使用 {key}-session 驗證我的 MCP 設定。確認可用後，簡短說明一下你能幫我做什麼。",
                    f"使用 {key}-contacts 列出最近聯絡人。",
                    f"使用 {key}-ops 給我一份專案摘要。",
                ],
            },
            "plugins": [
                {
                    "name": name,
                    "version": VERSION,
                    "source": {"source": "local", "path": f"./{name}"},
                    "policy": {
                        "installation": "AVAILABLE",
                        "authentication": "ON_INSTALL",
                    },
                    "category": "Productivity",
                }
            ],
        },
    )
    write_json(agents / name / "plugin.json", {"name": name})
    write_json(
        agents / name / "mcp_config.json",
        {"mcpServers": {key: {"url": mcp}}},
    )

    skill_mirror = agents / name / "skills"
    command_mirror = agents / name / "commands"
    ref_mirror = agents / name / "references"

    def skill(rel: str, body: str) -> None:
        write(base / "skills" / rel, body)
        write(skill_mirror / rel, body)

    def command(rel: str, body: str) -> None:
        write(base / "commands" / rel, body)
        write(command_mirror / rel, body)

    def reference(rel: str, body: str) -> None:
        write(base / "references" / rel, body)
        write(ref_mirror / rel, body)

    for rel, body in references_bodies(key, disp, domain).items():
        reference(rel, body)

    skill(
        f"{key}-mcp-connect/SKILL.md",
        f"""---
name: {key}-mcp-connect
description: Connect an agent to {disp} ({domain}) via MCP OAuth Authenticate. Use when the user wants to install, reconnect, or understand the thin MCP shell.
---

# {disp} MCP connect

## What this is

A thin connector. The MCP server lives at `{mcp}`.
Product code and customer data stay on {disp} servers — this plugin only points the agent at that URL.

## How to connect

1. Ensure this plugin is installed (MCP server `{key}` should appear).
2. Open MCP settings and click **Authenticate** / connect for `{key}`.
3. Sign in on {domain} in the browser, pick a project (workspace), allow access.
4. Prefer the `{key}-session` skill next to verify the session.

## Do not

- Do not invent tokens or paste long-lived keys unless the user explicitly uses the dashboard advanced key flow.
- Do not call other brands' domains from this skill.
- Do not ask the user to paste OAuth codes into chat.

Also read `references/brand-isolation.md`.
""",
    )

    skill(
        f"{key}-session/SKILL.md",
        f"""---
name: {key}-session
description: Validate {disp} MCP session by listing tools and calling workspace_summary. Use when verifying authentication, after OAuth, or when other {disp} skills fail with 401/403/429.
---

# Skill: {key}-session

**Prerequisite:** Read `skills/{key}-universal-workflow/SKILL.md` before operational work.
**Errors:** Read `references/error-recovery.md`.

This skill uses the `{key}` MCP server. Authentication is managed by the agent through MCP OAuth.

## MCP tools (session check)

- Prefer `tools/list` (or the host equivalent) to confirm tools are visible.
- Call `workspace_summary` — project name plus contact / reservation / dispatch counts (read-only). No arguments.

## Workflow

1. Confirm the `{key}` MCP server is connected.
2. Call `workspace_summary`.
3. If it succeeds, briefly tell the user which project is bound and what you can help with
   (contacts, reservations, dispatch, knowledge, memory, proposed writes needing approval).
4. On auth failure, follow `references/error-recovery.md`, then retry `workspace_summary`.

## Guardrails

- Stay read-only in this skill.
- Do not collect passwords or TOTP in chat.
- Do not paste, export, or request MCP access tokens.
- Scope is the project chosen during OAuth consent only.
""",
    )

    skill(
        f"{key}-universal-workflow/SKILL.md",
        f"""---
name: {key}-universal-workflow
description: Shared {disp} policy for customer language, write confirmation, brand isolation, and errors. Non-operational prerequisite for every {disp} workflow skill.
---

# Skill: {key}-universal-workflow

This is a **policy** skill, not an operational workflow. Read it before other `{key}-*` skills use tools.

## Mandatory references (read as needed)

- `references/product-terms.md` — customer-facing wording
- `references/write-lifecycle.md` — confirm before writes; proposal ≠ live
- `references/brand-isolation.md` — `{key}` / `{domain}` only
- `references/error-recovery.md` — auth / 429 / missing tools

## Mandatory core

1. **Customer language first** — use product terms from the reference.
2. **Confirm before writes** — follow write-lifecycle for every proposal tool.
3. **Allowlist** — if a tool is missing from `tools/list`, it is disabled; do not invent names.
4. **Brand isolation** — only MCP `{key}` on `{domain}`.

## Synonym routing

| User says | Route to |
|---|---|
| 連線／驗證／登入 MCP／設定好了嗎 | `{key}-session` |
| 聯絡人／客戶／查誰 | `{key}-contacts` |
| 預約 | `{key}-reservations` |
| 派工 | `{key}-dispatch` |
| 知識庫／FAQ／價目／店規 | `{key}-knowledge` |
| 記憶／偏好 | `{key}-memory` |
| 專案摘要／總覽 | `{key}-ops` |
| 轉真人 | `{key}-dispatch`（escalate）或 `{key}-ops` |
| 怎麼裝／Authenticate | `{key}-mcp-connect` |

## What this skill does not do

- It does not replace domain skills.
- It does not invent MCP tools beyond the server allowlist.
""",
    )

    skill(
        f"{key}-contacts/SKILL.md",
        f"""---
name: {key}-contacts
description: List and look up {disp} contacts via MCP (contacts_list, contact_get). Use when the user asks about customers or contacts.
---

# Skill: {key}-contacts

**Prerequisite:** `{key}-universal-workflow`. Auth issues → `{key}-session` + `references/error-recovery.md`.

## MCP tools

- `contacts_list` — recent contacts (read-only, max 50). Params: `limit` (1–50, default 20), optional `q`.
- `contact_get` — one contact by `contact_id` (required, integer).

## Workflow

1. Browse/search with `contacts_list`; pass `q` for name fragments.
2. Detail with `contact_get` using an id from the list or the user.
3. Use plain product language (`references/product-terms.md`).

## Writes

Tagging / notes are **not** in this skill — use `{key}-ops` and `references/write-lifecycle.md`.
""",
    )

    skill(
        f"{key}-reservations/SKILL.md",
        f"""---
name: {key}-reservations
description: List and propose updates to {disp} reservations (reservations_list, reservation_update_status, reservation_reschedule).
---

# Skill: {key}-reservations

**Prerequisite:** `{key}-universal-workflow` + `references/write-lifecycle.md` for any write.

## Read

- `reservations_list` — `status` optional, `limit` 1–50 (default 20)

## Write / proposal (confirm first)

- `reservation_update_status` — `reservation_id`, `status` (`pending|confirmed|cancelled|completed|no_show`)
- `reservation_reschedule` — `reservation_id`, `starts_at` (ISO), optional `ends_at`

## Workflow

1. List/filter to answer questions.
2. For status/time changes: confirm outcome → call proposal tool → remind dashboard approval may be required.
""",
    )

    skill(
        f"{key}-dispatch/SKILL.md",
        f"""---
name: {key}-dispatch
description: List {disp} dispatch jobs, propose new jobs, or escalate to a human (dispatch_list, dispatch_create, escalate_to_human).
---

# Skill: {key}-dispatch

**Prerequisite:** `{key}-universal-workflow` + `references/write-lifecycle.md` for any write.

## Read

- `dispatch_list` — `status` optional, `limit` 1–50

## Write / proposal (confirm first)

- `dispatch_create` — optional `title`, `region`, `notes`, `customer_name`, `customer_phone`
- `escalate_to_human` — optional `reason` (pauses bot after approval)

## Workflow

1. Prefer `dispatch_list` for status questions.
2. Confirm before create/escalate; remind approval may be required.
""",
    )

    skill(
        f"{key}-knowledge/SKILL.md",
        f"""---
name: {key}-knowledge
description: Search {disp} shop knowledge base FAQ / price / policy via knowledge_search.
---

# Skill: {key}-knowledge

**Prerequisite:** `{key}-universal-workflow`.

## MCP tools

- `knowledge_search` — `q` keyword, `limit` 1–10 (default 5). Read-only.

## Workflow

1. Call with the user's question as `q`.
2. Summarize answers in plain language; cite snippets when helpful.
3. If nothing useful returns, say the knowledge base may not cover it — do not invent shop facts.
""",
    )

    skill(
        f"{key}-memory/SKILL.md",
        f"""---
name: {key}-memory
description: List or upsert internal guest memory on {disp} (memory_list, memory_upsert). Memory is internal — not sent to the guest directly.
---

# Skill: {key}-memory

**Prerequisite:** `{key}-universal-workflow` + `references/write-lifecycle.md` before upsert.

## MCP tools

- `memory_list` — optional `q`, `limit` 1–20 (default 8). Read-only.
- `memory_upsert` — required `body`; optional `kind` (`preference|fact|history|note`), optional `key` (same key overwrites).

## Workflow

1. List/search first when the user asks what is remembered.
2. Confirm before upsert; clarify this is **internal** staff memory.
""",
    )

    skill(
        f"{key}-ops/SKILL.md",
        f"""---
name: {key}-ops
description: {disp} project overview via workspace_summary, and router to domain skills for contacts/reservations/dispatch/knowledge/memory.
---

# Skill: {key}-ops

**Prerequisite:** `{key}-universal-workflow`.

## Primary tool

- `workspace_summary` — contacts / reservations / dispatch counts (read-only)

## When to route elsewhere

| Need | Skill |
|---|---|
| 聯絡人 | `{key}-contacts` |
| 預約 | `{key}-reservations` |
| 派工／轉真人 | `{key}-dispatch` |
| FAQ／價目 | `{key}-knowledge` |
| 內部記憶 | `{key}-memory` |

Cross-cutting write proposals may still be done here **only if** the user already confirmed
and `references/write-lifecycle.md` is followed — otherwise prefer the domain skill.
""",
    )

    command(
        f"validate-{key}-setup.md",
        f"""---
name: validate-{key}-setup
description: 使用 {key}-session 驗證 MCP 設定，並簡短說明可用能力
---

使用 {key}-session 驗證我的 MCP 設定。確認可用後，簡短說明一下你能幫我做什麼。
""",
    )
    command(
        "list-contacts.md",
        f"""---
name: list-contacts
description: 使用 {key}-contacts 列出最近聯絡人
---

使用 {key}-contacts 列出最近聯絡人（約 20 筆）。若有關鍵字我再補。
""",
    )
    command(
        "project-summary.md",
        f"""---
name: project-summary
description: 使用 {key}-ops 取得專案摘要
---

使用 {key}-ops 呼叫 workspace_summary，給我一份專案摘要（聯絡人／預約／派工數量）。
""",
    )
    command(
        "list-reservations.md",
        f"""---
name: list-reservations
description: 使用 {key}-reservations 列出近期預約
---

使用 {key}-reservations 列出近期預約（約 20 筆）。
""",
    )
    command(
        "list-dispatch.md",
        f"""---
name: list-dispatch
description: 使用 {key}-dispatch 列出派工單
---

使用 {key}-dispatch 列出近期派工單。
""",
    )
    command(
        "search-knowledge.md",
        f"""---
name: search-knowledge
description: 使用 {key}-knowledge 搜尋知識庫
---

使用 {key}-knowledge 搜尋知識庫。若我沒給關鍵字，先問我要查什麼（FAQ／價目／店規）。
""",
    )
    command(
        "escalate-human.md",
        f"""---
name: escalate-human
description: 使用 {key}-dispatch 提議轉真人（需確認）
---

使用 {key}-dispatch：先向我確認轉真人的原因，確認後再呼叫 escalate_to_human，並提醒可能需後台核准。
""",
    )

    write(
        base / "README.md",
        f"""# {disp} MCP plugin

Points agents at **{mcp}** and uses OAuth Authenticate.

Includes:

- Skills: connect, session, policy, contacts, reservations, dispatch, knowledge, memory, ops
- References: write lifecycle, brand isolation, product terms, error recovery
- Commands: validate, contacts, summary, reservations, dispatch, knowledge, escalate
- Host manifests: Cursor, Claude, Codex, Agents

No product source code. Data stays on `{domain}`.

## Quick start

1. Install this plugin
2. Authenticate the `{key}` MCP server
3. Run **validate-{key}-setup**
4. Revoke later in {disp} dashboard → MCP / connected apps
""",
    )


def gen_root() -> None:
    write_json(
        ROOT / ".cursor-plugin" / "marketplace.json",
        {
            "name": "community-mcp-marketplace",
            "owner": {"name": "Community MCP", "email": "plugins@example.com"},
            "metadata": {
                "description": (
                    "Thin public shells that connect agents to REAL / s1mple / INFINITY LABS "
                    "MCP via OAuth Authenticate. Domain skills + references included. "
                    "No product source code."
                ),
                "version": VERSION,
                "pluginRoot": "plugins",
            },
            "plugins": [
                {
                    "name": "real-mcp",
                    "source": "real-mcp",
                    "description": "REAL MCP Authenticate + workflow skills",
                    "category": "mcp",
                    "tags": ["mcp", "oauth", "crm", "skills"],
                },
                {
                    "name": "s1mple-mcp",
                    "source": "s1mple-mcp",
                    "description": "s1mple MCP Authenticate + workflow skills",
                    "category": "mcp",
                    "tags": ["mcp", "oauth", "crm", "skills"],
                },
                {
                    "name": "infinity-labs-mcp",
                    "source": "infinity-labs-mcp",
                    "description": "INFINITY LABS MCP Authenticate + workflow skills",
                    "category": "mcp",
                    "tags": ["mcp", "oauth", "crm", "skills"],
                },
            ],
        },
    )

    write_json(
        ROOT / ".claude-plugin" / "marketplace.json",
        {
            "name": "community-mcp-marketplace",
            "owner": {"name": "Community MCP", "email": "plugins@example.com"},
            "description": (
                "Community MCP marketplace shells for REAL / s1mple / INFINITY LABS — "
                "OAuth Authenticate plus domain workflow skills."
            ),
            "version": VERSION,
            "plugins": [
                {
                    "name": b["dir"],
                    "source": f"./plugins/{b['dir']}",
                    "displayName": f"{b['display']} MCP",
                    "description": (
                        f"{b['display']} MCP skills. After install, run validate-{b['key']}-setup."
                    ),
                    "version": VERSION,
                    "author": {"name": "Community MCP", "url": b["homepage"]},
                    "homepage": b["homepage"],
                    "license": "MIT",
                    "category": "Productivity",
                    "commands": f"./plugins/{b['dir']}/commands/",
                    "keywords": ["mcp", "oauth", b["key"], "crm", "skills"],
                }
                for b in BRANDS
            ],
        },
    )

    write(
        ROOT / "SECURITY.md",
        """# Security

## Reporting

Report security issues through the support channel of the brand whose MCP URL you use
(REAL / s1mple / INFINITY LABS). Do not open public issues that include tokens or customer data.

## Revoking access

Removing a marketplace plugin from an agent does **not** by itself revoke server-side OAuth grants.

To revoke:

1. Sign in to that brand's dashboard.
2. Open **MCP** (or connected apps / agent authorizations).
3. Revoke the grant for the agent / client you no longer trust.

You can also re-Authenticate after Logout on the agent side if the token is stale.
""",
    )

    write(
        ROOT / "CHANGELOG.md",
        f"""# Changelog

## {VERSION}

- Split domain skills: reservations, dispatch, knowledge, memory (ops becomes overview + router).
- Add `references/`: write-lifecycle, brand-isolation, product-terms, error-recovery.
- Add commands: list-reservations, list-dispatch, search-knowledge, escalate-human.
- Harden session skill guidance for 401/403/429 and missing allowlisted tools.

## 1.1.0

- Add session / universal-workflow / contacts / ops skills per brand.
- Add commands: validate-*-setup, list-contacts, project-summary.
- Add Claude / Codex / Agents host manifests.
- Document install → Authenticate → validate → revoke.

## 1.0.0

- Initial thin Cursor marketplace shells (MCP URL + connect skill).
""",
    )

    write(
        ROOT / "README.md",
        f"""# Community MCP Marketplace（公開外殼）

給 **Cursor／Claude／Codex／Agents** 用的**公開薄包**：固定 MCP URL、OAuth Authenticate、domain skills／commands／references。

**不含**後台原始碼、資料庫、金鑰、商家資料。真正能力在各站伺服器（REAL／s1mple／INFINITY LABS）。

版本 **{VERSION}**。

## 與產品的關係

| 本 repo（可公開） | 產品站（保持私有） |
|---|---|
| `mcp.json` → `…/api/mcp/v1/jsonrpc` | FastAPI、DB、儀表板 |
| Skills／references 教 Agent 怎麼用工具 | OAuth／工具實作 |
| Commands 當快捷驗證／查詢 | 核准佇列、計費、稽核 |

## 本機結構

```text
community-mcp-marketplace/
├── .cursor-plugin/marketplace.json
├── .claude-plugin/marketplace.json
├── plugins/
│   ├── real-mcp/
│   │   ├── skills/       connect · session · policy · contacts ·
│   │   │                 reservations · dispatch · knowledge · memory · ops
│   │   ├── references/   write-lifecycle · brand-isolation ·
│   │   │                 product-terms · error-recovery
│   │   ├── commands/     validate · contacts · summary · reservations ·
│   │   │                 dispatch · knowledge · escalate
│   │   └── host manifests (Cursor / Claude / Codex / Agents)
│   ├── s1mple-mcp/
│   └── infinity-labs-mcp/
├── LICENSE · SECURITY.md · CHANGELOG.md · PUBLISH.md · README.md
└── regen_plugins.py
```

## 使用者流程（安裝 → 授權 → 驗證 → 撤銷）

1. **安裝**對應站 plugin  
2. **Authenticate**（瀏覽器登入 → 選專案 → 允許）  
3. **驗證** `validate-<brand>-setup`  
4. **日常** 聯絡人／預約／派工／知識庫 commands 或口語  
5. **撤銷** 後台 MCP／已授權應用（卸載 plugin ≠ 撤銷 grant）— 見 [SECURITY.md](./SECURITY.md)

## Skills ↔ 真實 MCP 工具

| Skill | Tools |
|---|---|
| session / ops | `workspace_summary` |
| contacts | `contacts_list`, `contact_get` |
| reservations | `reservations_list`, `reservation_*` |
| dispatch | `dispatch_list`, `dispatch_create`, `escalate_to_human` |
| knowledge | `knowledge_search` |
| memory | `memory_list`, `memory_upsert` |

寫入前必須確認意圖（`references/write-lifecycle.md`）。

## 維護

三站外殼同步：`python regen_plugins.py`  
發布步驟：[PUBLISH.md](./PUBLISH.md)
""",
    )

    publish_path = ROOT / "PUBLISH.md"
    publish = publish_path.read_text(encoding="utf-8")
    if "regen_plugins.py" not in publish:
        publish = publish.replace(
            "## E. 本包開了什麼、沒開什麼",
            """維護三站 skills／commands 時可跑 `python regen_plugins.py`（會覆寫各 plugin 外殼；勿把產品後端拷進來）。

## E. 本包開了什麼、沒開什麼""",
        )
        write(publish_path, publish)


def main() -> None:
    for b in BRANDS:
        gen_brand(b)
    gen_root()
    print("OK", VERSION)


if __name__ == "__main__":
    main()
