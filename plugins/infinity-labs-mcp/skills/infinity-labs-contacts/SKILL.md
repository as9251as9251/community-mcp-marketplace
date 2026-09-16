---
name: infinity-labs-contacts
description: List/search INFINITY LABS contacts and tags via MCP (contacts_list, contacts_search, contact_get, tags_list).
---

# Skill: infinity-labs-contacts

**Prerequisite:** `infinity-labs-universal-workflow`. Auth issues → `infinity-labs-session` + `references/error-recovery.md`.

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

Tagging / notes → `infinity-labs-ops` + write-lifecycle (proposals).
