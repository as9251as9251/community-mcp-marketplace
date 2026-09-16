---
name: s1mple-messaging
description: Preview then propose a 1:1 plain-text message on s1mple (message_preview → message_send; human approval required).
---

# Skill: s1mple-messaging

**Prerequisite:** `s1mple-universal-workflow` + `references/write-lifecycle.md`.

## MCP tools

- `message_preview` — **read-only gate**. Required `contact_id`, `text`. Returns preview + `preview_token` when sendable.
- `message_send` — **proposal**. Required `contact_id`, `text`, `preview_token` (same text as preview).
- Optional: `proposals_list` to see pending approvals.

## Workflow

1. Resolve `contact_id` via `s1mple-inbox` / `s1mple-contacts` if needed.
2. Draft text; call `message_preview`.
3. Show the preview body to the user; wait for explicit confirmation.
4. Call `message_send` with the **same** `contact_id` + `text` + `preview_token`.
5. Tell the user it is pending inbox approval — guest has **not** received it yet.
6. Do not claim delivery until approval/execution succeeds.

## Guardrails

- Plain text only via MCP. Cards / carousels / images → dashboard.
- Never skip preview or user confirmation.
- If `send_supported` is false, do not call `message_send`.
