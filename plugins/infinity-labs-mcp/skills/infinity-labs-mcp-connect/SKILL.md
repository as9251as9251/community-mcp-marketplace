---
name: infinity-labs-mcp-connect
description: Connect an agent to INFINITY LABS (infinity-labs.zeabur.app) via MCP OAuth Authenticate. Use when the user wants to install, reconnect, or understand the thin MCP shell.
---

# INFINITY LABS MCP connect

## What this is

A thin connector. The MCP server lives at `https://infinity-labs.zeabur.app/api/mcp/v1/jsonrpc`.
Product code and customer data stay on INFINITY LABS servers — this plugin only points the agent at that URL.

## How to connect

1. Ensure this plugin is installed (MCP server `infinity-labs` should appear).
2. Open MCP settings and click **Authenticate** / connect for `infinity-labs`.
3. Sign in on infinity-labs.zeabur.app in the browser, pick a project (workspace), allow access.
4. Prefer the `infinity-labs-session` skill next to verify the session.

## Do not

- Do not invent tokens or paste long-lived keys unless the user explicitly uses the dashboard advanced key flow.
- Do not call other brands' domains from this skill.
- Do not ask the user to paste OAuth codes into chat.
