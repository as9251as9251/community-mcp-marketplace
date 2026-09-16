---
name: s1mple-session
description: Validate s1mple MCP session by listing tools and calling workspace_summary. Use when verifying authentication, after OAuth, or when other s1mple skills fail with 401/403.
---

# Skill: s1mple-session

**Prerequisite:** Read `skills/s1mple-universal-workflow/SKILL.md` before operational work.

This skill uses the `s1mple` MCP server. Authentication is managed by the agent through MCP OAuth.

## MCP tools (session check)

- Prefer `tools/list` (or the host equivalent) to confirm tools are visible.
- Call `workspace_summary` — project name plus contact / reservation / dispatch counts (read-only). No arguments.

## Workflow

1. Confirm the `s1mple` MCP server is connected.
2. Call `workspace_summary`.
3. If it succeeds, briefly tell the user which project is bound and what you can help with (contacts, reservations, dispatch, knowledge, proposed writes that need human approval).
4. If authentication is missing/expired, follow OAuth recovery below — then retry `workspace_summary`.

## OAuth recovery

If calls fail with `401` / `403` / authentication-required for `s1mple`, **do not** ask for tokens, paste keys, or hand-edit MCP URLs.

| Agent | Recovery |
|---|---|
| Cursor | Plugin details → **MCPs** → `s1mple` → **Logout** (if present) → **Authenticate** |
| Claude Code | Uninstall this plugin, reinstall; OAuth should start on install |
| Codex / ChatGPT desktop | Uninstall this plugin, reinstall from the marketplace |
| Other hosts | Open MCP settings for `s1mple` and select **Authenticate** |

Do **not** treat network errors, timeouts, or `5xx` as OAuth failures — check connectivity first.

## Guardrails

- Stay read-only in this skill.
- Do not collect passwords or TOTP in chat.
- Do not paste, export, or request MCP access tokens.
- Scope is the project chosen during OAuth consent only.
