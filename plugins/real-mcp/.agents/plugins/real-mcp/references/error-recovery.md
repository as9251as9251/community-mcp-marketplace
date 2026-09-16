# Error recovery (REAL / `real`)

## Auth (`401` / `403` / authentication-required)

Do **not** ask for tokens or paste keys. Guide re-Authenticate:

| Agent | Action |
|---|---|
| Cursor | Plugin → MCPs → `real` → Logout（若有）→ Authenticate |
| Claude Code | Uninstall plugin → reinstall |
| Codex | Uninstall → reinstall from marketplace |
| Other | MCP settings for `real` → Authenticate |

Then retry with `real-session` (`mcp_whoami` or `workspace_summary`).

## Network / `5xx` / timeout

Treat as connectivity — do **not** start OAuth recovery first. Retry once; if still failing, say the server may be down.

## Tool missing from `tools/list`

The project allowlist disabled that tool. Tell the user it is turned off for this project in the REAL MCP settings. Do **not** invent a substitute tool name.

## Rate limit / `429`

Do not hammer retries. Tell the user to wait briefly and try again.
Customer-facing line: `這次操作無法完成，請稍後再試。`
Do not invent credit-wallet explanations; if they ask about volume, use `mcp_usage_summary` (call counts only).
