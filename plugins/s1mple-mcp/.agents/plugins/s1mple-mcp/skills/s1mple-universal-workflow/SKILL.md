---
name: s1mple-universal-workflow
description: Shared s1mple policy for customer language, write confirmation, brand isolation, and errors. Non-operational prerequisite for every s1mple workflow skill.
---

# Skill: s1mple-universal-workflow

This is a **policy** skill, not an operational workflow. Read it before other `s1mple-*` skills use tools.

## Mandatory references (read as needed)

- `references/product-terms.md` — customer-facing wording
- `references/write-lifecycle.md` — confirm before writes; proposal ≠ live
- `references/brand-isolation.md` — `s1mple` / `s1mple-pro.com` only
- `references/error-recovery.md` — auth / 429 / missing tools

## Mandatory core

1. **Customer language first** — use product terms from the reference.
2. **Confirm before writes** — follow write-lifecycle for every proposal tool.
3. **Allowlist** — if a tool is missing from `tools/list`, it is disabled; do not invent names.
4. **Brand isolation** — only MCP `s1mple` on `s1mple-pro.com`.

## Synonym routing

| User says | Route to |
|---|---|
| 連線／驗證／登入 MCP／設定好了嗎 | `s1mple-session` |
| 聯絡人／客戶／查誰 | `s1mple-contacts` |
| 預約 | `s1mple-reservations` |
| 派工 | `s1mple-dispatch` |
| 知識庫／FAQ／價目／店規 | `s1mple-knowledge` |
| 記憶／偏好 | `s1mple-memory` |
| 專案摘要／總覽 | `s1mple-ops` |
| 轉真人 | `s1mple-dispatch`（escalate）或 `s1mple-ops` |
| 怎麼裝／Authenticate | `s1mple-mcp-connect` |

## What this skill does not do

- It does not replace domain skills.
- It does not invent MCP tools beyond the server allowlist.
