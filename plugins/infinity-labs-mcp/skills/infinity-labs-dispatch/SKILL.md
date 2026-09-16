---
name: infinity-labs-dispatch
description: List INFINITY LABS dispatch jobs, propose new jobs, or escalate to a human (dispatch_list, dispatch_create, escalate_to_human).
---

# Skill: infinity-labs-dispatch

**Prerequisite:** `infinity-labs-universal-workflow` + `references/write-lifecycle.md` for any write.

## Read

- `dispatch_list` — `status` optional, `limit` 1–50

## Write / proposal (confirm first)

- `dispatch_create` — optional `title`, `region`, `notes`, `customer_name`, `customer_phone`
- `escalate_to_human` — optional `reason` (pauses bot after approval)

## Workflow

1. Prefer `dispatch_list` for status questions.
2. Confirm before create/escalate; remind approval may be required.
