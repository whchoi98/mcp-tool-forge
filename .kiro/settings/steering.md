# Steering Rules for mcp-tool-forge

## Allowed Operations
- Run pytest: `python3.11 -m pytest tests/ -v`
- Run CLI: `python3.11 -m mcp_to_cli.cli <command>`
- Git read commands: `git status`, `git log`, `git diff`

## Code Quality
- After writing or editing files under `src/`, check if module documentation exists
- If `docs/decisions/` has no ADR files, suggest recording architectural decisions
- Run `python3.11 -m pytest tests/ -v` after code changes to verify tests pass

## Documentation Sync
- Update `.kiro/AGENT.md` if architecture or commands change
- Update `docs/architecture.md` if components change
- Ensure all modules under `src/` have documentation

## Conventions
- Python 3.11, type hints preferred
- All tests use mocks (no real AWS/MCP calls)
- Bilingual comments (Korean/English) in source files
- Use Click for CLI, Jinja2 for templates, PyYAML for config
