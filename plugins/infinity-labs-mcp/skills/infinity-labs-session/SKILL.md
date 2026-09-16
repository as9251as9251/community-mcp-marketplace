---
name: infinity-labs-session
description: Validate INFINITY LABS MCP session via mcp_whoami / workspace_summary and optional usage. Use when verifying authentication, after OAuth, or when other INFINITY LABS skills fail with 401/403/429.
---

# Skill: infinity-labs-session

**Prerequisite:** Read `skills/infinity-labs-universal-workflow/SKILL.md` before operational work.
**Errors:** Read `references/error-recovery.md`.

This skill uses the `infinity-labs` MCP server. Authentication is managed by the agent through MCP OAuth.

## MCP tools (session check)

- Prefer `tools/list` (or the host equivalent) to confirm tools are visible.
- Call `mcp_whoami` — brand, project name, timezone, allowlisted tool names (read-only).
- Optionally `workspace_summary` — contact / reservation / dispatch counts.
- Optionally `mcp_usage_summary` — recent MCP call counts by actor/tool (not a billing wallet).

## Workflow

1. Confirm the `infinity-labs` MCP server is connected.
2. Call `mcp_whoami`. Tell the user which brand/project is bound and roughly what tools are allowed.
3. On auth failure, follow `references/error-recovery.md`, then retry `mcp_whoami`.

## Guardrails

- Stay read-only in this skill.
- Do not collect passwords or TOTP in chat.
- Do not paste, export, or request MCP access tokens.
- Scope is the project chosen during OAuth consent only.
