# Templates Module

Jinja2 templates for code generation. Used by generators/ module.

## Files
- `boto3_func.py.j2` - Single boto3 function template
- `boto3_module.py.j2` - Complete boto3 module with imports
- `cli_command.sh.j2` - Single CLI function template
- `cli_module.sh.j2` - Complete CLI module with header
- `schema_tool.json.j2` - OpenAPI JSON schema per tool
- `skill_tool.md.j2` - Claude Code / Kiro-CLI skill markdown (YAML frontmatter + parameters table + code examples)

## Convention
- Template variables come from `ToolDefinition` and `MappingResult` dataclasses
- `tool.*` for tool metadata, `mapping.*` for boto3/CLI mapping data
