# Error recovery (s1mple / `s1mple`)

## Auth (`401` / `403` / authentication-required)

Do **not** ask for tokens or paste keys. Guide re-Authenticate:

| Agent | Action |
|---|---|
| Cursor | Plugin → MCPs → `s1mple` → Logout（若有）→ Authenticate |
| Claude Code | Uninstall plugin → reinstall |
| Codex | Uninstall → reinstall from marketplace |
| Other | MCP settings for `s1mple` → Authenticate |

Then retry with `s1mple-session` (`mcp_whoami` or `workspace_summary`).

## Network / `5xx` / timeout

Treat as connectivity — do **not** start OAuth recovery first. Retry once; if still failing, say the server may be down.

## Tool missing from `tools/list`

The project allowlist disabled that tool. Tell the user it is turned off for this project in the s1mple MCP settings. Do **not** invent a substitute tool name.

## Rate limit / `429`

Do not hammer retries. Tell the user to wait briefly and try again.
Customer-facing line: `這次操作無法完成，請稍後再試。`
