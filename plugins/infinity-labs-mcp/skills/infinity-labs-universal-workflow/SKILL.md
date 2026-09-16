---
name: infinity-labs-universal-workflow
description: Shared INFINITY LABS policy for customer language, write confirmation, brand isolation, and OAuth. Non-operational prerequisite for every INFINITY LABS workflow skill.
---

# Skill: infinity-labs-universal-workflow

This is a **policy** skill, not an operational workflow. Read it before other `infinity-labs-*` skills use tools.

## Mandatory core

1. **Customer language first** — Explain outcomes in plain product terms (聯絡人、預約、派工、知識庫、記憶). Lead with business meaning, not internal IDs, unless the user asks for IDs.
2. **Confirm before writes** — Tools that *propose* changes (`contact_add_tag`, `contact_append_note`, `reservation_update_status`, `reservation_reschedule`, `dispatch_create`, `escalate_to_human`, `memory_upsert`) need an explicit user confirmation of the intended outcome **before** the tool call. Summarize who/what/when in one short sentence.
3. **Writes are proposals** — Many write tools create actions that still need human approval in the INFINITY LABS dashboard. After calling, say they may need dashboard approval — do not claim the change already went live unless the tool result says so.
4. **Brand isolation** — Only use MCP server `infinity-labs` and domain `infinity-labs.zeabur.app`. Never call other merchant brands interchangeably from this skill set.
5. **Allowlist** — If a tool is missing from `tools/list`, it is disabled for this project. Do not invent tool names.

## Synonym routing

| User says | Route to |
|---|---|
| 連線／驗證／登入 MCP／設定好了嗎 | `infinity-labs-session` |
| 聯絡人／客戶／查誰 | `infinity-labs-contacts` |
| 預約／派工／摘要／知識庫／FAQ／記憶 | `infinity-labs-ops` |
| 怎麼裝／Authenticate | `infinity-labs-mcp-connect` |

## What this skill does not do

- It does not replace domain skills.
- It does not invent MCP tools beyond the server allowlist.
