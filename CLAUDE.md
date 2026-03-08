# MCP Tool Forge
# MCP Tool Forge - MCP 도구 변환 도구

A Python CLI tool that extracts tool schemas from MCP servers and converts them to 5 formats: boto3/CLI/schema/agentcore/skill.

MCP 서버의 tool schema를 추출하여 boto3/CLI/schema/agentcore/skill 5가지 형식으로 변환하는 Python CLI 도구.

## Tech Stack / 기술 스택

- **Language**: Python 3.11
- **CLI**: Click 8.x + Rich (terminal UI)
- **MCP Client**: MCP SDK 1.26.0 (`stdio_client` + `ClientSession`)
- **AWS**: boto3 (API calls + Bedrock LLM inference / API 호출 + Bedrock LLM 추론)
- **Templates**: Jinja2 (code generation / 코드 생성)
- **Config**: PyYAML (registry, mappings / 레지스트리, 매핑)
- **Build**: Hatchling
- **Test**: pytest + pytest-asyncio

## Project Structure / 프로젝트 구조

```
mcp-tool-forge/
├── src/mcp_to_cli/
│   ├── cli.py              # Click CLI entry point / Click CLI 진입점
│   ├── pipeline.py          # 3-phase orchestrator (extract -> map -> generate) / 3단계 오케스트레이터
│   ├── connector.py         # MCP SDK stdio_client connection / MCP SDK stdio_client 연결
│   ├── parser.py            # MCP tool schema -> ToolDefinition / MCP 도구 스키마 변환
│   ├── registry.py          # Server registry loader / 서버 레지스트리 로더
│   ├── registry.yaml        # 63 servers (package names, runtime, category) / 63개 서버 설정
│   ├── mapping_loader.py    # Static YAML mapping loader / 정적 YAML 매핑 로더
│   ├── llm_mapper.py        # Bedrock Claude LLM mapping (Phase 3) / Bedrock Claude LLM 매핑
│   ├── cache.py             # Schema cache (~/.mcp-tool-forge/cache/) / 스키마 캐시
│   ├── validator.py         # Generated code syntax validator/fixer / 생성 코드 검증/수정
│   ├── skill_registrar.py   # Claude Code skill registration / Claude Code 스킬 등록
│   ├── models.py            # Dataclasses (ToolParam, ToolDefinition, etc.) / 데이터 클래스
│   ├── generators/          # 5 output generators / 5가지 출력 생성기
│   │   ├── boto3_gen.py     # Python boto3 functions / Python boto3 함수 생성
│   │   ├── cli_gen.py       # Bash AWS CLI functions / Bash AWS CLI 함수 생성
│   │   ├── schema_gen.py    # OpenAPI JSON schema / OpenAPI JSON 스키마 생성
│   │   ├── agentcore_gen.py # AgentCore Gateway toolSpec / AgentCore Gateway toolSpec 생성
│   │   └── skill_gen.py     # Claude Code skill markdown / Claude Code 스킬 마크다운 생성
│   ├── mappings/            # Static YAML mappings (iam.yaml, dynamodb.yaml) / 정적 YAML 매핑
│   └── templates/           # Jinja2 templates (6 .j2 files) / Jinja2 템플릿 (6개)
├── tests/                   # 38 pytest tests / 38개 pytest 테스트
├── docs/plans/              # Design and implementation plans / 설계 및 구현 계획
└── output/                  # Generated code (gitignored) / 생성된 코드 (gitignore)
```

## Key Commands / 주요 명령어

```bash
# Install / 설치
pip3.11 install -e ".[dev]"

# Test / 테스트
python3.11 -m pytest tests/ -v

# CLI usage / CLI 사용법
python3.11 -m mcp_to_cli.cli list-servers
python3.11 -m mcp_to_cli.cli list-servers --category "Data & Analytics"
python3.11 -m mcp_to_cli.cli list-tools --server aws-iam-mcp-server
python3.11 -m mcp_to_cli.cli convert --server aws-iam-mcp-server --output all
python3.11 -m mcp_to_cli.cli convert --server <name> --llm-assist
python3.11 -m mcp_to_cli.cli register --server <name> -d output
```

## Conventions / 규칙

### Pipeline Phases / 파이프라인 단계
1. **Extract / 추출**: MCP SDK `tools/list` (cached in ~/.mcp-tool-forge/cache/)
2. **Map - Static / 정적 매핑**: `mappings/*.yaml` for known boto3/CLI mappings
3. **Map - LLM / LLM 매핑**: Bedrock Haiku (`us.anthropic.claude-3-5-haiku-20241022-v1:0`)
4. **Generate / 생성**: Jinja2 templates -> 5 output formats

### Registry / 레지스트리
- Package names from PyPI (differ from server names) / PyPI 패키지명 (서버명과 다름)
- ECS uses split-package: `"--from awslabs-ecs-mcp-server ecs-mcp-server"` / ECS는 분리 패키지 사용
- Some servers need `AWS_REGION` env var / 일부 서버는 `AWS_REGION` 환경변수 필요

### Testing / 테스트
- All tests use mocks (no real AWS/MCP calls) / 모든 테스트는 모의 객체 사용 (실제 AWS/MCP 호출 없음)
- `pytest-asyncio` for async tests / 비동기 테스트용 `pytest-asyncio`

## Auto-Sync Rules / 자동 동기화 규칙

When exiting Plan Mode after making changes:

Plan Mode 종료 시 변경사항이 있으면:

1. Update this CLAUDE.md if architecture or commands changed / 아키텍처 또는 명령이 변경되면 이 CLAUDE.md 업데이트
2. Update `docs/architecture.md` if components changed / 컴포넌트가 변경되면 `docs/architecture.md` 업데이트
