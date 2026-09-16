---
name: s1mple-universal-workflow
description: s1mple merchant charter policy — language, proposal writes, brand isolation, errors. Prerequisite for every s1mple workflow skill.
---

# Skill: s1mple-universal-workflow（商家憲章）

This is the **s1mple merchant charter** skill (policy), not an operational workflow.
Read before other `s1mple-*` skills use tools.

Canonical design: repo `docs/我們的Skill設計.md` · local summary `references/merchant-charter.md`.

## Mandatory references

- `references/merchant-charter.md` — our product rules in one page
- `references/product-terms.md` — customer-facing wording
- `references/write-lifecycle.md` — confirm → propose → approve
- `references/brand-isolation.md` — `s1mple` / `s1mple-pro.com` only
- `references/error-recovery.md` — auth / 429 / missing tools

## Mandatory core

1. **Read first, propose second** — lists/summary/search before writes.
2. **Confirm before writes** — follow write-lifecycle for every proposal tool.
3. **Proposal ≠ live** — remind dashboard approval unless the result says applied.
4. **Allowlist** — missing from `tools/list` means disabled; do not invent names.
5. **Brand isolation** — only MCP `s1mple` on `s1mple-pro.com`.

## Synonym routing

| User says | Route to |
|---|---|
| 連線／驗證／登入 MCP／設定好了嗎 | `s1mple-session` |
| 你能做什麼／憲章／邊界 | 本 skill ＋ `references/merchant-charter.md` |
| 聯絡人／客戶／查誰 | `s1mple-contacts` |
| 預約 | `s1mple-reservations` |
| 派工 | `s1mple-dispatch` |
| 知識庫／FAQ／價目／店規 | `s1mple-knowledge` |
| 記憶／偏好 | `s1mple-memory` |
| 專案摘要／總覽 | `s1mple-ops` |
| 轉真人 | `s1mple-dispatch` |
| 怎麼裝／Authenticate | `s1mple-mcp-connect` |

## What this skill does not do

- It does not replace domain skills.
- It does not invent MCP tools beyond the server allowlist.
- It does not copy other products' feature catalogs.
