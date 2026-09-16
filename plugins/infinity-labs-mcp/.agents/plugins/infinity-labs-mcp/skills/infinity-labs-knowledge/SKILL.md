---
name: infinity-labs-knowledge
description: Search or propose upserts to INFINITY LABS shop knowledge base (knowledge_search, knowledge_upsert).
---

# Skill: infinity-labs-knowledge

**Prerequisite:** `infinity-labs-universal-workflow` + `references/write-lifecycle.md` before upsert.

## Read

- `knowledge_search` — `q` keyword, `limit` 1–10 (default 5).

## Write / proposal

- `knowledge_upsert` — required `title`, `body`; optional `category`, `entry_id` (update), `enabled`.

## Workflow

1. Search first with the user's question as `q`.
2. Summarize answers; cite snippets; do not invent shop facts.
3. To add/update FAQ from investigation: confirm title/body → `knowledge_upsert` → remind dashboard approval.
