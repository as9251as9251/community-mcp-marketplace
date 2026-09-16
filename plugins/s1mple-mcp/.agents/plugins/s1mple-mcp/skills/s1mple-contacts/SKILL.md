---
name: s1mple-contacts
description: List and look up s1mple contacts via MCP (contacts_list, contact_get). Use when the user asks about customers or contacts.
---

# Skill: s1mple-contacts

**Prerequisite:** `s1mple-universal-workflow`. Auth issues → `s1mple-session` + `references/error-recovery.md`.

## MCP tools

- `contacts_list` — recent contacts (read-only, max 50). Params: `limit` (1–50, default 20), optional `q`.
- `contact_get` — one contact by `contact_id` (required, integer).

## Workflow

1. Browse/search with `contacts_list`; pass `q` for name fragments.
2. Detail with `contact_get` using an id from the list or the user.
3. Use plain product language (`references/product-terms.md`).

## Writes

Tagging / notes are **not** in this skill — use `s1mple-ops` and `references/write-lifecycle.md`.
