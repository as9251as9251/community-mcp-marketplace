---
name: infinity-labs-flows
description: Inspect INFINITY LABS multi-step DM journeys (flows_list, flow_get, flow_sessions_list). Read-only.
---

# Skill: infinity-labs-flows

**Prerequisite:** `infinity-labs-universal-workflow`.

## MCP tools

- `flows_list` — journey summaries (`enabled_only` optional, `limit`)
- `flow_get` — one journey summary by `flow_id` (no full steps JSON)
- `flow_sessions_list` — run status; filter `contact_id` / `flow_id` / `status`

## Workflow

1. List or get definition summary.
2. For “is this guest in a journey?”, use `flow_sessions_list` with `contact_id`.
3. Do not invent create/start/pause tools — not exposed on MCP yet.
