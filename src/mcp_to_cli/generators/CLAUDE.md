# Generators Module / 생성기 모듈

Code generators that produce 5 output formats.

5가지 출력 형식을 생성하는 코드 제너레이터.

## Components / 컴포넌트
- `base.py` - Jinja2 Environment factory / Jinja2 Environment 팩토리
- `boto3_gen.py` - Python boto3 function generation / Python boto3 함수 생성
- `cli_gen.py` - Bash AWS CLI function generation / Bash AWS CLI 함수 생성
- `schema_gen.py` - OpenAPI JSON schema generation / OpenAPI JSON 스키마 생성
- `agentcore_gen.py` - AgentCore Gateway toolSpec generation / AgentCore Gateway toolSpec 생성
- `skill_gen.py` - Claude Code / Kiro-CLI skill markdown generation / Claude Code / Kiro-CLI skill 마크다운 생성

## Pattern / 패턴

All generators follow the `generate_function()` + `generate_module()` pattern.
Jinja2 templates are located in the `../templates/` directory.

모든 제너레이터는 `generate_function()` + `generate_module()` 패턴을 따름.
Jinja2 템플릿은 `../templates/` 디렉터리에 위치.
