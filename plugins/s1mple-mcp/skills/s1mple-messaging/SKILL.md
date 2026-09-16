---
name: s1mple-messaging
description: Propose a 1:1 text message to a s1mple contact via message_send (human approval required before send).
---

# Skill: s1mple-messaging

**Prerequisite:** `s1mple-universal-workflow` + `references/write-lifecycle.md`.

## MCP tools

- `message_send` — **proposal**. Required `contact_id`, `text` (plain text only).

## Workflow

1. Resolve `contact_id` via `s1mple-inbox` / `s1mple-contacts` if needed.
2. Confirm recipient + full message text with the user.
3. Call `message_send`. Tell the user it is pending inbox approval and will send only after approve.
4. Do not claim the guest already received it until approval/execution succeeds.

## Guardrails

- Text only. No images/stickers/cards via this skill yet.
- Never skip confirmation.
