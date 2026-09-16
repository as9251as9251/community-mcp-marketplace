---
name: s1mple-flows
description: Inspect and propose enable/start for s1mple multi-step DM journeys (flows_list, flow_get, flow_sessions_list, flow_set_enabled, flow_start).
---

# Skill: s1mple-flows

**Prerequisite:** `s1mple-universal-workflow` + `references/write-lifecycle.md` for writes.

## Read

- `flows_list` — journey summaries (`enabled_only` optional, `limit`)
- `flow_get` — one journey summary by `flow_id` (no full steps JSON)
- `flow_sessions_list` — run status; filter `contact_id` / `flow_id` / `status`

## Write / proposal

- `flow_set_enabled` — required `flow_id`, `enabled` (true/false)
- `flow_start` — required `flow_id`, `contact_id` (flow must already be enabled)

## Lifecycle

| User ask | Do |
|---|---|
| 有哪些旅程 | `flows_list` |
| 某一支細節 | `flow_get` |
| 某人是否在旅程中 | `flow_sessions_list` + `contact_id` |
| 啟用／停用 | confirm → `flow_set_enabled` → dashboard approval |
| 幫某人啟動 | confirm → `flow_start` → approval; then check sessions |
| 建立新旅程步驟圖 | **後台** — MCP 無 create/edit steps |

## Guardrails

- Do not invent create/edit-step tools.
- Reminder: proposal ≠ live until approved.
