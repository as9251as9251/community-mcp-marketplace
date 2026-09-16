---
name: infinity-labs-knowledge
description: Search INFINITY LABS shop knowledge base FAQ / price / policy via knowledge_search.
---

# Skill: infinity-labs-knowledge

**Prerequisite:** `infinity-labs-universal-workflow`.

## MCP tools

- `knowledge_search` — `q` keyword, `limit` 1–10 (default 5). Read-only.

## Workflow

1. Call with the user's question as `q`.
2. Summarize answers in plain language; cite snippets when helpful.
3. If nothing useful returns, say the knowledge base may not cover it — do not invent shop facts.
