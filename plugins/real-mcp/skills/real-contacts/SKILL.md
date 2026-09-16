---
name: real-contacts
description: List/search REAL contacts and tags via MCP (contacts_list, contacts_search, contact_get, tags_list).
---

# Skill: real-contacts

**Prerequisite:** `real-universal-workflow`. Auth issues → `real-session` + `references/error-recovery.md`.

## MCP tools

- `contacts_list` — recent contacts (max 50). Params: `limit`, optional `q` name.
- `contacts_search` — finer search: optional `q` (name／external id), `tag`, `platform`, `limit`.
- `contact_get` — one contact by `contact_id`.
- `tags_list` — tag catalog + holder counts; optional `q`, `limit`.

## Workflow

1. Prefer `contacts_search` when the user gives a tag/platform/id fragment.
2. Use `tags_list` before tagging or broadcast-by-tag.
3. Detail with `contact_get`.

## Writes (proposal)

- `contact_add_tag` — required `contact_id`, `tag`
- `contact_append_note` — required `contact_id`, `note`

Confirm with write-lifecycle first; remind dashboard approval may be required.
