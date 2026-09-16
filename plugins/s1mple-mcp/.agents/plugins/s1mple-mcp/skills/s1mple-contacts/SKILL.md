---
name: s1mple-contacts
description: List and look up s1mple contacts via MCP (contacts_list, contact_get). Use when the user asks about customers or contacts.
---

# Skill: s1mple-contacts

**Prerequisite:** Read `skills/s1mple-universal-workflow/SKILL.md`. If auth fails, use `s1mple-session` recovery first.

## MCP tools

- `contacts_list` — recent contacts (read-only, max 50). Params: `limit` (1–50, default 20), optional `q` name keyword.
- `contact_get` — one contact by `contact_id` (required, integer).

## Workflow

1. For browse/search: `contacts_list` with a sensible `limit`; pass `q` when the user gives a name fragment.
2. For detail: `contact_get` with the id from a prior list (or the id the user provides).
3. Present names and useful fields in plain language; include ids only when helpful for follow-up.

## Guardrails

- Read-only in this skill. Tagging / notes belong in `s1mple-ops` with confirmation.
- Do not fetch other brands' contacts.
