---
name: real-universal-workflow
description: Shared REAL policy for customer language, write confirmation, brand isolation, and errors. Non-operational prerequisite for every REAL workflow skill.
---

# Skill: real-universal-workflow

This is a **policy** skill, not an operational workflow. Read it before other `real-*` skills use tools.

## Mandatory references (read as needed)

- `references/product-terms.md` — customer-facing wording
- `references/write-lifecycle.md` — confirm before writes; proposal ≠ live
- `references/brand-isolation.md` — `real` / `realvip.cc` only
- `references/error-recovery.md` — auth / 429 / missing tools

## Mandatory core

1. **Customer language first** — use product terms from the reference.
2. **Confirm before writes** — follow write-lifecycle for every proposal tool.
3. **Allowlist** — if a tool is missing from `tools/list`, it is disabled; do not invent names.
4. **Brand isolation** — only MCP `real` on `realvip.cc`.

## Synonym routing

| User says | Route to |
|---|---|
| 連線／驗證／登入 MCP／設定好了嗎 | `real-session` |
| 聯絡人／客戶／查誰 | `real-contacts` |
| 預約 | `real-reservations` |
| 派工 | `real-dispatch` |
| 知識庫／FAQ／價目／店規 | `real-knowledge` |
| 記憶／偏好 | `real-memory` |
| 專案摘要／總覽 | `real-ops` |
| 轉真人 | `real-dispatch`（escalate）或 `real-ops` |
| 怎麼裝／Authenticate | `real-mcp-connect` |

## What this skill does not do

- It does not replace domain skills.
- It does not invent MCP tools beyond the server allowlist.
