# INFINITY LABS MCP plugin

Points agents at **https://infinity-labs.zeabur.app/api/mcp/v1/jsonrpc** and uses OAuth Authenticate.

Built on **our** merchant charter (not a generic CRM skill pack):
multi-brand isolation, OAuth project scope, read-first, proposal writes.

See repo root: [`docs/我們的Skill設計.md`](../../docs/我們的Skill設計.md)

Includes:

- Skills: connect, session, charter/policy, contacts, inbox, investigate, messaging, broadcast, flows, reservations, dispatch, knowledge, memory, ops
- References: merchant-charter, write-lifecycle, timezone-policy, investigate-playbook, broadcast-status-cases, brand-isolation, product-terms, error-recovery
- Commands: validate, whoami, contacts, tags, inbox, search-messages, investigate-week, broadcasts, draft-broadcast, draft-message, proposals, flows, summary, reservations, dispatch, knowledge, escalate, explain-capabilities
- Host manifests: Cursor, Claude, Codex, Agents

No product source code. Data stays on `infinity-labs.zeabur.app`.

## Quick start

1. Install this plugin
2. Authenticate the `infinity-labs` MCP server
3. Run **validate-infinity-labs-setup** or **explain-capabilities**
4. Revoke later in INFINITY LABS dashboard → MCP / connected apps
