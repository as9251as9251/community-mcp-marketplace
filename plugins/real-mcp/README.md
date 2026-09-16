# REAL MCP plugin

Points agents at **https://realvip.cc/api/mcp/v1/jsonrpc** and uses OAuth Authenticate.

Includes:

- Skills: connect, session validation, shared policy, contacts, ops
- Commands: validate setup, list contacts, project summary
- Host manifests: Cursor, Claude, Codex, Agents

No product source code is included. Data stays on `realvip.cc`.

## Quick start

1. Install this plugin
2. Authenticate the `real` MCP server
3. Run command **validate-real-setup** (or ask the agent to use `real-session`)
4. To revoke access later: open REAL dashboard → MCP / connected apps → revoke the grant
