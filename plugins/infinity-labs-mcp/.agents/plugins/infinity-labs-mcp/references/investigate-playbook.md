# Investigate playbook (INFINITY LABS)

Read-only. Tools: `messages_search`, optional `conversation_get`, optional `knowledge_search`.

## Tool choice

| Ask | Use | Do not |
|---|---|---|
| 誰最近找過／收件匣 | `inbox_list`（`infinity-labs-inbox`） | treat as full DB census |
| 期間／關鍵字證據 | `messages_search` | use `inbox_list` for sentiment % |
| 單線近期上下文 | `conversation_get` | treat as a year-long corpus |

## Sample guardrails

1. Prefer ≤ **5** `messages_search` calls per user ask before summarizing.
2. Always pass real `q`. Our API **requires** a keyword — do not invent empty-corpus search.
3. Cap: `days` ≤ 30 (default 14). Longer asks → split windows and say so; do not claim full-project coverage.
4. Coverage label in the answer: report tool `days` / `since` / `count`. Use wording like「樣本／部分」when `count` hit the `limit`.
5. Cite `message_id` or contact display name + short quote from the payload. **Never fabricate** complaints or guest quotes.
6. Non-text / empty bodies: do not treat media-only rows as satisfaction signals.
7. Do not blind-retry the same failing query. On auth errors → `infinity-labs-session`.

## FAQ thin path (from search hits)

1. Search with concrete `q` themes the user cares about.
2. Cluster recurring questions from **customer** text in the hits.
3. Optionally `knowledge_search` for duplicates already in the knowledge base.
4. Draft Q→A as **建議／綜合**; mark “樣本內無客服回覆” if you cannot verify a staff answer via `conversation_get`.
5. Do **not** call a write/upsert tool unless it appears in `tools/list` and the user confirmed write-lifecycle.

## Lenses (same tools, separate passes)

- Complaint themes → keyword pass, then theme → evidence → improvement suggestion.
- Opportunity / recurring ask → **separate** keyword pass; do not reuse one broad pull for both complaint + opportunity.
- CS quality → only if payloads clearly distinguish staff vs guest; otherwise say attribution is unavailable.
