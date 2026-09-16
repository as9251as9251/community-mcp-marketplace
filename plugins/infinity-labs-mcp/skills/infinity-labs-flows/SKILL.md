---
name: infinity-labs-flows
description: Inspect INFINITY LABS multi-step DM journeys (flows_list, flow_get, flow_sessions_list). Read-only — no create/start/pause via MCP.
---

# Skill: infinity-labs-flows

**Prerequisite:** `infinity-labs-universal-workflow`.

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
