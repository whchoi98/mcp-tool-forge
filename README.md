# mcp-tool-forge
# MCP Tool Forge

A Python CLI tool that extracts tools from MCP (Model Context Protocol) servers and converts them into **5 formats**: boto3 functions, AWS CLI commands, OpenAPI schemas, AgentCore Gateway configs, and Claude Code Skills. Also includes **7 ready-to-use AWS Skills** for Claude Code.

MCP (Model Context Protocol) 서버의 도구를 추출하여 **boto3 함수, AWS CLI 명령어, OpenAPI 스키마, AgentCore Gateway 설정, Claude Code Skill** 5가지 형식으로 변환하는 Python CLI 도구. **7개 AWS Claude Code Skills**을 포함합니다.

## Why? / 왜 필요한가?

The MCP protocol consumes LLM tokens for both tool definitions (JSON Schema) and request/response cycles. Using hundreds of tools across 66+ AWS MCP servers causes token costs to skyrocket.

MCP 프로토콜은 도구 정의(JSON Schema)와 요청/응답이 모두 LLM 토큰으로 소모됩니다. 66개 이상의 AWS MCP 서버에서 수백 개 도구를 사용하면 토큰 비용이 급증합니다.

**mcp-tool-forge** extracts MCP tools once and converts them to code that can be used directly in various runtimes — **zero tokens, zero latency**.

**mcp-tool-forge**는 MCP 도구를 한 번 추출하여 다양한 런타임에서 직접 사용할 수 있는 코드로 변환합니다 — **토큰 0, 지연 0**.

| Output Format / 출력 형식 | Purpose / 용도 |
|----------|------|
| **boto3 (.py)** | Direct invocation from AgentCore Gateway Lambda, Interpreter / AgentCore Gateway Lambda, Interpreter에서 직접 호출 |
| **AWS CLI (.sh)** | Shell-based agents, automation scripts / Shell 기반 에이전트, 자동화 스크립트 |
| **Schema (.json)** | OpenAPI-compatible tool definitions / OpenAPI 호환 도구 정의 |
| **AgentCore (.json)** | Amazon Bedrock AgentCore Gateway toolSpec |
| **Skill (.md)** | Claude Code / Kiro-CLI skill registration / Claude Code / Kiro-CLI 스킬 등록 |

## AWS Skills for Claude Code / Claude Code용 AWS Skills

**Use AWS services directly from Claude Code without MCP servers.** Copy `.claude/skills/` to any project.

**MCP 서버 없이 Claude Code에서 직접 AWS 서비스를 사용합니다.** `.claude/skills/`를 아무 프로젝트에 복사하세요.

| Skill | Trigger / 트리거 | Operations / 주요 작업 |
|-------|---------|----------|
| **aws-iam** | "IAM 사용자/역할/정책" | list_users, create_role, attach_policy, simulate_policy |
| **aws-cloudwatch** | "로그/메트릭/알람/감사" | Logs Insights, get_metric_data, describe_alarms, CloudTrail |
| **aws-cost** | "비용/청구/가격" | get_cost_and_usage, cost_forecast, pricing lookup |
| **aws-infra** | "리소스/스택/컨테이너" | Cloud Control API, CloudFormation, EKS, ECS, Lambda |
| **aws-messaging** | "큐/토픽/메시지/워크플로" | SNS publish, SQS send/receive, MQ, Step Functions |
| **aws-data** | "DB/캐시/쿼리" | DynamoDB, Aurora, Redshift, ElastiCache, Neptune |
| **aws-security** | "계정/자격증명/보안감사" | get_caller_identity, credential audit, MFA check |

### Install Skills to Your Project / 프로젝트에 Skills 설치

```bash
# Copy all AWS skills to your project / 프로젝트에 모든 AWS 스킬 복사
cp -r .claude/skills/aws-* /path/to/your-project/.claude/skills/

# Or install specific skills / 또는 특정 스킬만 설치
cp -r .claude/skills/aws-iam /path/to/your-project/.claude/skills/
cp -r .claude/skills/aws-cost /path/to/your-project/.claude/skills/
```

### Skills Test Results / Skills 테스트 결과

Tested on a real AWS account (Seoul region, IAM role auth):

실제 AWS 계정에서 테스트 완료 (서울 리전, IAM 역할 인증):

| # | Skill | Test / 테스트 | Result / 결과 |
|---|-------|------|--------|
| 1 | aws-security | `sts get-caller-identity` | OK |
| 2 | aws-iam | `list-users` | OK (2 users) |
| 3 | aws-iam | `list-roles` | OK (13 roles) |
| 4 | aws-cloudwatch | `describe-log-groups` | OK |
| 5 | aws-cloudwatch | `describe-alarms` | OK |
| 6 | aws-infra | Cloud Control EC2 | OK |
| 7 | aws-infra | Cloud Control S3 | OK (1 bucket) |
| 8 | aws-infra | CloudFormation stacks | OK |
| 9 | aws-cost | `get-cost-and-usage` | OK ($1,093) |
| 10 | aws-cost | Cost by service (top 5) | OK |
| 11 | aws-security | MFA check (boto3) | OK (2 NO MFA) |
| 12 | aws-security | Access key age (boto3) | OK (23 days) |
| 13 | aws-security | Account summary (boto3) | OK (Root MFA: NO) |
| 14 | aws-messaging | SNS topics | OK |
| 15 | aws-messaging | SQS queues | OK |
| 16 | aws-data | DynamoDB tables | OK |
| 17 | aws-infra | Lambda functions | OK |

**17/17 passed** — All skills work with standard AWS credentials.

**17/17 통과** — 모든 스킬이 표준 AWS 자격 증명으로 동작합니다.

## Quick Start / 빠른 시작

```bash
# Install / 설치
pip install -e ".[dev]"

# List servers / 서버 목록 조회
mcp-tool-forge list-servers
mcp-tool-forge list-servers --category "Data & Analytics"

# Check tools (connects to real MCP server) / 도구 확인 (실제 MCP 서버 연결)
mcp-tool-forge list-tools --server aws-iam-mcp-server

# Convert to all formats / 모든 형식으로 변환
mcp-tool-forge convert --server aws-iam-mcp-server --output all

# LLM mapping (Bedrock Claude) / LLM 매핑
mcp-tool-forge convert --server amazon-cloudwatch-mcp-server --output all --llm-assist

# Register skills to Claude Code / Claude Code에 스킬 등록
mcp-tool-forge register --server aws-iam-mcp-server -d output
```

## Architecture / 아키텍처

```
┌──────────────────────────────────────────────────────┐
│                    mcp-tool-forge                     │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Phase 1: Schema Extraction / 스키마 추출             │
│  ┌───────────┐  tools/list  ┌────────────────┐      │
│  │ MCP Server ├────────────►│ Schema Cache    │      │
│  │ (stdio)    │  MCP SDK    │(~/.mcp-tool-forge)│    │
│  └───────────┘              └───────┬────────┘      │
│                                      │               │
│  Phase 2: Static Mapping / 정적 매핑   │               │
│  ┌──────────────┐                    │               │
│  │ YAML Mappings │◄──────────────────┘               │
│  │ (iam, dynamo) │                                   │
│  └──────┬───────┘                                   │
│         │ unmapped                                   │
│  Phase 3: LLM Inference / LLM 추론                   │
│  ┌──────▼───────┐                                   │
│  │ Bedrock Claude│  tool schema → boto3 mapping      │
│  │ (Opus 4.6)    │                                   │
│  └──────┬───────┘                                   │
│         │                                            │
│  Code Generation / 코드 생성                          │
│  ┌──────▼───────┐                                   │
│  │  Generators   │  boto3 / cli / schema /           │
│  │  (Jinja2)     │  agentcore / skill                │
│  └──────────────┘                                   │
└──────────────────────────────────────────────────────┘
```

### 3-Phase Hybrid Pipeline / 3단계 하이브리드 파이프라인

1. **Phase 1 (Extract / 추출)** — MCP SDK `stdio_client` connects to server, `tools/list` extracts schemas. Cached in `~/.mcp-tool-forge/cache/`.
   MCP SDK `stdio_client`로 서버 연결, `tools/list`로 스키마 추출. `~/.mcp-tool-forge/cache/`에 캐시.

2. **Phase 2 (Static Map / 정적 매핑)** — Known mappings from `mappings/*.yaml` (IAM 29 + DynamoDB 6 = 35 tools).
   `mappings/*.yaml`에서 알려진 매핑 조회 (IAM 29 + DynamoDB 6 = 35개).

3. **Phase 3 (LLM Map / LLM 매핑)** — Unmapped tools sent to Bedrock Claude Opus 4.6 for inference. `--llm-assist` flag.
   미매핑 도구를 Bedrock Claude Opus 4.6에 전송. `--llm-assist` 플래그.

## Extraction Results / 추출 결과

| Metric / 지표 | Value / 값 |
|------|------|
| Servers connected / 연결 성공 | **51 / 63** (81%) |
| Tools extracted / 도구 추출 | **755** |
| boto3 functions / boto3 함수 | **480** |
| Skills generated / 생성된 스킬 | **755** |
| Syntax pass rate / 구문 통과율 | **91.4%** (after auto-fix) |

## Supported Servers / 지원 서버

| Category / 카테고리 | Count / 수 | Servers / 서버 |
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

## Use Cases / 사용 사례

### AgentCore Gateway Lambda

```python
from output.aws_iam_mcp_server.boto3.tools import list_users, create_role

def handler(event, context):
    tool_name = event['tool_name']
    params = event['parameters']
    if tool_name == 'list_users':
        return list_users(**params)
```

### Claude Code Skills (No MCP) / MCP 없이 사용

```bash
cp -r .claude/skills/aws-* ~/my-project/.claude/skills/
# "IAM 사용자 목록 보여줘" → aws-iam skill activates
# "이번 달 비용은?" → aws-cost skill activates
# "보안 감사 실행" → aws-security skill activates
```

### Automation Scripts / 자동화 스크립트

```bash
source output/aws-iam-mcp-server/cli/tools.sh
list_users
```

## Project Structure / 프로젝트 구조

```
mcp-tool-forge/
├── .claude/skills/             # 7 AWS Skills (portable)
│   ├── aws-iam/                # IAM users, roles, policies
│   ├── aws-cloudwatch/         # Logs, metrics, alarms, CloudTrail
│   ├── aws-cost/               # Cost Explorer, billing, pricing
│   ├── aws-infra/              # CloudFormation, EKS, ECS, Lambda
│   ├── aws-messaging/          # SNS, SQS, MQ, Step Functions
│   ├── aws-data/               # DynamoDB, Aurora, Redshift, Neptune
│   └── aws-security/           # Account info, security audit
├── src/mcp_to_cli/
│   ├── cli.py                  # Click CLI entry point
│   ├── pipeline.py             # 3-phase orchestrator
│   ├── connector.py            # MCP SDK stdio_client
│   ├── registry.yaml           # 63 server configs
│   ├── llm_mapper.py           # Bedrock Claude Opus 4.6
│   ├── validator.py            # Generated code fixer
│   ├── generators/             # 5 output generators
│   ├── mappings/               # Static YAML (IAM, DynamoDB)
│   └── templates/              # 6 Jinja2 templates
├── tests/                      # 38 pytest tests
└── docs/                       # Architecture & plans
```

## Development / 개발

```bash
pip install -e ".[dev]"      # Install / 설치
python -m pytest tests/ -v   # Test / 테스트 (38 tests)
```

## Requirements / 요구사항

- Python >= 3.11
- AWS credentials (IAM role, CLI profile, or env vars) / AWS 자격 증명
- uvx (Python MCP servers) / npx (Node.js MCP servers, optional)
- Amazon Bedrock access (for LLM mapping) / Bedrock 접근 (LLM 매핑용)

## License / 라이선스

MIT
