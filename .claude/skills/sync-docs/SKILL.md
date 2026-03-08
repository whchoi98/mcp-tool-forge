# Sync Docs Skill

Synchronize project documentation with current code state.

## Actions

### 1. CLAUDE.md Sync
- Update root CLAUDE.md to match current project state

### 2. Architecture Doc Sync
- Update docs/architecture.md to reflect current system structure

### 3. Module CLAUDE.md Audit
- Scan all directories under src/
- Create CLAUDE.md for modules missing one

### 4. ADR Audit
- Check recent commits (git log --oneline -20)
- Suggest new ADRs for undocumented architectural decisions

## Usage
Run with `/sync-docs` command
