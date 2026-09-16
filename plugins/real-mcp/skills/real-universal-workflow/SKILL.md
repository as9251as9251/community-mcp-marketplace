---
name: real-universal-workflow
description: REAL merchant charter policy — language, proposal writes, brand isolation, errors. Prerequisite for every REAL workflow skill.
---

# Skill: real-universal-workflow（商家憲章）

This is the **REAL merchant charter** skill (policy), not an operational workflow.
Read before other `real-*` skills use tools.

Canonical design: repo `docs/我們的Skill設計.md` · local summary `references/merchant-charter.md`.

## Mandatory references

- `references/merchant-charter.md` — our product rules in one page
- `references/product-terms.md` — customer-facing wording
- `references/write-lifecycle.md` — confirm → propose → approve
- `references/brand-isolation.md` — `real` / `realvip.cc` only
- `references/error-recovery.md` — auth / 429 / missing tools

## Mandatory core

1. **Read first, propose second** — lists/summary/search before writes.
2. **Confirm before writes** — follow write-lifecycle for every proposal tool.
3. **Proposal ≠ live** — remind dashboard approval unless the result says applied.
4. **Allowlist** — missing from `tools/list` means disabled; do not invent names.
5. **Brand isolation** — only MCP `real` on `realvip.cc`.

## Synonym routing

| User says | Route to |
|---|---|
| 連線／驗證／登入 MCP／設定好了嗎 | `real-session` |
| 你能做什麼／憲章／邊界 | 本 skill ＋ `references/merchant-charter.md` |
| 聯絡人／客戶／查誰 | `real-contacts` |
| 收件匣／訊息中心／誰找過 | `real-inbox` |
| 搜訊息／查對話內容／關鍵字 | `real-investigate` |
| 預約 | `real-reservations` |
| 派工 | `real-dispatch` |
| 知識庫／FAQ／價目／店規 | `real-knowledge` |
| 記憶／偏好 | `real-memory` |
| 專案摘要／總覽 | `real-ops` |
| 轉真人 | `real-dispatch` |
| 怎麼裝／Authenticate | `real-mcp-connect` |

## What this skill does not do

- It does not replace domain skills.
- It does not invent MCP tools beyond the server allowlist.
- It does not copy other products' feature catalogs.
