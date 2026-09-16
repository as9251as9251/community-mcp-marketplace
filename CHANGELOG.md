# Changelog

## 1.7.0

- Session/ops: `mcp_whoami`, `mcp_usage_summary`, `proposals_list`.
- Messaging preview-gate: `message_preview` → `message_send` requires matching `preview_token` (plain text only).
- Skills: session/ops/messaging/investigate thickened; commands `whoami`, `list-proposals`, `draft-message`.

## 1.6.0

- P2 MCP: `tags_list`, `contacts_search`, `flows_list`, `flow_get`, `flow_sessions_list`.
- Skills: expand contacts; add `*-flows`; commands `list-tags`, `list-flows`.

## 1.5.0

- P1 MCP: `message_send` (approve → send), `broadcast_list`, `broadcast_audience_preview`, `broadcast_create` (approve → draft only).
- Skills: `*-messaging`, `*-broadcast`; commands: `list-broadcasts`, `draft-broadcast`.

## 1.4.0

- MCP P0 tools (product): `inbox_list`, `conversation_get`, `messages_search` on all three brands.
- Skills: `*-inbox`, `*-investigate`; commands: `list-inbox`, `search-messages`.

## 1.3.0

- Publish our own skill design: `docs/我們的Skill設計.md` (merchant charter).
- Add `references/merchant-charter.md` and command `explain-capabilities`.
- Reframe policy skill as merchant charter (read-first, proposal writes, multi-brand).

## 1.2.0

- Split domain skills: reservations, dispatch, knowledge, memory (ops becomes overview + router).
- Add `references/`: write-lifecycle, brand-isolation, product-terms, error-recovery.
- Add commands: list-reservations, list-dispatch, search-knowledge, escalate-human.
- Harden session skill guidance for 401/403/429 and missing allowlisted tools.

## 1.1.0

- Add session / universal-workflow / contacts / ops skills per brand.
- Add commands: validate-*-setup, list-contacts, project-summary.
- Add Claude / Codex / Agents host manifests.
- Document install → Authenticate → validate → revoke.

## 1.0.0

- Initial thin Cursor marketplace shells (MCP URL + connect skill).
