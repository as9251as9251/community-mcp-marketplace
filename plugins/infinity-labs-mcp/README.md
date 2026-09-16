# INFINITY LABS MCP plugin

Points agents at **https://infinity-labs.zeabur.app/api/mcp/v1/jsonrpc** and uses OAuth Authenticate.

Includes:

- Skills: connect, session validation, shared policy, contacts, ops
- Commands: validate setup, list contacts, project summary
- Host manifests: Cursor, Claude, Codex, Agents

No product source code is included. Data stays on `infinity-labs.zeabur.app`.

## Quick start

1. Install this plugin
2. Authenticate the `infinity-labs` MCP server
3. Run command **validate-infinity-labs-setup** (or ask the agent to use `infinity-labs-session`)
4. To revoke access later: open INFINITY LABS dashboard → MCP / connected apps → revoke the grant
