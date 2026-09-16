---
name: infinity-labs-universal-workflow
description: Shared INFINITY LABS policy for customer language, write confirmation, brand isolation, and errors. Non-operational prerequisite for every INFINITY LABS workflow skill.
---

# Skill: infinity-labs-universal-workflow

This is a **policy** skill, not an operational workflow. Read it before other `infinity-labs-*` skills use tools.

## Mandatory references (read as needed)

- `references/product-terms.md` — customer-facing wording
- `references/write-lifecycle.md` — confirm before writes; proposal ≠ live
- `references/brand-isolation.md` — `infinity-labs` / `infinity-labs.zeabur.app` only
- `references/error-recovery.md` — auth / 429 / missing tools

## Mandatory core

1. **Customer language first** — use product terms from the reference.
2. **Confirm before writes** — follow write-lifecycle for every proposal tool.
3. **Allowlist** — if a tool is missing from `tools/list`, it is disabled; do not invent names.
4. **Brand isolation** — only MCP `infinity-labs` on `infinity-labs.zeabur.app`.

## Synonym routing

| User says | Route to |
|---|---|
| 連線／驗證／登入 MCP／設定好了嗎 | `infinity-labs-session` |
| 聯絡人／客戶／查誰 | `infinity-labs-contacts` |
| 預約 | `infinity-labs-reservations` |
| 派工 | `infinity-labs-dispatch` |
| 知識庫／FAQ／價目／店規 | `infinity-labs-knowledge` |
| 記憶／偏好 | `infinity-labs-memory` |
| 專案摘要／總覽 | `infinity-labs-ops` |
| 轉真人 | `infinity-labs-dispatch`（escalate）或 `infinity-labs-ops` |
| 怎麼裝／Authenticate | `infinity-labs-mcp-connect` |

## What this skill does not do

- It does not replace domain skills.
- It does not invent MCP tools beyond the server allowlist.
