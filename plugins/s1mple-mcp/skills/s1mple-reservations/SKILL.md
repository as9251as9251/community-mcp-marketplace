---
name: s1mple-reservations
description: List and propose updates to s1mple reservations (reservations_list, reservation_update_status, reservation_reschedule).
---

# Skill: s1mple-reservations

**Prerequisite:** `s1mple-universal-workflow` + `references/write-lifecycle.md` for any write.

## Read

- `reservations_list` — `status` optional, `limit` 1–50 (default 20)

## Write / proposal (confirm first)

- `reservation_update_status` — `reservation_id`, `status` (`pending|confirmed|cancelled|completed|no_show`)
- `reservation_reschedule` — `reservation_id`, `starts_at` (ISO), optional `ends_at`

## Workflow

1. List/filter to answer questions.
2. For status/time changes: confirm outcome → call proposal tool → remind dashboard approval may be required.
