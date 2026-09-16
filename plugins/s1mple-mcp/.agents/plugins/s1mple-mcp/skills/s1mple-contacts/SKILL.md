---
name: s1mple-contacts
description: List/search s1mple contacts and tags via MCP (contacts_list, contacts_search, contact_get, tags_list).
---

# Skill: s1mple-contacts

**Prerequisite:** `s1mple-universal-workflow`. Auth issues → `s1mple-session` + `references/error-recovery.md`.

## MCP tools

- `contacts_list` — recent contacts (max 50). Params: `limit`, optional `q` name.
- `contacts_search` — finer search: optional `q` (name／external id), `tag`, `platform`, `limit`.
- `contact_get` — one contact by `contact_id`.
- `tags_list` — tag catalog + holder counts; optional `q`, `limit`.

## Workflow

1. Prefer `contacts_search` when the user gives a tag/platform/id fragment.
2. Use `tags_list` before tagging or broadcast-by-tag.
3. Detail with `contact_get`.

## Writes

Tagging / notes → `s1mple-ops` + write-lifecycle (proposals).
