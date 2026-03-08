# Architecture / 아키텍처

## System Overview / 시스템 개요

MCP Tool Forge is a Python CLI tool that connects to AWS MCP servers, extracts tool schemas, and converts them to multiple output formats for use in different agent runtimes.

MCP Tool Forge는 AWS MCP 서버에 연결하여 도구 스키마를 추출하고, 다양한 에이전트 런타임에서 사용할 수 있도록 여러 출력 형식으로 변환하는 Python CLI 도구입니다.

```
MCP Server (stdio)  -->  Connector  -->  Parser  -->  Pipeline  -->  Generators
     |                                      |            |              |
     v                                      v            v              v
 tools/list                           ToolDefinition   Mapping     5 formats / 5가지 형식:
 (JSON-RPC)                           (dataclass)      (static     boto3, cli,
                                                       + LLM)      schema, agentcore,
                                                                   skill
```

## Components / 컴포넌트

### CLI Layer / CLI 계층 (`cli.py`)
- Click-based CLI with commands: `list-servers`, `list-tools`, `convert`, `register`
- Rich tables for terminal output
- Click 기반 CLI 명령어: `list-servers`, `list-tools`, `convert`, `register`
- Rich 테이블 터미널 출력

### Pipeline / 파이프라인 (`pipeline.py`)
- Orchestrates 3-phase process: Extract -> Map -> Generate
- Manages cache for extracted schemas
- 3단계 프로세스 오케스트레이션: 추출 -> 매핑 -> 생성
- 추출된 스키마 캐시 관리

### Connector / 커넥터 (`connector.py`)
- MCP SDK `stdio_client` + `ClientSession`
- Supports uvx and npx runtimes / uvx, npx 런타임 지원
- 60s timeout with graceful cleanup / 60초 타임아웃 및 정상 종료

### Registry / 레지스트리 (`registry.py` + `registry.yaml`)
- 63 AWS MCP server configurations / 63개 AWS MCP 서버 설정
- Package names, runtimes, categories / 패키지명, 런타임, 카테고리
- Verified against PyPI / PyPI 검증 완료

### Mapping / 매핑 (`mapping_loader.py` + `llm_mapper.py`)
- Static: YAML files for known services (IAM 29, DynamoDB 6) / 정적: 알려진 서비스 YAML 파일 (IAM 29, DynamoDB 6)
- LLM: Bedrock Claude 3.5 Haiku for unmapped tools / LLM: 매핑 없는 도구용 Bedrock Claude 3.5 Haiku

### Generators / 생성기 (`generators/`)
- boto3: Python functions with type hints / 타입 힌트 포함 Python 함수
- cli: Bash shell functions / Bash 셸 함수
- schema: OpenAPI-compatible JSON / OpenAPI 호환 JSON
- agentcore: AgentCore Gateway toolSpec format / AgentCore Gateway toolSpec 형식
- skill: Claude Code skill markdown / Claude Code 스킬 마크다운

### Validator / 검증기 (`validator.py`)
- Post-generation syntax validation / 생성 후 구문 검증
- Auto-fix LLM hallucination patterns / LLM 할루시네이션 패턴 자동 수정

## Data Flow / 데이터 흐름

1. User runs `mcp-tool-forge convert --server <name>` / 사용자가 `mcp-tool-forge convert --server <name>` 실행
2. Pipeline checks cache -> connects to MCP server -> extracts tools / 파이프라인이 캐시 확인 -> MCP 서버 연결 -> 도구 추출
3. Parser converts raw schemas to `ToolDefinition` objects / 파서가 원시 스키마를 `ToolDefinition` 객체로 변환
4. Mapping loader checks static YAML, then optionally LLM mapper / 매핑 로더가 정적 YAML 확인 후 선택적으로 LLM 매퍼 사용
5. Generators produce output files in `output/<server>/<format>/` / 생성기가 `output/<server>/<format>/`에 출력 파일 생성

## Infrastructure / 인프라

- Python 3.11 package (hatchling build)
- Schema cache / 스키마 캐시: `~/.mcp-tool-forge/cache/`
- Plugin output / 플러그인 출력: `~/.claude/plugins/mcp-tool-forge-tools/`
- LLM: Bedrock `us.anthropic.claude-3-5-haiku` in us-east-1
