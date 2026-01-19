# tracewise — Project Context

## Project Goal
Tracewise is an open-source CLI tool that analyzes MySQL slow query logs and outputs ranked performance insights. It targets backend engineers and SREs who need actionable rankings to decide what to optimize first.

The tool is local-first and runs offline, producing reports without sending data to external services.

## Current Phase
Phase 0: Foundation. No MVP features are implemented yet.

## Technical Decisions
- Python 3.10+
- CLI-first design
- Packaged via pyproject.toml using Hatchling
- Minimal dependencies
- No database connections
- No cloud services required

## Constraints
- README.md already exists and MUST NOT be overwritten unless explicitly instructed.
- One GitHub issue = one unit of work.
- Codex should only implement the issue it is given.
- No AI/LLM features until Phase 5.
- No over-engineering or speculative abstractions.

## Repository Workflow
- Issues define scope and acceptance criteria.
- One issue → one Codex prompt → one commit.
- Changes must be minimal and scoped.
- Prefer clear, readable code over clever abstractions.

## What NOT to do
- Do not redesign architecture unless an issue explicitly says so.
- Do not add features outside the current issue.
- Do not modify files unrelated to the issue.
