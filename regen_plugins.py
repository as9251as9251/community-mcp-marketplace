# -*- coding: utf-8 -*-
"""One-shot generator: multi-host manifests + skills/commands for each brand plugin."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLUGINS = ROOT / "plugins"

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
            "version": "1.1.0",
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
            "version": "1.1.0",
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
            "version": "1.1.0",
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
                    f"Session validation, contacts, reservations, dispatch, and knowledge "
                    f"tools via OAuth. Product data stays on {domain}."
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
                    f"使用 {key}-ops 給我一份專案摘要（聯絡人／預約／派工數量）。",
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
            "version": "1.1.0",
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
                    "version": "1.1.0",
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

    # Skills/commands written below also mirrored into .agents/plugins/<name>/ for Antigravity-style hosts.
    skill_mirror_root = agents / name / "skills"
    command_mirror_root = agents / name / "commands"

    def skill(rel: str, body: str) -> None:
        write(base / "skills" / rel, body)
        write(skill_mirror_root / rel, body)

    def command(rel: str, body: str) -> None:
        write(base / "commands" / rel, body)
        write(command_mirror_root / rel, body)

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
""",
    )

    skill(
        f"{key}-session/SKILL.md",
        f"""---
name: {key}-session
description: Validate {disp} MCP session by listing tools and calling workspace_summary. Use when verifying authentication, after OAuth, or when other {disp} skills fail with 401/403.
---

# Skill: {key}-session

**Prerequisite:** Read `skills/{key}-universal-workflow/SKILL.md` before operational work.

This skill uses the `{key}` MCP server. Authentication is managed by the agent through MCP OAuth.

## MCP tools (session check)

- Prefer `tools/list` (or the host equivalent) to confirm tools are visible.
- Call `workspace_summary` — project name plus contact / reservation / dispatch counts (read-only). No arguments.

## Workflow

1. Confirm the `{key}` MCP server is connected.
2. Call `workspace_summary`.
3. If it succeeds, briefly tell the user which project is bound and what you can help with (contacts, reservations, dispatch, knowledge, proposed writes that need human approval).
4. If authentication is missing/expired, follow OAuth recovery below — then retry `workspace_summary`.

## OAuth recovery

If calls fail with `401` / `403` / authentication-required for `{key}`, **do not** ask for tokens, paste keys, or hand-edit MCP URLs.

| Agent | Recovery |
|---|---|
| Cursor | Plugin details → **MCPs** → `{key}` → **Logout** (if present) → **Authenticate** |
| Claude Code | Uninstall this plugin, reinstall; OAuth should start on install |
| Codex / ChatGPT desktop | Uninstall this plugin, reinstall from the marketplace |
| Other hosts | Open MCP settings for `{key}` and select **Authenticate** |

Do **not** treat network errors, timeouts, or `5xx` as OAuth failures — check connectivity first.

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
description: Shared {disp} policy for customer language, write confirmation, brand isolation, and OAuth. Non-operational prerequisite for every {disp} workflow skill.
---

# Skill: {key}-universal-workflow

This is a **policy** skill, not an operational workflow. Read it before other `{key}-*` skills use tools.

## Mandatory core

1. **Customer language first** — Explain outcomes in plain product terms (聯絡人、預約、派工、知識庫、記憶). Lead with business meaning, not internal IDs, unless the user asks for IDs.
2. **Confirm before writes** — Tools that *propose* changes (`contact_add_tag`, `contact_append_note`, `reservation_update_status`, `reservation_reschedule`, `dispatch_create`, `escalate_to_human`, `memory_upsert`) need an explicit user confirmation of the intended outcome **before** the tool call. Summarize who/what/when in one short sentence.
3. **Writes are proposals** — Many write tools create actions that still need human approval in the {disp} dashboard. After calling, say they may need dashboard approval — do not claim the change already went live unless the tool result says so.
4. **Brand isolation** — Only use MCP server `{key}` and domain `{domain}`. Never call other merchant brands interchangeably from this skill set.
5. **Allowlist** — If a tool is missing from `tools/list`, it is disabled for this project. Do not invent tool names.

## Synonym routing

| User says | Route to |
|---|---|
| 連線／驗證／登入 MCP／設定好了嗎 | `{key}-session` |
| 聯絡人／客戶／查誰 | `{key}-contacts` |
| 預約／派工／摘要／知識庫／FAQ／記憶 | `{key}-ops` |
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

**Prerequisite:** Read `skills/{key}-universal-workflow/SKILL.md`. If auth fails, use `{key}-session` recovery first.

## MCP tools

- `contacts_list` — recent contacts (read-only, max 50). Params: `limit` (1–50, default 20), optional `q` name keyword.
- `contact_get` — one contact by `contact_id` (required, integer).

## Workflow

1. For browse/search: `contacts_list` with a sensible `limit`; pass `q` when the user gives a name fragment.
2. For detail: `contact_get` with the id from a prior list (or the id the user provides).
3. Present names and useful fields in plain language; include ids only when helpful for follow-up.

## Guardrails

- Read-only in this skill. Tagging / notes belong in `{key}-ops` with confirmation.
- Do not fetch other brands' contacts.
""",
    )

    skill(
        f"{key}-ops/SKILL.md",
        f"""---
name: {key}-ops
description: {disp} project ops via MCP — summary, reservations, dispatch, knowledge search, memory, and human-approved write proposals.
---

# Skill: {key}-ops

**Prerequisite:** Read `skills/{key}-universal-workflow/SKILL.md`. If auth fails, use `{key}-session` recovery first.

## Read tools

- `workspace_summary` — counts for contacts / reservations / dispatch jobs
- `reservations_list` — recent reservations (`status` optional, `limit` 1–50)
- `dispatch_list` — dispatch jobs (`status` optional, `limit` 1–50)
- `knowledge_search` — shop FAQ / price / policy facts (`q`, `limit` 1–10)
- `memory_list` — long-term guest memory (`q` optional, `limit` 1–20)

## Write / proposal tools (confirm first)

- `memory_upsert` — upsert internal memory (`body` required; optional `kind`, `key`)
- `contact_add_tag` — propose tag
- `contact_append_note` — propose internal note
- `reservation_update_status` — propose status change
- `reservation_reschedule` — propose new `starts_at` (ISO)
- `dispatch_create` — propose a dispatch job
- `escalate_to_human` — propose handoff to a human agent

## Workflow

1. Prefer reads (`workspace_summary`, lists, `knowledge_search`) to answer questions.
2. Before any write/proposal tool: confirm the intended business outcome in one sentence; wait for explicit yes.
3. After a proposal tool: remind that dashboard approval may still be required.

## Guardrails

- Never claim a proposed write is live without confirmation from the tool/dashboard.
- Stay on `{key}` / `{domain}` only.
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

    write(
        base / "README.md",
        f"""# {disp} MCP plugin

Points agents at **{mcp}** and uses OAuth Authenticate.

Includes:

- Skills: connect, session validation, shared policy, contacts, ops
- Commands: validate setup, list contacts, project summary
- Host manifests: Cursor, Claude, Codex, Agents

No product source code is included. Data stays on `{domain}`.

## Quick start

1. Install this plugin
2. Authenticate the `{key}` MCP server
3. Run command **validate-{key}-setup** (or ask the agent to use `{key}-session`)
4. To revoke access later: open {disp} dashboard → MCP / connected apps → revoke the grant
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
                    "MCP via OAuth Authenticate. Skills + commands included. No product source code."
                ),
                "version": "1.1.0",
                "pluginRoot": "plugins",
            },
            "plugins": [
                {
                    "name": "real-mcp",
                    "source": "real-mcp",
                    "description": "Connect to REAL (realvip.cc) MCP with Authenticate + workflow skills",
                    "category": "mcp",
                    "tags": ["mcp", "oauth", "crm", "skills"],
                },
                {
                    "name": "s1mple-mcp",
                    "source": "s1mple-mcp",
                    "description": "Connect to s1mple (s1mple-pro.com) MCP with Authenticate + workflow skills",
                    "category": "mcp",
                    "tags": ["mcp", "oauth", "crm", "skills"],
                },
                {
                    "name": "infinity-labs-mcp",
                    "source": "infinity-labs-mcp",
                    "description": "Connect to INFINITY LABS MCP with Authenticate + workflow skills",
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
                "OAuth Authenticate plus workflow skills."
            ),
            "version": "1.1.0",
            "plugins": [
                {
                    "name": b["dir"],
                    "source": f"./plugins/{b['dir']}",
                    "displayName": f"{b['display']} MCP",
                    "description": (
                        f"{b['display']} MCP skills. After install, run validate-{b['key']}-setup "
                        "then query contacts or project summary as needed."
                    ),
                    "version": "1.1.0",
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
        """# Changelog

## 1.1.0

- Add session / universal-workflow / contacts / ops skills per brand (aligned to real MCP tools).
- Add commands: validate-*-setup, list-contacts, project-summary.
- Add Claude / Codex / Agents host manifests (`.claude-plugin`, `.codex-plugin`, `.agents`).
- Add `.mcp.json` / `codex.mcp.json` HTTP MCP declarations.
- Document install → Authenticate → validate → revoke in README and SECURITY.md.

## 1.0.0

- Initial thin Cursor marketplace shells (MCP URL + connect skill).
""",
    )

    write(
        ROOT / "README.md",
        """# Community MCP Marketplace（公開外殼）

給 **Cursor／Claude／Codex／Agents** 用的**公開薄包**：固定 MCP URL、OAuth Authenticate、workflow skills／commands。

**不含**後台原始碼、資料庫、金鑰、商家資料。真正能力在各站伺服器（REAL／s1mple／INFINITY LABS）。

## 與產品的關係

| 本 repo（可公開） | 產品站（保持私有） |
|---|---|
| `mcp.json` → `…/api/mcp/v1/jsonrpc` | FastAPI、DB、儀表板 |
| Skills 教 Agent 何時呼叫哪個工具 | OAuth／工具實作 |
| Commands 當快捷驗證／查詢 | 核准佇列、計費、稽核 |

## 本機結構

```text
community-mcp-marketplace/
├── .cursor-plugin/marketplace.json
├── .claude-plugin/marketplace.json
├── plugins/
│   ├── real-mcp/
│   │   ├── .cursor-plugin/  .claude-plugin/  .codex-plugin/  .agents/
│   │   ├── skills/          (connect · session · policy · contacts · ops)
│   │   ├── commands/        (validate · list-contacts · project-summary)
│   │   ├── mcp.json  .mcp.json  codex.mcp.json
│   │   └── assets/
│   ├── s1mple-mcp/
│   └── infinity-labs-mcp/
├── LICENSE
├── SECURITY.md
├── CHANGELOG.md
├── PUBLISH.md
└── README.md
```

## 使用者流程（安裝 → 授權 → 驗證 → 撤銷）

1. **安裝**對應站的 plugin（Cursor Team Marketplace／Import from Repo，或其他 host 的 plugin 目錄）。
2. **Authenticate**：在 MCP 設定對該 server 按授權；瀏覽器登入該站 → 選專案 → 允許。無需手貼 Token。
3. **驗證**：執行命令 `validate-<brand>-setup`，或請 Agent 使用 `<brand>-session`（會打 `workspace_summary`）。
4. **日常**：`list-contacts`／`project-summary`，或口語「查聯絡人」「專案摘要」。
5. **撤銷**：到該站後台 MCP／已授權應用撤銷 grant（卸載 plugin **不會**自動撤銷伺服器端授權）。詳見 [SECURITY.md](./SECURITY.md)。

## Skills 對應的真實工具

唯讀：`workspace_summary`、`contacts_list`、`contact_get`、`reservations_list`、`dispatch_list`、`knowledge_search`、`memory_list`  
寫入（多為儀表板核准提案）：`memory_upsert`、`contact_add_tag`、`contact_append_note`、`reservation_*`、`dispatch_create`、`escalate_to_human`

寫入前 Agent 必須先確認意圖（見各站 `*-universal-workflow` skill）。

## 下一步

見 [PUBLISH.md](./PUBLISH.md)：建立公開 GitHub repo →（可選）送 Cursor Marketplace 審核。
""",
    )

    # Refresh PUBLISH note about multi-host without rewriting entire file intent
    publish = (ROOT / "PUBLISH.md").read_text(encoding="utf-8")
    if "Claude／Codex" not in publish:
        publish = publish.replace(
            "## D. 本包開了什麼、沒開什麼",
            """## D. 多 host 清單

各 `plugins/*` 已含 `.cursor-plugin`、`.claude-plugin`、`.codex-plugin`、`.agents`。  
根目錄另有 `.claude-plugin/marketplace.json`（三站並列）。送審時以目標 host 文件為準；Cursor 仍以根目錄 `.cursor-plugin/marketplace.json` 為主。

## E. 本包開了什麼、沒開什麼""",
        )
        write(ROOT / "PUBLISH.md", publish)


def main() -> None:
    for b in BRANDS:
        gen_brand(b)
    gen_root()
    print("OK")


if __name__ == "__main__":
    main()
