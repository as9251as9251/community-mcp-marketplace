---
name: real-contacts
description: List and look up REAL contacts via MCP (contacts_list, contact_get). Use when the user asks about customers or contacts.
---

# Skill: real-contacts

**Prerequisite:** `real-universal-workflow`. Auth issues → `real-session` + `references/error-recovery.md`.

## MCP tools

- `contacts_list` — recent contacts (read-only, max 50). Params: `limit` (1–50, default 20), optional `q`.
- `contact_get` — one contact by `contact_id` (required, integer).

## Workflow

1. Browse/search with `contacts_list`; pass `q` for name fragments.
2. Detail with `contact_get` using an id from the list or the user.
3. Use plain product language (`references/product-terms.md`).

## Writes

Tagging / notes are **not** in this skill — use `real-ops` and `references/write-lifecycle.md`.
