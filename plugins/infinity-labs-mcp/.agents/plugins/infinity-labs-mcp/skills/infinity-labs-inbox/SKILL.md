---
name: infinity-labs-inbox
description: Browse INFINITY LABS Unified Inbox threads (inbox_list, conversation_get). Read-only message-center triage.
---

# Skill: infinity-labs-inbox

**Prerequisite:** `infinity-labs-universal-workflow`. Auth issues → `infinity-labs-session`.

## MCP tools

- `inbox_list` — recent threads. Params: optional `folder` (`open|pending|done`), `platform`, `q`, `limit` 1–50.
- `conversation_get` — one contact summary + recent messages. Required `contact_id`; optional `limit` 1–50 (default 30).

## Workflow

1. Triage with `inbox_list` (folder/platform/name as needed).
2. Open a thread with `conversation_get`.
3. For keyword / period search across the project, hand off to `infinity-labs-investigate` (`messages_search`).

## Guardrails

- Read-only. Sending messages is not in this skill (no MCP send tool yet).
- Do not treat `inbox_list` as a full historical census of every contact.
