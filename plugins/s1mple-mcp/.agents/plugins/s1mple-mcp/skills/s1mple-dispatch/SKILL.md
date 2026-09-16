---
name: s1mple-dispatch
description: List s1mple dispatch jobs, propose new jobs, or escalate to a human (dispatch_list, dispatch_create, escalate_to_human).
---

# Skill: s1mple-dispatch

**Prerequisite:** `s1mple-universal-workflow` + `references/write-lifecycle.md` for any write.

## Read

- `dispatch_list` — `status` optional, `limit` 1–50

## Write / proposal (confirm first)

- `dispatch_create` — optional `contact_id`, `title`, `region`, `notes`, `customer_name`, `customer_phone`
- `escalate_to_human` — required `contact_id`; optional `reason` (pauses bot after approval)

## Workflow

1. Prefer `dispatch_list` for status questions.
2. Resolve `contact_id` via `s1mple-contacts` / `s1mple-inbox` before escalate (or when binding a job to a guest).
3. Confirm before create/escalate; remind approval may be required.
