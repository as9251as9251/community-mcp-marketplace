---
name: real-inbox
description: Browse REAL Unified Inbox threads (inbox_list, conversation_get). Read-only message-center triage.
---

# Skill: real-inbox

**Prerequisite:** `real-universal-workflow`. Auth issues → `real-session`.

## MCP tools

- `inbox_list` — recent threads. Params: optional `folder` (`open|pending|done`), `platform`, `q`, `limit` 1–50.
- `conversation_get` — one contact summary + recent messages. Required `contact_id`; optional `limit` 1–50 (default 30).

## Workflow

1. Triage with `inbox_list` (folder/platform/name as needed).
2. Open a thread with `conversation_get`.
3. For keyword / period search across the project, hand off to `real-investigate` (`messages_search`).

## Guardrails

- Read-only. Sending messages belongs in `real-messaging` (preview → propose → approve).
- Do not treat `inbox_list` as a full historical census of every contact.
