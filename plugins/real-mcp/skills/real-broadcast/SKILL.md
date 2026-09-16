---
name: real-broadcast
description: List broadcasts, preview audience size, and propose draft broadcasts on REAL (broadcast_list, broadcast_audience_preview, broadcast_create).
---

# Skill: real-broadcast

**Prerequisite:** `real-universal-workflow` + `references/write-lifecycle.md` for create.

## Read

- `broadcast_list` — recent tasks (`limit` 1–50)
- `broadcast_audience_preview` — eligible counts for `platform` + `target_type` (`all|tag`) + optional `target_tag`

## Write / proposal

- `broadcast_create` — propose a **draft** (`message` required; optional `name`, `platform`, `target_type`, `target_tag`). After approval a draft is created — user must still press Send in the Broadcast page.

## Workflow

1. Preview audience before creating.
2. Confirm name / platform / target / message.
3. Call `broadcast_create`; explain draft ≠ sent.
