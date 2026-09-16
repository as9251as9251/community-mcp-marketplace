# -*- coding: utf-8 -*-
"""Regenerate multi-host manifests + skills/commands for each brand plugin."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLUGINS = ROOT / "plugins"
VERSION = "1.8.0"

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
        "merchant-charter.md": f"""# {disp} merchant charter (summary)

This plugin follows **Community MCP** rules — multi-brand merchant ops, not a generic CRM clone.

1. **One brand** — MCP `{key}` on `{domain}` only. Never cross brands.
2. **OAuth project scope** — tools only see the project chosen at consent.
3. **Read first** — summary / list / search before any write.
4. **Proposal writes** — confirm intent → call tool → say dashboard approval may still be required.
5. **No invented tools** — if missing from `tools/list`, it is disabled for this project.
6. **No secrets in chat** — never ask for tokens, passwords, or OTP; use Authenticate recovery.

Full design (repo root): `docs/我們的Skill設計.md`
""",
        "write-lifecycle.md": f"""# Write lifecycle ({disp})

## Before any write / proposal tool

1. Restate the intended business outcome in one short sentence (who / what / when).
2. Wait for an explicit user confirmation (yes / 確認 / 可以).
3. Only then call the tool.

Applies to: `memory_upsert`, `contact_add_tag`, `contact_append_note`,
`reservation_update_status`, `reservation_reschedule`, `dispatch_create`,
`escalate_to_human`, `message_send`, `broadcast_create`.

### message_send preview-gate

1. Call `message_preview` (same `contact_id` + `text`).
2. Show the preview body to the user; wait for explicit confirmation.
3. Only then call `message_send` with the same text **and** `preview_token`.
4. Dashboard approval is still required before the guest receives the message.

Rich cards / carousels are **not** sendable via MCP — use the {disp} dashboard.

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
| 收件匣／訊息中心 | inbox activity list as “全庫普查” |
| 待核准提案 | “已送出給客人” without approval |
| 群發草稿 | “已群發完成” when status is draft |
| 旅程／自動化 | inventing create/start MCP tools |
| 預約 | reservation entity |
| 派工／派工單 | dispatch job payload |
| 知識庫／FAQ／價目／店規 | knowledge_search raw hits only |
| 記憶（內部） | memory_upsert internals |
| 轉真人 | escalate payload |
| 需後台核准 | “已寫入完成” without evidence |
| MCP 呼叫次數 | credits／錢包／扣款 |

## Dashboard label ↔ MCP tools

| 後台說法 | MCP |
|---|---|
| 訊息中心／收件匣 | `inbox_list`, `conversation_get` |
| 搜訊息／查關鍵字 | `messages_search` |
| 私訊客人 | `message_preview` → `message_send` |
| 群發 | `broadcast_list`, `broadcast_audience_preview`, `broadcast_create` |
| 標籤 | `tags_list`, `contact_add_tag` |
| 旅程 | `flows_list`, `flow_get`, `flow_sessions_list`（唯讀） |
| 待核准 | `proposals_list` |
| 連線／用量 | `mcp_whoami`, `mcp_usage_summary` |

If the user asks for IDs or API fields, you may disclose non-sensitive mappings.
""",
        "timezone-policy.md": f"""# Timezone policy ({disp}) — instant MCP inputs

Use when the user gives temporal language and you will put a **specific instant** into an MCP argument.

Default wall-clock timezone when the user omits one: **Asia/Taipei (UTC+8)** — also returned by `mcp_whoami.timezone`.

## Conversion rules

1. Wall-clock without timezone → interpret as Asia/Taipei and encode with `+08:00`.
2. User names a timezone / supplies `Z` / an offset → **honor it**; do not rewrite to Taipei.
3. Relative calendar language (“明天”、“下週五”) → resolve on the **effective** timezone calendar (named offset or Taipei default).
4. User gives **date only** but the tool needs an instant → ask for the clock boundary; do **not** invent midnight.
5. Do not default an omitted customer timezone to `Z`.

## Do not force this policy on

| Class | Examples |
|---|---|
| Relative duration | “等 30 分鐘”、timeout 長度 |
| Relative day windows | `messages_search.days`（往回 N 天；伺服器以 UTC `since` 截斷） |
| Returned timestamps | tool 回傳的 `created_at`／`since`（原樣引用即可） |
| Opaque tokens | pagination／preview_token |

## Reads vs writes

- **Reads:** when you encode user wall-clock into a plan, disclose the effective timezone in the same turn.
- **Writes** (e.g. `reservation_reschedule.starts_at`): show intent + timezone + encoded ISO in the write-lifecycle confirmation.

## Our tools note

- `messages_search` uses relative `days` (1–30), not `startAt`/`endAt`. Translate “上週／本月” into an explicit `days` (or say the tool cannot express arbitrary calendar bounds) and report the returned `since`.
- `mcp_usage_summary.days` is the same relative-window pattern.
""",
        "investigate-playbook.md": f"""# Investigate playbook ({disp})

Read-only. Tools: `messages_search`, optional `conversation_get`, optional `knowledge_search`.

## Tool choice

| Ask | Use | Do not |
|---|---|---|
| 誰最近找過／收件匣 | `inbox_list`（`{key}-inbox`） | treat as full DB census |
| 期間／關鍵字證據 | `messages_search` | use `inbox_list` for sentiment % |
| 單線近期上下文 | `conversation_get` | treat as a year-long corpus |

## Sample guardrails

1. Prefer ≤ **5** `messages_search` calls per user ask before summarizing.
2. Always pass real `q`. Our API **requires** a keyword — do not invent empty-corpus search.
3. Cap: `days` ≤ 30 (default 14). Longer asks → split windows and say so; do not claim full-project coverage.
4. Coverage label in the answer: report tool `days` / `since` / `count`. Use wording like「樣本／部分」when `count` hit the `limit`.
5. Cite `message_id` or contact display name + short quote from the payload. **Never fabricate** complaints or guest quotes.
6. Non-text / empty bodies: do not treat media-only rows as satisfaction signals.
7. Do not blind-retry the same failing query. On auth errors → `{key}-session`.

## FAQ thin path (from search hits)

1. Search with concrete `q` themes the user cares about.
2. Cluster recurring questions from **customer** text in the hits.
3. Optionally `knowledge_search` for duplicates already in the knowledge base.
4. Draft Q→A as **建議／綜合**; mark “樣本內無客服回覆” if you cannot verify a staff answer via `conversation_get`.
5. Do **not** call a write/upsert tool unless it appears in `tools/list` and the user confirmed write-lifecycle.

## Lenses (same tools, separate passes)

- Complaint themes → keyword pass, then theme → evidence → improvement suggestion.
- Opportunity / recurring ask → **separate** keyword pass; do not reuse one broad pull for both complaint + opportunity.
- CS quality → only if payloads clearly distinguish staff vs guest; otherwise say attribution is unavailable.
""",
        "broadcast-status-cases.md": f"""# Broadcast status cases ({disp})

Fields from `broadcast_list`: `status`, `target_count`, `sent_count`, `failed_count`, `scheduled_at`, `sent_at`.

**Audience size:** trust `broadcast_audience_preview.eligible_count` only.  
`tags_list` counts ≠ deliverable audience.

## Golden cases

| Observation | What you may say | Must not |
|---|---|---|
| `status=draft` (typical after MCP `broadcast_create` approve) | 草稿已建立；須到群發頁按發送 | 宣稱客人已收到 |
| `status` shows scheduled + future `scheduled_at` | 已排程至該時間（若後台支援） | 改排程／取消（無對應 MCP） |
| `scheduled_at` in the past but still not sent | 排程時間已過、目前狀態仍為… | 自動再 `broadcast_create` 當重送 |
| `sent` / completed + `failed_count=0` | 已送出；成功數用 `sent_count` | 發明開啟率／點擊率 |
| `failed_count>0` | 成功 `sent_count`、失敗 `failed_count`；根因不明就說不明 | 自動重送失敗名單 |
| User wants retry after failure | 重新 `broadcast_audience_preview` + 確認 + 新草稿提案 | 靜默重複同一提案 |

## After create

Approval of `broadcast_create` creates a **draft** only. Sending remains a dashboard action.
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

Then retry with `{key}-session` (`mcp_whoami` or `workspace_summary`).

## Network / `5xx` / timeout

Treat as connectivity — do **not** start OAuth recovery first. Retry once; if still failing, say the server may be down.

## Tool missing from `tools/list`

The project allowlist disabled that tool. Tell the user it is turned off for this project in the {disp} MCP settings. Do **not** invent a substitute tool name.

## Rate limit / `429`

Do not hammer retries. Tell the user to wait briefly and try again.
Customer-facing line: `這次操作無法完成，請稍後再試。`
Do not invent credit-wallet explanations; if they ask about volume, use `mcp_usage_summary` (call counts only).
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
                    f"使用 {key}-inbox 列出訊息中心最近對話。",
                    f"使用 {key}-investigate 搜尋最近訊息關鍵字。",
                    f"使用 {key}-contacts 列出最近聯絡人。",
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
description: Validate {disp} MCP session via mcp_whoami / workspace_summary and optional usage. Use when verifying authentication, after OAuth, or when other {disp} skills fail with 401/403/429.
---

# Skill: {key}-session

**Prerequisite:** Read `skills/{key}-universal-workflow/SKILL.md` before operational work.
**Errors:** Read `references/error-recovery.md`.

This skill uses the `{key}` MCP server. Authentication is managed by the agent through MCP OAuth.

## MCP tools (session check)

- Prefer `tools/list` (or the host equivalent) to confirm tools are visible.
- Call `mcp_whoami` — brand, project name, timezone, allowlisted tool names (read-only).
- Optionally `workspace_summary` — contact / reservation / dispatch counts.
- Optionally `mcp_usage_summary` — **only when the user asks** about volume／呼叫次數 (call counts, not a billing wallet).

## Workflow

1. Confirm the `{key}` MCP server is connected.
2. Call `mcp_whoami`. Tell the user which brand/project is bound and roughly what tools are allowed.
3. On auth failure, follow `references/error-recovery.md`, then retry `mcp_whoami`.

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
description: {disp} merchant charter policy — language, proposal writes, brand isolation, errors. Prerequisite for every {disp} workflow skill.
---

# Skill: {key}-universal-workflow（商家憲章）

This is the **{disp} merchant charter** skill (policy), not an operational workflow.
Read before other `{key}-*` skills use tools.

Canonical design: repo `docs/我們的Skill設計.md` · local summary `references/merchant-charter.md`.

## Mandatory references

- `references/merchant-charter.md` — our product rules in one page
- `references/product-terms.md` — customer-facing wording + dashboard↔MCP map
- `references/write-lifecycle.md` — confirm → propose → approve (+ message preview-gate)
- `references/timezone-policy.md` — wall-clock → MCP instant encoding
- `references/brand-isolation.md` — `{key}` / `{domain}` only
- `references/error-recovery.md` — auth / 429 / missing tools

On-demand (domain):

- `references/investigate-playbook.md` — when searching / analysing messages
- `references/broadcast-status-cases.md` — when reading or drafting broadcasts

## Mandatory core

1. **Read first, propose second** — lists/summary/search before writes.
2. **Confirm before writes** — follow write-lifecycle for every proposal tool (`message_send`, `broadcast_create`, tags, reservations, …).
3. **Proposal ≠ live** — remind dashboard approval unless the result says applied. For `broadcast_create`, approval only creates a **draft** — user still sends from Broadcast page.
4. **Allowlist** — missing from `tools/list` means disabled; do not invent names.
5. **Brand isolation** — only MCP `{key}` on `{domain}`.

## Synonym routing

| User says | Route to |
|---|---|
| 連線／驗證／登入 MCP／設定好了嗎 | `{key}-session` |
| 用量／呼叫次數 | `{key}-session`（mcp_usage_summary） |
| 待核准／提案佇列 | `{key}-ops`（proposals_list） |
| 你能做什麼／憲章／邊界 | 本 skill ＋ `references/merchant-charter.md` |
| 聯絡人／客戶／查誰 | `{key}-contacts` |
| 標籤目錄 | `{key}-contacts`（tags_list） |
| 收件匣／訊息中心／誰找過 | `{key}-inbox` |
| 搜訊息／查對話內容／關鍵字 | `{key}-investigate` |
| 發訊息／回覆客人／私訊 | `{key}-messaging` |
| 群發／broadcast | `{key}-broadcast` |
| 旅程／自動化流程 | `{key}-flows` |
| 預約 | `{key}-reservations` |
| 派工 | `{key}-dispatch` |
| 知識庫／FAQ／價目／店規 | `{key}-knowledge` |
| 記憶／偏好 | `{key}-memory` |
| 專案摘要／總覽 | `{key}-ops` |
| 轉真人 | `{key}-dispatch` |
| 怎麼裝／Authenticate | `{key}-mcp-connect` |

## What this skill does not do

- It does not replace domain skills.
- It does not invent MCP tools beyond the server allowlist.
- It does not copy other products' feature catalogs.
""",
    )

    skill(
        f"{key}-contacts/SKILL.md",
        f"""---
name: {key}-contacts
description: List/search {disp} contacts and tags via MCP (contacts_list, contacts_search, contact_get, tags_list).
---

# Skill: {key}-contacts

**Prerequisite:** `{key}-universal-workflow`. Auth issues → `{key}-session` + `references/error-recovery.md`.

## MCP tools

- `contacts_list` — recent contacts (max 50). Params: `limit`, optional `q` name.
- `contacts_search` — finer search: optional `q` (name／external id), `tag`, `platform`, `limit`.
- `contact_get` — one contact by `contact_id`.
- `tags_list` — tag catalog + holder counts; optional `q`, `limit`.

## Workflow

1. Prefer `contacts_search` when the user gives a tag/platform/id fragment.
2. Use `tags_list` before tagging or broadcast-by-tag.
3. Detail with `contact_get`.

## Writes

Tagging / notes → `{key}-ops` + write-lifecycle (proposals).
""",
    )

    skill(
        f"{key}-flows/SKILL.md",
        f"""---
name: {key}-flows
description: Inspect {disp} multi-step DM journeys (flows_list, flow_get, flow_sessions_list). Read-only — no create/start/pause via MCP.
---

# Skill: {key}-flows

**Prerequisite:** `{key}-universal-workflow`.

## MCP tools

- `flows_list` — journey summaries (`enabled_only` optional, `limit`)
- `flow_get` — one journey summary by `flow_id` (no full steps JSON)
- `flow_sessions_list` — run status; filter `contact_id` / `flow_id` / `status`

## Lifecycle (read-only truth)

| User ask | Do |
|---|---|
| 有哪些旅程 | `flows_list` |
| 某一支細節 | `flow_get`（只報工具回傳欄位） |
| 某人是否在旅程中 | `flow_sessions_list` + `contact_id` |
| 建立／啟動／暫停 | **後台** — MCP 無 create/start/pause；勿發明工具名 |

## Guardrails

- Report only statuses returned by the tools.
- Do not claim publish/pause succeeded via MCP.
""",
    )

    skill(
        f"{key}-inbox/SKILL.md",
        f"""---
name: {key}-inbox
description: Browse {disp} Unified Inbox threads (inbox_list, conversation_get). Read-only message-center triage — not period corpus search.
---

# Skill: {key}-inbox

**Prerequisite:** `{key}-universal-workflow`. Auth issues → `{key}-session`.

## MCP tools

- `inbox_list` — recent **activity** threads. Params: optional `folder` (`open|pending|done`), `platform`, `q`, `limit` 1–50.
- `conversation_get` — one contact summary + **recent** messages. Required `contact_id`; optional `limit` 1–50 (default 30).

## Use when / Do not use when

| Use when | Do not use when |
|---|---|
| 誰最近找過、收件匣分流 | 情緒占比／期間主題統計 → `{key}-investigate` |
| 打開某一線近期對話 | 把 list 當「全專案歷史普查」 |
| 確認某人目前資料夾／平台 | 無關鍵字的全庫搜訊（我們沒有這種工具） |

## Workflow

1. Triage with `inbox_list` (folder/platform/name as needed).
2. Open a thread with `conversation_get`.
3. For keyword / period evidence across the project, hand off to `{key}-investigate` (`messages_search`).

## Guardrails

- Read-only. Sending → `{key}-messaging` (preview → propose → approve).
- `inbox_list` ≠ message `createdAt` corpus; it is activity-oriented.
""",
    )

    skill(
        f"{key}-investigate/SKILL.md",
        f"""---
name: {key}-investigate
description: Search {disp} inbox message bodies with messages_search (read-only, max 30-day window). Load investigate-playbook for sample/FAQ rules.
---

# Skill: {key}-investigate

**Prerequisite:** `{key}-universal-workflow` + `references/error-recovery.md`.  
**On demand:** `references/investigate-playbook.md`, `references/timezone-policy.md`.

## MCP tools

- `messages_search` — required `q`; optional `contact_id`, `days` (1–30, default 14), `limit` 1–50.

## Use when / Do not use when

| Use when | Do not use when |
|---|---|
| 關鍵字／客訴主題／FAQ 草稿證據 | 「誰找過」→ `{key}-inbox` |
| 明確期間（轉成 `days`≤30） | 把 `conversation_get` 當整月語料 |
| 需可追溯引用的訊息片段 | 無 `q` 的空搜尋（API 必填關鍵字） |

## Workflow

1. Load `references/investigate-playbook.md` for caps and honesty labels.
2. Always pass a real keyword in `q`. Prefer concrete nouns over vague verbs.
3. If the user names a period, set `days` explicitly (cap 30). Report returned `since` / `count`.
4. Cite message ids / contact names from the result; do not invent quotes.
5. After a hit, optional `{key}-inbox` → `conversation_get` for recent context.
6. Reply drafting → `{key}-messaging`. FAQ draft → playbook thin path + optional `knowledge_search`.

## Guardrails

- Read-only. Prefer ≤5 searches per ask before summarizing.
- Hard max **30 days** — split longer asks; label coverage as 樣本／部分 when limited.
""",
    )

    skill(
        f"{key}-messaging/SKILL.md",
        f"""---
name: {key}-messaging
description: Preview then propose a 1:1 plain-text message on {disp} (message_preview → message_send; human approval required).
---

# Skill: {key}-messaging

**Prerequisite:** `{key}-universal-workflow` + `references/write-lifecycle.md`.

## MCP tools

- `message_preview` — **read-only gate**. Required `contact_id`, `text`. Returns preview + `preview_token` when sendable.
- `message_send` — **proposal**. Required `contact_id`, `text`, `preview_token` (same text as preview).
- Optional: `proposals_list` to see pending approvals.

## Workflow

1. Resolve `contact_id` via `{key}-inbox` / `{key}-contacts` if needed.
2. Draft text; call `message_preview`.
3. Show the preview body to the user; wait for explicit confirmation.
4. Call `message_send` with the **same** `contact_id` + `text` + `preview_token`.
5. Tell the user it is pending inbox approval — guest has **not** received it yet.
6. Do not claim delivery until approval/execution succeeds.

## Guardrails

- Plain text only via MCP. Cards / carousels / images → dashboard.
- Never skip preview or user confirmation (stricter than “text-only skip preview” products).
- If `send_supported` is false, do not call `message_send`.
""",
    )

    skill(
        f"{key}-broadcast/SKILL.md",
        f"""---
name: {key}-broadcast
description: List broadcasts, preview audience size, and propose draft broadcasts on {disp}. Read broadcast-status-cases before interpreting status.
---

# Skill: {key}-broadcast

**Prerequisite:** `{key}-universal-workflow` + `references/write-lifecycle.md` for create.  
**On demand:** `references/broadcast-status-cases.md`.

## Read

- `broadcast_list` — recent tasks (`limit` 1–50) — interpret with status-cases
- `broadcast_audience_preview` — eligible counts for `platform` + `target_type` (`all|tag`) + optional `target_tag`

## Write / proposal

- `broadcast_create` — propose a **draft** (`message` required; optional `name`, `platform`, `target_type`, `target_tag`). After approval a draft is created — user must still press Send in the Broadcast page.

## Workflow

1. Preview audience before creating. **`tags_list` count ≠ eligible_count.**
2. Confirm name / platform / target / message.
3. Call `broadcast_create`; explain draft ≠ sent.
4. When reporting progress, follow `references/broadcast-status-cases.md` — never auto-resend failures.
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
description: {disp} project overview via mcp_whoami / workspace_summary / proposals_list, and router to domain skills.
---

# Skill: {key}-ops

**Prerequisite:** `{key}-universal-workflow`.

## Primary tools

- `mcp_whoami` — brand / project / allowlisted tools
- `workspace_summary` — contacts / reservations / dispatch counts (read-only)
- `proposals_list` — pending (or filtered) write proposals awaiting dashboard approval
- `mcp_usage_summary` — optional call-volume snapshot

## When to route elsewhere

| Need | Skill |
|---|---|
| 聯絡人 | `{key}-contacts` |
| 標籤 | `{key}-contacts` |
| 收件匣／對話 | `{key}-inbox` |
| 搜訊息 | `{key}-investigate` |
| 發私訊 | `{key}-messaging` |
| 群發 | `{key}-broadcast` |
| 旅程 | `{key}-flows` |
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
        "whoami.md",
        f"""---
name: whoami
description: 使用 {key}-session 確認目前 MCP 專案與允許工具
---

使用 {key}-session 呼叫 mcp_whoami，告訴我目前綁定的品牌／專案與可用工具概況。
""",
    )
    command(
        "list-proposals.md",
        f"""---
name: list-proposals
description: 使用 {key}-ops 列出待核准提案
---

使用 {key}-ops 的 proposals_list 列出 pending 寫入提案（可依聯絡人篩選）。
""",
    )
    command(
        "draft-message.md",
        f"""---
name: draft-message
description: 使用 {key}-messaging 預覽並提議發送純文字私訊
---

使用 {key}-messaging：先 message_preview，把預覽給我確認，再 message_send（帶 preview_token）。提醒我後台核准前客人收不到。
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
        "list-inbox.md",
        f"""---
name: list-inbox
description: 使用 {key}-inbox 列出訊息中心收件匣
---

使用 {key}-inbox 的 inbox_list 列出最近對話（約 20 筆）。預設看 open；若要 pending／done 跟我說。
""",
    )
    command(
        "search-messages.md",
        f"""---
name: search-messages
description: 使用 {key}-investigate 搜尋訊息內文
---

使用 {key}-investigate（messages_search）搜尋訊息。若我還沒給關鍵字，先問我要搜什麼；時間窗預設 14 天、最多 30 天。遵守 investigate-playbook：可追溯引用、標明樣本覆蓋。
""",
    )
    command(
        "investigate-week.md",
        f"""---
name: investigate-week
description: 使用 {key}-investigate 做近 7 日關鍵字調查摘要
---

使用 {key}-investigate：先問我要查的關鍵字（可多個主題分開搜），`days=7`，依 investigate-playbook 給我可追溯摘要（勿假裝儀表板圖表）。需要回覆時再轉 {key}-messaging。
""",
    )
    command(
        "list-broadcasts.md",
        f"""---
name: list-broadcasts
description: 使用 {key}-broadcast 列出近期群發
---

使用 {key}-broadcast 的 broadcast_list 列出近期群發任務。
""",
    )
    command(
        "list-tags.md",
        f"""---
name: list-tags
description: 使用 {key}-contacts 列出標籤目錄
---

使用 {key}-contacts 的 tags_list 列出專案標籤與人數。
""",
    )
    command(
        "list-flows.md",
        f"""---
name: list-flows
description: 使用 {key}-flows 列出多步驟旅程
---

使用 {key}-flows 的 flows_list 列出多步驟私訊旅程摘要。
""",
    )
    command(
        "draft-broadcast.md",
        f"""---
name: draft-broadcast
description: 使用 {key}-broadcast 預覽受眾並提議建立群發草稿
---

使用 {key}-broadcast：先 broadcast_audience_preview 給我 eligible_count（不要用 tags_list 人數代替），確認文案／平台／對象後再 broadcast_create。提醒我核准後仍是草稿，要到群發頁才發送；狀態解讀看 broadcast-status-cases。
""",
    )
    command(
        "project-summary.md",
        f"""---
name: project-summary
description: 使用 {key}-ops 取得專案摘要
---

使用 {key}-ops 呼叫 mcp_whoami 與 workspace_summary，給我專案摘要（品牌／聯絡人／預約／派工；可順便看 proposals_list）。
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
    command(
        "explain-capabilities.md",
        f"""---
name: explain-capabilities
description: 用商家憲章說明能做／不能做的事
---

使用 {key}-universal-workflow 與 references/merchant-charter.md，用白話說明你現在能幫我做什麼、不能做什麼（含：先讀後提議、後台核准、品牌隔離）。不要誇大沒有的 MCP 工具。
""",
    )

    write(
        base / "README.md",
        f"""# {disp} MCP plugin

Points agents at **{mcp}** and uses OAuth Authenticate.

Built on **our** merchant charter (not a generic CRM skill pack):
multi-brand isolation, OAuth project scope, read-first, proposal writes.

See repo root: [`docs/我們的Skill設計.md`](../../docs/我們的Skill設計.md)

Includes:

- Skills: connect, session, charter/policy, contacts, inbox, investigate, messaging, broadcast, flows, reservations, dispatch, knowledge, memory, ops
- References: merchant-charter, write-lifecycle, timezone-policy, investigate-playbook, broadcast-status-cases, brand-isolation, product-terms, error-recovery
- Commands: validate, whoami, contacts, tags, inbox, search-messages, investigate-week, broadcasts, draft-broadcast, draft-message, proposals, flows, summary, reservations, dispatch, knowledge, escalate, explain-capabilities
- Host manifests: Cursor, Claude, Codex, Agents

No product source code. Data stays on `{domain}`.

## Quick start

1. Install this plugin
2. Authenticate the `{key}` MCP server
3. Run **validate-{key}-setup** or **explain-capabilities**
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

- Skill shell learning pass: `timezone-policy`, `investigate-playbook`, `broadcast-status-cases`.
- Thicker inbox／investigate／broadcast／flows boundaries; product-terms dashboard↔MCP map.
- Commands: `investigate-week`; harden draft-broadcast／search-messages wording.
- No new MCP tools — mechanisms only (no ChatGroup / rich-send copy).

## 1.7.0

- Session/ops: `mcp_whoami`, `mcp_usage_summary`, `proposals_list`.
- Messaging preview-gate: `message_preview` → `message_send` requires matching `preview_token` (plain text only).
- Skills: session/ops/messaging/investigate thickened; commands `whoami`, `list-proposals`, `draft-message`.

## 1.6.0

- P2 MCP: `tags_list`, `contacts_search`, `flows_list`, `flow_get`, `flow_sessions_list`.
- Skills: expand contacts; add `*-flows`; commands `list-tags`, `list-flows`.

## 1.5.0

- P1 MCP: `message_send` (approve → send), `broadcast_list`, `broadcast_audience_preview`, `broadcast_create` (approve → draft only).
- Skills: `*-messaging`, `*-broadcast`; commands: `list-broadcasts`, `draft-broadcast`.

## 1.4.0

- MCP P0 tools (product): `inbox_list`, `conversation_get`, `messages_search` on all three brands.
- Skills: `*-inbox`, `*-investigate`; commands: `list-inbox`, `search-messages`.

## 1.3.0

- Publish our own skill design: `docs/我們的Skill設計.md` (merchant charter).
- Add `references/merchant-charter.md` and command `explain-capabilities`.
- Reframe policy skill as merchant charter (read-first, proposal writes, multi-brand).

## 1.2.0

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

## 我們自己的設計（請先讀）

→ **[docs/我們的Skill設計.md](./docs/我們的Skill設計.md)**

重點不是追別人的功能清單，而是：

- 多品牌隔離  
- OAuth 綁專案  
- 先讀後提議  
- 後台核准才生效  
- Skill 只描述已上線的 MCP 工具  

## 與產品的關係

| 本 repo（可公開） | 產品站（保持私有） |
|---|---|
| `mcp.json` → `…/api/mcp/v1/jsonrpc` | FastAPI、DB、儀表板 |
| Skills／references 教 Agent 怎麼用工具 | OAuth／工具實作 |
| Commands 當快捷驗證／查詢 | 核准佇列、計費、稽核 |

## 本機結構

```text
community-mcp-marketplace/
├── docs/我們的Skill設計.md          ← 憲章（我們自己的）
├── .cursor-plugin/marketplace.json
├── .claude-plugin/marketplace.json
├── plugins/
│   ├── real-mcp/ · s1mple-mcp/ · infinity-labs-mcp/
│   │     skills/ · references/ · commands/ · host manifests
├── LICENSE · SECURITY.md · CHANGELOG.md · PUBLISH.md
└── regen_plugins.py
```

## 使用者流程（安裝 → 授權 → 驗證 → 撤銷）

1. **安裝**對應站 plugin  
2. **Authenticate**（瀏覽器登入 → 選專案 → 允許）  
3. **驗證** `validate-<brand>-setup` 或 `explain-capabilities`  
4. **日常** 聯絡人／預約／派工／知識庫  
5. **撤銷** 後台 MCP／已授權應用 — 見 [SECURITY.md](./SECURITY.md)

## Skills ↔ 真實 MCP 工具

| Skill | Tools |
|---|---|
| session / ops | `mcp_whoami`, `workspace_summary`, `mcp_usage_summary`, `proposals_list` |
| contacts | `contacts_list`, `contacts_search`, `contact_get`, `tags_list` |
| inbox | `inbox_list`, `conversation_get` |
| investigate | `messages_search` |
| messaging | `message_preview`（唯讀門檻）, `message_send`（提案，需 preview_token） |
| broadcast | `broadcast_list`, `broadcast_audience_preview`, `broadcast_create`（草稿提案） |
| flows | `flows_list`, `flow_get`, `flow_sessions_list` |
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
