---
name: s1mple-mcp-connect
description: Connect an agent to s1mple (s1mple-pro.com) via MCP OAuth Authenticate. Use when the user wants to install, reconnect, or understand the thin MCP shell.
---

# s1mple MCP connect

## What this is

A thin connector. The MCP server lives at `https://s1mple-pro.com/api/mcp/v1/jsonrpc`.
Product code and customer data stay on s1mple servers — this plugin only points the agent at that URL.

## How to connect

1. Ensure this plugin is installed (MCP server `s1mple` should appear).
2. Open MCP settings and click **Authenticate** / connect for `s1mple`.
3. Sign in on s1mple-pro.com in the browser, pick a project (workspace), allow access.
4. Prefer the `s1mple-session` skill next to verify the session.

## Do not

- Do not invent tokens or paste long-lived keys unless the user explicitly uses the dashboard advanced key flow.
- Do not call other brands' domains from this skill.
- Do not ask the user to paste OAuth codes into chat.
