---
name: s1mple-inbox
description: Browse s1mple Unified Inbox threads (inbox_list, conversation_get). Read-only message-center triage.
---

# Skill: s1mple-inbox

**Prerequisite:** `s1mple-universal-workflow`. Auth issues → `s1mple-session`.

## MCP tools

- `inbox_list` — recent threads. Params: optional `folder` (`open|pending|done`), `platform`, `q`, `limit` 1–50.
- `conversation_get` — one contact summary + recent messages. Required `contact_id`; optional `limit` 1–50 (default 30).

## Workflow

1. Triage with `inbox_list` (folder/platform/name as needed).
2. Open a thread with `conversation_get`.
3. For keyword / period search across the project, hand off to `s1mple-investigate` (`messages_search`).

## Guardrails

- Read-only. Sending messages is not in this skill (no MCP send tool yet).
- Do not treat `inbox_list` as a full historical census of every contact.
