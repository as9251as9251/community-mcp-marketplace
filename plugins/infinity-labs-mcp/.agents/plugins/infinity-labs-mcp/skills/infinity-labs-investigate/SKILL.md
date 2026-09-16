---
name: infinity-labs-investigate
description: Search INFINITY LABS inbox message bodies with messages_search (read-only, max 30-day window). Use for keyword investigation before drafting replies or FAQ.
---

# Skill: infinity-labs-investigate

**Prerequisite:** `infinity-labs-universal-workflow` + `references/error-recovery.md`.

## MCP tools

- `messages_search` — required `q`; optional `contact_id`, `days` (1–30, default 14), `limit` 1–50.

## Workflow

1. Always pass a real keyword in `q`. Prefer concrete nouns (product names, order ids) over vague verbs.
2. If the user names a period, set `days` explicitly (cap 30). Do not claim coverage beyond the window returned in `since` / `days`.
3. Cite message ids / contact names from the result; do not invent quotes.
4. For opening a full recent thread after a hit, use `infinity-labs-inbox` → `conversation_get`.
5. If the user wants a reply, hand off to `infinity-labs-messaging` (preview-gate) — do not send from this skill.
6. If hits suggest a reusable FAQ, propose drafting knowledge text for the user to confirm; do not invent `knowledge_upsert` if missing from `tools/list`.

## Guardrails

- Read-only. No send / broadcast / CRM writes here.
- Hard max **30 days** — split longer asks into multiple windows and say so.
- Timezone for windows is server UTC unless the tool payload says otherwise; say so if the user asks.
