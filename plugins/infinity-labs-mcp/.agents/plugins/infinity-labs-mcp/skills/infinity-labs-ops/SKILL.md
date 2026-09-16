---
name: infinity-labs-ops
description: INFINITY LABS project ops via MCP — summary, reservations, dispatch, knowledge search, memory, and human-approved write proposals.
---

# Skill: infinity-labs-ops

**Prerequisite:** Read `skills/infinity-labs-universal-workflow/SKILL.md`. If auth fails, use `infinity-labs-session` recovery first.

## Read tools

- `workspace_summary` — counts for contacts / reservations / dispatch jobs
- `reservations_list` — recent reservations (`status` optional, `limit` 1–50)
- `dispatch_list` — dispatch jobs (`status` optional, `limit` 1–50)
- `knowledge_search` — shop FAQ / price / policy facts (`q`, `limit` 1–10)
- `memory_list` — long-term guest memory (`q` optional, `limit` 1–20)

## Write / proposal tools (confirm first)

- `memory_upsert` — upsert internal memory (`body` required; optional `kind`, `key`)
- `contact_add_tag` — propose tag
- `contact_append_note` — propose internal note
- `reservation_update_status` — propose status change
- `reservation_reschedule` — propose new `starts_at` (ISO)
- `dispatch_create` — propose a dispatch job
- `escalate_to_human` — propose handoff to a human agent

## Workflow

1. Prefer reads (`workspace_summary`, lists, `knowledge_search`) to answer questions.
2. Before any write/proposal tool: confirm the intended business outcome in one sentence; wait for explicit yes.
3. After a proposal tool: remind that dashboard approval may still be required.

## Guardrails

- Never claim a proposed write is live without confirmation from the tool/dashboard.
- Stay on `infinity-labs` / `infinity-labs.zeabur.app` only.
