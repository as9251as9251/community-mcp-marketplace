# Write lifecycle (s1mple)

## Before any write / proposal tool

1. Restate the intended business outcome in one short sentence (who / what / when).
2. Wait for an explicit user confirmation (yes / 確認 / 可以).
3. Only then call the tool.

Applies to: `memory_upsert`, `contact_add_tag`, `contact_append_note`,
`reservation_update_status`, `reservation_reschedule`, `dispatch_create`,
`escalate_to_human`.

## After the tool returns

- Many writes are **proposals** that still need human approval in the s1mple dashboard.
- Say clearly: may need dashboard approval — do **not** claim the change is live
  unless the tool result says so.
- If the user cancels, do not call the tool.

## Invalidation

If the user changes the intended outcome after confirming, confirm again before calling.
