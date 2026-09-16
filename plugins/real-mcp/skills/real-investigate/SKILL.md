---
name: real-investigate
description: Search REAL inbox message bodies with messages_search (read-only, max 30-day window).
---

# Skill: real-investigate

**Prerequisite:** `real-universal-workflow` + `references/error-recovery.md`.

## MCP tools

- `messages_search` — required `q`; optional `contact_id`, `days` (1–30, default 14), `limit` 1–50.

## Workflow

1. Always pass a real keyword in `q`.
2. If the user names a period, set `days` explicitly (cap 30). Do not claim coverage beyond the window returned in `since` / `days`.
3. Cite message ids / contact names from the result; do not invent quotes.
4. For opening a full recent thread after a hit, use `real-inbox` → `conversation_get`.

## Guardrails

- Read-only. No send / broadcast / CRM writes here.
- Hard max **30 days** — split longer asks into multiple windows and say so.
