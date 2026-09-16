---
name: infinity-labs-universal-workflow
description: INFINITY LABS merchant charter policy — language, proposal writes, brand isolation, errors. Prerequisite for every INFINITY LABS workflow skill.
---

# Skill: infinity-labs-universal-workflow（商家憲章）

This is the **INFINITY LABS merchant charter** skill (policy), not an operational workflow.
Read before other `infinity-labs-*` skills use tools.

Canonical design: repo `docs/我們的Skill設計.md` · local summary `references/merchant-charter.md`.

## Mandatory references

- `references/merchant-charter.md` — our product rules in one page
- `references/product-terms.md` — customer-facing wording + dashboard↔MCP map
- `references/write-lifecycle.md` — confirm → propose → approve (+ message preview-gate)
- `references/timezone-policy.md` — wall-clock → MCP instant encoding
- `references/brand-isolation.md` — `infinity-labs` / `infinity-labs.zeabur.app` only
- `references/error-recovery.md` — auth / 429 / missing tools

On-demand (domain):

- `references/investigate-playbook.md` — when searching / analysing messages
- `references/broadcast-status-cases.md` — when reading or drafting broadcasts

## Mandatory core

1. **Read first, propose second** — lists/summary/search before writes.
2. **Confirm before writes** — follow write-lifecycle for every proposal tool (`message_send`, `broadcast_create`, tags, reservations, …).
3. **Proposal ≠ live** — remind dashboard approval unless the result says applied. For `broadcast_create`, approval only creates a **draft** — user still sends from Broadcast page.
4. **Allowlist** — missing from `tools/list` means disabled; do not invent names.
5. **Brand isolation** — only MCP `infinity-labs` on `infinity-labs.zeabur.app`.

## Synonym routing

| User says | Route to |
|---|---|
| 連線／驗證／登入 MCP／設定好了嗎 | `infinity-labs-session` |
| 用量／呼叫次數 | `infinity-labs-session`（mcp_usage_summary） |
| 待核准／提案佇列 | `infinity-labs-ops`（proposals_list） |
| 你能做什麼／憲章／邊界 | 本 skill ＋ `references/merchant-charter.md` |
| 聯絡人／客戶／查誰 | `infinity-labs-contacts` |
| 標籤目錄 | `infinity-labs-contacts`（tags_list） |
| 收件匣／訊息中心／誰找過 | `infinity-labs-inbox` |
| 搜訊息／查對話內容／關鍵字 | `infinity-labs-investigate` |
| 發訊息／回覆客人／私訊 | `infinity-labs-messaging` |
| 群發／broadcast | `infinity-labs-broadcast` |
| 旅程／自動化流程 | `infinity-labs-flows` |
| 預約 | `infinity-labs-reservations` |
| 派工 | `infinity-labs-dispatch` |
| 知識庫／FAQ／價目／店規 | `infinity-labs-knowledge` |
| 記憶／偏好 | `infinity-labs-memory` |
| 專案摘要／總覽 | `infinity-labs-ops` |
| 轉真人 | `infinity-labs-dispatch` |
| 怎麼裝／Authenticate | `infinity-labs-mcp-connect` |

## What this skill does not do

- It does not replace domain skills.
- It does not invent MCP tools beyond the server allowlist.
- It does not copy other products' feature catalogs.
