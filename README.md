# mcp-to-cli
# MCP-to-CLI 변환 도구

A Python CLI tool that extracts tools from MCP (Model Context Protocol) servers and converts them into **5 formats**: boto3 functions, AWS CLI commands, OpenAPI schemas, AgentCore Gateway configs, and Claude Code Skills.

MCP (Model Context Protocol) 서버의 도구를 추출하여 **boto3 함수, AWS CLI 명령어, OpenAPI 스키마, AgentCore Gateway 설정, Claude Code Skill** 5가지 형식으로 변환하는 Python CLI 도구.

## Why? / 왜 필요한가?

The MCP protocol consumes LLM tokens for both tool definitions (JSON Schema) and request/response cycles. Using hundreds of tools across 66+ AWS MCP servers causes token costs to skyrocket.

MCP 프로토콜은 도구 정의(JSON Schema)와 요청/응답이 모두 LLM 토큰으로 소모됩니다. 66개 이상의 AWS MCP 서버에서 수백 개 도구를 사용하면 토큰 비용이 급증합니다.

**mcp-to-cli** extracts MCP tools once and converts them to code that can be used directly in various runtimes:

**mcp-to-cli**는 MCP 도구를 한 번 추출하여 다양한 런타임에서 직접 사용할 수 있는 코드로 변환합니다:

| Output Format / 출력 형식 | Purpose / 용도 |
|----------|------|
| **boto3 (.py)** | Direct invocation from AgentCore Gateway Lambda, Interpreter / AgentCore Gateway Lambda, Interpreter에서 직접 호출 |
| **AWS CLI (.sh)** | Shell-based agents, automation scripts / Shell 기반 에이전트, 자동화 스크립트 |
| **Schema (.json)** | OpenAPI-compatible tool definitions / OpenAPI 호환 도구 정의 |
| **AgentCore (.json)** | Amazon Bedrock AgentCore Gateway toolSpec |
| **Skill (.md)** | Claude Code / Kiro-CLI skill registration / Claude Code / Kiro-CLI 스킬 등록 |

## Quick Start / 빠른 시작

```bash
# Install / 설치
pip install -e ".[dev]"

# List servers / 서버 목록 조회
mcp-to-cli list-servers
mcp-to-cli list-servers --category "Data & Analytics"

# Check tools for a specific server (connects to real MCP server)
# 특정 서버의 도구 확인 (실제 MCP 서버 연결)
mcp-to-cli list-tools --server aws-iam-mcp-server

# Convert to all formats / 모든 형식으로 변환
mcp-to-cli convert --server aws-iam-mcp-server --output all

# Enable LLM mapping (infer unmapped tools via Bedrock Claude)
# LLM 매핑 활성화 (정적 매핑 없는 도구를 Bedrock Claude로 추론)
mcp-to-cli convert --server amazon-cloudwatch-mcp-server --output all --llm-assist

# Register skills to Claude Code / Claude Code에 스킬 등록
mcp-to-cli register --server aws-iam-mcp-server -d output
```

## Architecture / 아키텍처

```
┌──────────────────────────────────────────────────┐
│                  mcp-to-cli                       │
├──────────────────────────────────────────────────┤
│                                                   │
│  Phase 1: Schema Extraction / 스키마 추출          │
│  ┌───────────┐  tools/list  ┌──────────────┐    │
│  │ MCP Server ├────────────►│ Schema Cache  │    │
│  │ (stdio)    │  MCP SDK    │ (~/.mcp-to-cli)│   │
│  └───────────┘              └──────┬───────┘    │
│                                     │            │
│  Phase 2: Static Mapping / 정적 매핑  │            │
│  ┌──────────────┐                   │            │
│  │ YAML Mappings │◄─────────────────┘            │
│  │ (iam, dynamo) │                               │
│  └──────┬───────┘                               │
│         │ unmapped                               │
│  Phase 3: LLM Inference / LLM 추론               │
│  ┌──────▼───────┐                               │
│  │ Bedrock Claude│ tool schema → boto3 mapping   │
│  │ (Haiku 3.5)   │                               │
│  └──────┬───────┘                               │
│         │                                        │
│  Code Generation / 코드 생성                       │
│  ┌──────▼───────┐                               │
│  │  Generators   │ boto3 / cli / schema /        │
│  │  (Jinja2)     │ agentcore / skill             │
│  └──────────────┘                               │
└──────────────────────────────────────────────────┘
```

### 3-Phase Hybrid Pipeline / 3단계 하이브리드 파이프라인

1. **Phase 1 (Extract / 추출)** — Connects to the server via MCP SDK's `stdio_client`, extracts tool schemas with `tools/list`. Results are cached in `~/.mcp-to-cli/cache/`.
   MCP SDK의 `stdio_client`로 서버에 연결, `tools/list`로 도구 스키마 추출. 결과는 `~/.mcp-to-cli/cache/`에 캐시.

2. **Phase 2 (Static Map / 정적 매핑)** — Looks up known boto3/CLI mappings from `mappings/*.yaml`. Currently IAM 29 + DynamoDB 6 = 35 mappings.
   `mappings/*.yaml` 파일에서 알려진 도구의 boto3/CLI 매핑 조회. 현재 IAM 29개 + DynamoDB 6개 = 35개 매핑.

3. **Phase 3 (LLM Map / LLM 매핑)** — Sends unmapped tools to Amazon Bedrock Claude 3.5 Haiku for automatic boto3/CLI code inference. Activated with `--llm-assist` flag.
   매핑되지 않은 도구를 Amazon Bedrock Claude 3.5 Haiku에 전송, boto3/CLI 코드 자동 추론. `--llm-assist` 플래그로 활성화.

## Supported Servers / 지원 서버

Supports 63 AWS MCP servers across 9 categories:

63개 AWS MCP 서버를 지원합니다 (9개 카테고리):

| Category / 카테고리 | Count / 서버 수 | Representative Servers / 대표 서버 |
|----------|---------|----------|
| Data & Analytics | 18 | DynamoDB, Aurora, Redshift, ElastiCache, Neptune |
| AI & Machine Learning | 10 | Bedrock, SageMaker, Kendra, Nova Canvas |
| Infrastructure & Deployment | 9 | EKS, ECS, CloudFormation, Terraform, Serverless |
| Cost & Operations | 8 | CloudWatch, CloudTrail, Cost Explorer, Billing |
| Developer Tools & Support | 7 | IAM, MSK, Diagram, Code Doc Gen |
| Integration & Messaging | 5 | SNS/SQS, MQ, Step Functions, Location |
| Healthcare & Lifesciences | 3 | HealthOmics, HealthImaging, HealthLake |
| Documentation | 2 | AWS Documentation, Knowledge |
| Essential Setup | 1 | AWS MCP (unified proxy) |

```bash
# View full list / 전체 목록 확인
mcp-to-cli list-servers

# Filter by category / 카테고리별 필터
mcp-to-cli list-servers --category "AI & Machine Learning"
```

## Output Examples / 출력 예시

### boto3 (Python)

```python
# output/aws-iam-mcp-server/boto3/tools.py
def list_users(ctx: str, path_prefix: str | None = None, max_items: int | None = None, **kwargs) -> dict:
    """List IAM users in the account."""
    client = boto3.client('iam')
    params = {}
    if path_prefix is not None:
        params['PathPrefix'] = path_prefix
    if max_items is not None:
        params['MaxItems'] = max_items
    params.update(kwargs)
    return client.list_users(**params)
```

### AWS CLI (Bash)

```bash
# output/aws-iam-mcp-server/cli/tools.sh
list_users() {
    aws iam list-users \
        --path-prefix "$PATH_PREFIX" \
        --max-items "$MAX_ITEMS"
}
```

### AgentCore Gateway (JSON)

```json
{
  "tools": [{
    "toolSpec": {
      "name": "list_users",
      "description": "List IAM users in the account.",
      "inputSchema": {
        "json": {
          "type": "object",
          "properties": {
            "path_prefix": {"type": "string", "description": "Path prefix to filter users"},
            "max_items": {"type": "integer", "description": "Maximum number of users to return"}
          },
          "required": []
        }
      }
    }
  }]
}
```

### Claude Code Skill (Markdown)

```markdown
---
name: list-users
description: List IAM users in the account.
---
# List Users
## Parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path_prefix` | string | No | Path prefix to filter users |
## boto3
boto3.client('iam').list_users(PathPrefix=path_prefix)
```

## Use Cases / 사용 사례

### AgentCore Gateway Lambda

```python
# Use generated boto3 functions directly in Lambda handler
# Lambda handler에서 생성된 boto3 함수 직접 사용
from output.aws_iam_mcp_server.boto3.tools import list_users, create_role

def handler(event, context):
    tool_name = event['tool_name']
    params = event['parameters']

    if tool_name == 'list_users':
        return list_users(**params)
    elif tool_name == 'create_role':
        return create_role(**params)
```

### Claude Code / Kiro-CLI

```bash
# Register skills then use directly in Claude Code
# 스킬 등록 후 Claude Code에서 바로 사용
mcp-to-cli register --all-servers -d output

# In Claude Code / Claude Code에서:
# /list-users → IAM user listing guide / IAM 사용자 조회 방법 안내
# /create-role → IAM role creation guide / IAM 역할 생성 방법 안내
```

### Automation Scripts / 자동화 스크립트

```bash
# Source generated CLI functions and use them
# 생성된 CLI 함수를 소싱하여 사용
source output/aws-iam-mcp-server/cli/tools.sh
list_users
create_role "my-role" '{"Version":"2012-10-17","Statement":[...]}'
```

## Project Structure / 프로젝트 구조

```
mcp-to-cli/
├── src/mcp_to_cli/
│   ├── cli.py              # Click CLI (list-servers, list-tools, convert, register)
│   ├── pipeline.py          # 3-phase orchestrator / 3단계 오케스트레이터
│   ├── connector.py         # MCP SDK stdio_client
│   ├── parser.py            # Tool schema parser / 도구 스키마 파서
│   ├── registry.py          # Server registry loader / 서버 레지스트리 로더
│   ├── registry.yaml        # 63 server configs / 63개 서버 설정
│   ├── mapping_loader.py    # Static YAML mapping loader / 정적 YAML 매핑 로더
│   ├── llm_mapper.py        # Bedrock Claude LLM mapper / Bedrock Claude LLM 매퍼
│   ├── cache.py             # Schema cache / 스키마 캐시
│   ├── validator.py         # Generated code validator/fixer / 생성 코드 검증/수정
│   ├── skill_registrar.py   # Claude Code skill registration / Claude Code 스킬 등록
│   ├── models.py            # Data models / 데이터 모델
│   ├── generators/          # 5 output generators / 5가지 출력 생성기
│   ├── mappings/            # Static YAML mappings (IAM, DynamoDB) / 정적 YAML 매핑
│   └── templates/           # 6 Jinja2 templates / 6개 Jinja2 템플릿
├── tests/                   # 38 pytest tests / 38개 pytest 테스트
├── docs/
│   ├── architecture.md
│   └── plans/               # Design documents / 설계 문서
└── output/                  # Generated code (gitignored) / 생성된 코드 (gitignore)
```

## Development / 개발

```bash
# Install / 설치
pip install -e ".[dev]"

# Test / 테스트
python -m pytest tests/ -v

# Lint (optional) / 린트 (선택)
python -m py_compile src/mcp_to_cli/cli.py
```

## Requirements / 요구사항

- Python >= 3.11
- AWS credentials (IAM role or ~/.aws/config) / AWS 자격 증명 (IAM 역할 또는 ~/.aws/config)
- uvx (for running Python MCP servers) / uvx (Python MCP 서버 실행)
- npx (for running Node.js MCP servers, optional) / npx (Node.js MCP 서버 실행, 선택)
- Amazon Bedrock access (when using LLM mapping, us-east-1) / Amazon Bedrock 접근 (LLM 매핑 사용 시, us-east-1)

## License / 라이선스

MIT
