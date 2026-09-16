---
name: infinity-labs-session
description: Validate INFINITY LABS MCP session by listing tools and calling workspace_summary. Use when verifying authentication, after OAuth, or when other INFINITY LABS skills fail with 401/403/429.
---

# Skill: infinity-labs-session

**Prerequisite:** Read `skills/infinity-labs-universal-workflow/SKILL.md` before operational work.
**Errors:** Read `references/error-recovery.md`.

This skill uses the `infinity-labs` MCP server. Authentication is managed by the agent through MCP OAuth.

## MCP tools (session check)

- Prefer `tools/list` (or the host equivalent) to confirm tools are visible.
- Call `workspace_summary` — project name plus contact / reservation / dispatch counts (read-only). No arguments.

## Workflow

1. Confirm the `infinity-labs` MCP server is connected.
2. Call `workspace_summary`.
3. If it succeeds, briefly tell the user which project is bound and what you can help with
   (contacts, reservations, dispatch, knowledge, memory, proposed writes needing approval).
4. On auth failure, follow `references/error-recovery.md`, then retry `workspace_summary`.

## Guardrails

- Stay read-only in this skill.
- Do not collect passwords or TOTP in chat.
- Do not paste, export, or request MCP access tokens.
- Scope is the project chosen during OAuth consent only.
