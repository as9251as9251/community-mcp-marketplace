# Changelog

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
