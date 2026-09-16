# Write lifecycle (INFINITY LABS)

## Before any write / proposal tool

1. Restate the intended business outcome in one short sentence (who / what / when).
2. Wait for an explicit user confirmation (yes / 確認 / 可以).
3. Only then call the tool.

Applies to: `memory_upsert`, `contact_add_tag`, `contact_append_note`,
`reservation_update_status`, `reservation_reschedule`, `dispatch_create`,
`escalate_to_human`, `message_send`, `broadcast_create`, `knowledge_upsert`,
`flow_set_enabled`, `flow_start`.

### message_send preview-gate

1. Call `message_preview` (same `contact_id` + `text`).
2. Show the preview body to the user; wait for explicit confirmation.
3. Only then call `message_send` with the same text **and** `preview_token`.
4. Dashboard approval is still required before the guest receives the message.

Rich cards / carousels are **not** sendable via MCP — use the INFINITY LABS dashboard.

## After the tool returns

- Many writes are **proposals** that still need human approval in the INFINITY LABS dashboard.
- Say clearly: may need dashboard approval — do **not** claim the change is live
  unless the tool result says so.
- If the user cancels, do not call the tool.

## Invalidation

If the user changes the intended outcome after confirming, confirm again before calling.
