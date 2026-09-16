# Security

## Reporting

Report security issues through the support channel of the brand whose MCP URL you use
(REAL / s1mple / INFINITY LABS). Do not open public issues that include tokens or customer data.

## Revoking access

Removing a marketplace plugin from an agent does **not** by itself revoke server-side OAuth grants.

To revoke:

1. Sign in to that brand's dashboard.
2. Open **MCP** (or connected apps / agent authorizations).
3. Revoke the grant for the agent / client you no longer trust.

You can also re-Authenticate after Logout on the agent side if the token is stale.
