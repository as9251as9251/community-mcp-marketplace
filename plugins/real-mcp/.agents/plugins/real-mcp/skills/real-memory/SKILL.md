---
name: real-memory
description: List or upsert internal guest memory on REAL (memory_list, memory_upsert). Memory is internal — not sent to the guest directly.
---

# Skill: real-memory

**Prerequisite:** `real-universal-workflow` + `references/write-lifecycle.md` before upsert.

## MCP tools

- `memory_list` — required `contact_id`; optional `q`, `limit` 1–20 (default 8). Read-only.
- `memory_upsert` — required `contact_id`, `body`; optional `kind` (`preference|fact|history|note`), optional `key` (same key overwrites).

## Workflow

1. Resolve `contact_id` via `real-contacts` / `real-inbox` if needed.
2. List/search first when the user asks what is remembered.
3. Confirm before upsert; clarify this is **internal** staff memory.
