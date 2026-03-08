# Generators Module

5가지 출력 형식을 생성하는 코드 제너레이터.

## Components
- `base.py` - Jinja2 Environment 팩토리
- `boto3_gen.py` - Python boto3 함수 생성
- `cli_gen.py` - Bash AWS CLI 함수 생성
- `schema_gen.py` - OpenAPI JSON 스키마 생성
- `agentcore_gen.py` - AgentCore Gateway toolSpec 생성
- `skill_gen.py` - Claude Code skill 마크다운 생성

## Pattern
모든 제너레이터는 `generate_function()` + `generate_module()` 패턴을 따름.
Jinja2 템플릿은 `../templates/` 디렉터리에 위치.
