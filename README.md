# AI Recruitment Copilot

A multi-agent system that screens resumes against a job description, scores
the match, checks against a database of past candidates, and routes the
outcome — shortlist, reject, or manual review — automatically.

Built to learn and demonstrate: structured LLM output, tool calling, MCP
(Model Context Protocol), LangGraph orchestration, and multi-agent design.

## Architecture
- **parse_resume** — extracts a structured candidate profile (Pydantic schema)
  from raw resume text using an LLM.
- **match** — a deterministic tool (no LLM) that scores candidate skills
  against required skills, called by the LLM via tool calling.
- **lookup_similar** — queries a candidate database through a real MCP
  server (SQLite-backed), connected as an MCP client from inside the graph.
- **route** — a LangGraph conditional edge that sends the workflow down a
  different path depending on the computed match score.

## Tech stack

- **LangChain** — structured output, tool calling
- **LangGraph** — stateful multi-node orchestration with conditional routing
- **MCP** — a custom server exposing a candidate database as tools, and a
  client consuming it from within the graph
- **Groq (Llama 3.3 70B)** — LLM backend
- **Pydantic** — schema validation for structured extraction

## Project structure
## Running it

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python scripts\seed_db.py
```

Add a `.env` file with:
Run the full workflow:
```bash
python -m tests.test_workflow
```

## What this demonstrates

- Structured prompting with schema-constrained LLM output
- Tool calling, where the LLM decides when to invoke a deterministic function
- A real MCP server/client round trip (not just an in-process tool call)
- LangGraph state management and conditional branching across multiple agents
- A Git/GitHub workflow of feature branches, PRs, and incremental merges