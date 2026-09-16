# Timezone policy (REAL) — instant MCP inputs

Use when the user gives temporal language and you will put a **specific instant** into an MCP argument.

Default wall-clock timezone when the user omits one: **Asia/Taipei (UTC+8)** — also returned by `mcp_whoami.timezone`.

## Conversion rules

1. Wall-clock without timezone → interpret as Asia/Taipei and encode with `+08:00`.
2. User names a timezone / supplies `Z` / an offset → **honor it**; do not rewrite to Taipei.
3. Relative calendar language (“明天”、“下週五”) → resolve on the **effective** timezone calendar (named offset or Taipei default).
4. User gives **date only** but the tool needs an instant → ask for the clock boundary; do **not** invent midnight.
5. Do not default an omitted customer timezone to `Z`.

## Do not force this policy on

| Class | Examples |
|---|---|
| Relative duration | “等 30 分鐘”、timeout 長度 |
| Relative day windows | `messages_search.days`（往回 N 天；伺服器以 UTC `since` 截斷） |
| Returned timestamps | tool 回傳的 `created_at`／`since`（原樣引用即可） |
| Opaque tokens | pagination／preview_token |

## Reads vs writes

- **Reads:** when you encode user wall-clock into a plan, disclose the effective timezone in the same turn.
- **Writes** (e.g. `reservation_reschedule.starts_at`): show intent + timezone + encoded ISO in the write-lifecycle confirmation.

## Our tools note

- `messages_search` uses relative `days` (1–30), not `startAt`/`endAt`. Translate “上週／本月” into an explicit `days` (or say the tool cannot express arbitrary calendar bounds) and report the returned `since`.
- `mcp_usage_summary.days` is the same relative-window pattern.
