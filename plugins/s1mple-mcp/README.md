# s1mple MCP plugin

Points agents at **https://s1mple-pro.com/api/mcp/v1/jsonrpc** and uses OAuth Authenticate.

Includes:

- Skills: connect, session validation, shared policy, contacts, ops
- Commands: validate setup, list contacts, project summary
- Host manifests: Cursor, Claude, Codex, Agents

No product source code is included. Data stays on `s1mple-pro.com`.

## Quick start

1. Install this plugin
2. Authenticate the `s1mple` MCP server
3. Run command **validate-s1mple-setup** (or ask the agent to use `s1mple-session`)
4. To revoke access later: open s1mple dashboard → MCP / connected apps → revoke the grant
