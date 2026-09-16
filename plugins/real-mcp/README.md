# REAL MCP plugin

Points agents at **https://realvip.cc/api/mcp/v1/jsonrpc** and uses OAuth Authenticate.

Built on **our** merchant charter (not a generic CRM skill pack):
multi-brand isolation, OAuth project scope, read-first, proposal writes.

See repo root: [`docs/我們的Skill設計.md`](../../docs/我們的Skill設計.md)

Includes:

- Skills: connect, session, charter/policy, contacts, inbox, investigate, messaging, broadcast, reservations, dispatch, knowledge, memory, ops
- References: merchant-charter, write-lifecycle, brand-isolation, product-terms, error-recovery
- Commands: validate, contacts, inbox, search-messages, broadcasts, draft-broadcast, summary, reservations, dispatch, knowledge, escalate, explain-capabilities
- Host manifests: Cursor, Claude, Codex, Agents

No product source code. Data stays on `realvip.cc`.

## Quick start

1. Install this plugin
2. Authenticate the `real` MCP server
3. Run **validate-real-setup** or **explain-capabilities**
4. Revoke later in REAL dashboard → MCP / connected apps
