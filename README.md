# MCP Tool Forge

A Python CLI tool that extracts tools from MCP servers and converts them into **5 formats**: boto3, AWS CLI, OpenAPI schemas, AgentCore Gateway configs, and Claude Code / Kiro-CLI Skills.
Includes **9 ready-to-use AWS Skills** for Claude Code and Kiro-CLI.

> **[한국어 버전은 아래에 있습니다 / Korean version below](#mcp-tool-forge-한국어)**

---

## Why?

### The MCP Token Cost Problem

MCP is powerful, but **every tool definition and request/response consumes LLM tokens**.

```
Token consumption per conversation:

┌─────────────┐     JSON Schema (tool defs)      ┌─────────┐
│  LLM Agent  │ ◄──────── ~2,000 tokens/tool ──── │   MCP   │
│             │ ──────── request (function call) ► │  Server │
│             │ ◄──────── response (result) ────── │         │
└─────────────┘                                   └─────────┘
```

**Real-world measurement (Kiro-CLI):**

| Scenario | Credits | Token Usage |
|----------|---------|-------------|
| 4 MCP servers ON | 0.71 | Schema loading + response |
| 4 MCP servers OFF (Skills only) | **0.27** | Selective skill loading |
| **Savings** | **62%** | |

Loading all 792 tools from 67 AWS MCP servers would consume **~1.5M tokens** just for tool definitions.

### How MCP Tool Forge Solves This

```
Extract once → Convert to native code → Run without MCP

  MCP way:    Agent ←→ MCP Server ←→ AWS API  (tokens every time)
  Skill way:  Agent → boto3/CLI code → AWS API  (zero tokens, zero latency)
```

| Comparison | MCP Approach | Skill Approach |
|------------|-------------|---------------|
| Tool definition tokens | ~2,000/tool (per conversation) | **0** (embedded in code) |
| Request/response tokens | JSON-RPC roundtrip | **0** (direct execution) |
| Server dependency | Always required | **Not required** |
| Latency | MCP server roundtrip | **0** |
| Offline support | No | **Yes** |

---

## Skills Installation (3 lines)

> **No MCP servers, Python packages, or Bedrock access required.**
> Just AWS credentials and you're ready.

### Claude Code

```bash
git clone https://github.com/whchoi98/mcp-tool-forge.git
mkdir -p .claude/skills
cp -r mcp-tool-forge/.claude/skills/aws-* .claude/skills/
```

### Kiro-CLI

```bash
git clone https://github.com/whchoi98/mcp-tool-forge.git
mkdir -p .kiro/skills
cp -r mcp-tool-forge/.claude/skills/aws-* .kiro/skills/
```

### Global Installation (all projects)

```bash
# Claude Code
mkdir -p ~/.claude/skills
cp -r mcp-tool-forge/.claude/skills/aws-* ~/.claude/skills/

# Kiro-CLI
mkdir -p ~/.kiro/skills
cp -r mcp-tool-forge/.claude/skills/aws-* ~/.kiro/skills/
```

### Install Specific Skills

```bash
# Claude Code
cp -r mcp-tool-forge/.claude/skills/aws-iam .claude/skills/
cp -r mcp-tool-forge/.claude/skills/aws-cost .claude/skills/
cp -r mcp-tool-forge/.claude/skills/aws-network .claude/skills/

# Kiro-CLI
cp -r mcp-tool-forge/.claude/skills/aws-iam .kiro/skills/
cp -r mcp-tool-forge/.claude/skills/aws-network .kiro/skills/
```

Natural language triggers activate skills automatically:

| Request | Skill |
|---------|-------|
| "List IAM users" | aws-iam |
| "Show this month's costs" | aws-cost |
| "Check CloudWatch alarms" | aws-cloudwatch |
| "List Lambda functions" | aws-infra |
| "List SQS queues" | aws-messaging |
| "Check VPC network" | aws-network |
| "List Bedrock models" | aws-ai |
| "Query DynamoDB tables" | aws-data |
| "Run security audit" | aws-security |

---

## 9 AWS Skills

| Skill | Trigger | Operations |
|-------|---------|------------|
| **aws-iam** | "IAM users/roles/policies" | list_users, create_role, attach_policy, simulate_policy |
| **aws-cloudwatch** | "Logs/metrics/alarms/audit" | Logs Insights, get_metric_data, describe_alarms, CloudTrail |
| **aws-cost** | "Cost/billing/pricing" | get_cost_and_usage, cost_forecast, pricing lookup |
| **aws-infra** | "Resources/stacks/containers" | Cloud Control API, CloudFormation, EKS, ECS, Lambda |
| **aws-messaging** | "Queues/topics/messages" | SNS publish, SQS send/receive, MQ, Step Functions |
| **aws-network** | "VPC/subnet/TGW/VPN" | VPC, Transit Gateway, Cloud WAN, Network Firewall, VPN, Flow Logs |
| **aws-ai** | "Bedrock/SageMaker/Kendra" | Bedrock Converse, Knowledge Bases, Agents, SageMaker, Kendra, Q Business |
| **aws-data** | "DB/cache/query" | DynamoDB, Aurora, Redshift, ElastiCache, Neptune |
| **aws-security** | "Account/credentials/audit" | get_caller_identity, credential audit, MFA check |

### Skills Coverage

The 9 hand-crafted skills cover **52 of 67 MCP servers (78%)**.

Uncovered 15 servers:

| Category | Uncovered Servers | Reason |
|----------|------------------|--------|
| Core / Essential | aws-api, core-mcp, aws-mcp | MCP proxy/planning — not a specific service |
| Documentation | aws-documentation, aws-knowledge | Doc search only — not a boto3/CLI target |
| Developer Tools | aws-diagram, aws-msk, code-doc-gen, frontend, git-repo-research, synthetic-data | Dev tools (diagrams, Kafka, code docs, etc.) |
| Healthcare | aws-healthomics, healthimaging, healthlake | Specialized healthcare services |
| Cost & Operations | aws-managed-prometheus | Prometheus monitoring |

> Uncovered servers can still be used through **792 auto-generated skills** via `mcp-tool-forge convert`.

### Skills Test Results

Tested on a real AWS account (Seoul region, IAM role auth):

| # | Skill | Test | Result |
|---|-------|------|--------|
| 1 | aws-security | `sts get-caller-identity` | Pass |
| 2 | aws-iam | `list-users` | Pass (2 users) |
| 3 | aws-iam | `list-roles` | Pass (13 roles) |
| 4 | aws-cloudwatch | `describe-log-groups` | Pass |
| 5 | aws-cloudwatch | `describe-alarms` | Pass |
| 6 | aws-infra | Cloud Control EC2 | Pass |
| 7 | aws-infra | Cloud Control S3 | Pass (1 bucket) |
| 8 | aws-infra | CloudFormation stacks | Pass |
| 9 | aws-cost | `get-cost-and-usage` | Pass ($1,093) |
| 10 | aws-cost | Cost by service (top 5) | Pass |
| 11 | aws-security | MFA check (boto3) | Pass (2 NO MFA) |
| 12 | aws-security | Access key age (boto3) | Pass (23 days) |
| 13 | aws-security | Account summary (boto3) | Pass (Root MFA: NO) |
| 14 | aws-messaging | SNS topics | Pass |
| 15 | aws-messaging | SQS queues | Pass |
| 16 | aws-data | DynamoDB tables | Pass |
| 17 | aws-infra | Lambda functions | Pass |

**17/17 passed** — All skills work with standard AWS credentials.

---

## Token Economics: MCP vs Skills

### Why Does MCP Consume So Many Tokens?

When MCP servers load, **all tool JSON Schemas are injected into the LLM context**. This is necessary for the LLM to "know" available tools, but most tools go unused.

```
Example: IAM MCP server loading

  29 tools x ~2,000 tokens/tool = ~58,000 tokens (definitions only)
  + request/response JSON-RPC roundtrip = ~500 tokens/call

  All 67 servers loaded:
  792 tools x ~2,000 tokens = ~1,584,000 tokens (~1.5M)
```

### How Skills Save Tokens

Skills use **selective loading** — only the relevant skill is loaded per request.

```
Example: "List IAM users" request

  MCP way:   Load all 29 tool schemas (58,000 tokens) -> use 1
  Skill way: Load aws-iam SKILL.md (~3,000 tokens) -> execute directly
```

| Item | MCP (1 server) | MCP (all 67) | Skill |
|------|---------------|--------------|-------|
| Initial loading | ~58,000 tokens | ~1,584,000 tokens | **~3,000 tokens** |
| Per tool call | ~500 tokens | ~500 tokens | **0 tokens** |
| Server processes | 1 required | 67 required | **0** |
| Cold start | 2-5s | 30s+ | **0s** |

### Cost Estimation (Claude Opus 4.6, $15/1M input tokens)

| Scenario | Input Tokens | Cost |
|----------|-------------|------|
| MCP 1 server/conversation | 58,000 | $0.87 |
| MCP 10 servers/conversation | 580,000 | $8.70 |
| **Skill 1/conversation** | **3,000** | **$0.045** |
| **Skill all 9/conversation** | **27,000** | **$0.41** |

> **Skills reduce token costs by 95%+ compared to MCP.**

---

## Quick Start (CLI Tool)

> If you only need Skills, skip this section. [Skills Installation](#skills-installation-3-lines) above is all you need.

```bash
# Install
pip install -e ".[dev]"

# List servers
mcp-tool-forge list-servers
mcp-tool-forge list-servers --category "Data & Analytics"

# Check tools (connects to real MCP server)
mcp-tool-forge list-tools --server aws-iam-mcp-server

# Convert to all formats
mcp-tool-forge convert --server aws-iam-mcp-server --output all

# LLM mapping (Bedrock Claude)
mcp-tool-forge convert --server amazon-cloudwatch-mcp-server --output all --llm-assist

# Multi-profile support (set default profile in generated code)
mcp-tool-forge convert --server aws-iam-mcp-server --output boto3 --aws-profile prod-account

# Register skills to Claude Code
mcp-tool-forge register --server aws-iam-mcp-server -d output

# Register skills to Kiro-CLI
mcp-tool-forge register --server aws-iam-mcp-server -d output --target kiro
```

### Multi AWS Profile Support

Use `--aws-profile` to set a default AWS profile in generated boto3 code.
Useful for AWS Organizations + SSO environments with multiple accounts.

```python
# Generated without --aws-profile (default)
def list_users(profile_name: str | None = None, **kwargs) -> dict:
    session = boto3.Session(profile_name=profile_name)
    client = session.client('iam')
    ...

# Generated with --aws-profile prod-account
def list_users(profile_name: str | None = "prod-account", **kwargs) -> dict:
    session = boto3.Session(profile_name=profile_name)
    client = session.client('iam')
    ...

# Override profile at call time
list_users()                                  # Uses default profile
list_users(profile_name="staging-account")    # Switch to another account
```

### Output Formats

| Format | File | Purpose |
|--------|------|---------|
| **boto3** (.py) | `output/*/boto3/tools.py` | Direct invocation from AgentCore Gateway Lambda |
| **AWS CLI** (.sh) | `output/*/cli/tools.sh` | Shell-based agents, automation scripts |
| **Schema** (.json) | `output/*/schema/tools.json` | OpenAPI-compatible tool definitions |
| **AgentCore** (.json) | `output/*/agentcore/tool_config.json` | Bedrock AgentCore Gateway toolSpec |
| **Skill** (.md) | `output/*/skill/*.md` | Claude Code / Kiro-CLI skills |

---

## Architecture

```
┌──────────────────────────────────────────────────────┐
│                    mcp-tool-forge                     │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Phase 1: Schema Extraction                          │
│  ┌───────────┐  tools/list  ┌────────────────┐      │
│  │ MCP Server ├────────────►│ Schema Cache    │      │
│  │ (stdio)    │  MCP SDK    │(~/.mcp-tool-forge)│    │
│  └───────────┘              └───────┬────────┘      │
│                                      │               │
│  Phase 2: Static Mapping             │               │
│  ┌──────────────┐                    │               │
│  │ YAML Mappings │◄──────────────────┘               │
│  │ (iam, dynamo) │                                   │
│  └──────┬───────┘                                   │
│         │ unmapped                                   │
│  Phase 3: LLM Inference                              │
│  ┌──────▼───────┐                                   │
│  │ Bedrock Claude│  tool schema → boto3 mapping      │
│  │ (Opus 4.6)    │                                   │
│  └──────┬───────┘                                   │
│         │                                            │
│  Code Generation                                     │
│  ┌──────▼───────┐                                   │
│  │  Generators   │  boto3 / cli / schema /           │
│  │  (Jinja2)     │  agentcore / skill                │
│  └──────────────┘                                   │
└──────────────────────────────────────────────────────┘
```

1. **Extract** — MCP SDK `stdio_client` connects to server, `tools/list` extracts schemas. Cached in `~/.mcp-tool-forge/cache/`.
2. **Static Map** — Known mappings from `mappings/*.yaml` (IAM 29 + DynamoDB 6 = 35 tools).
3. **LLM Map** — Unmapped tools sent to Bedrock Claude Opus 4.6 for inference. `--llm-assist` flag.

---

## Extraction Results

| Metric | Value |
|--------|-------|
| Registered servers | **67** |
| Servers connected | **55 / 67** (82%) |
| Tools extracted | **792** |
| boto3 functions | **480+** |
| Skills generated | **792** |
| Syntax pass rate | **91.4%** (after auto-fix) |

## Supported Servers (67)

| Category | Count | Servers |
|----------|-------|---------|
| Data & Analytics | 18 | DynamoDB, Aurora, Redshift, ElastiCache, Neptune |
| Infrastructure & Deployment | 11 | EKS, ECS, CDK, CloudFormation, Network, Terraform, Serverless |
| AI & Machine Learning | 10 | Bedrock, SageMaker, Kendra, Nova Canvas |
| Cost & Operations | 8 | CloudWatch, CloudTrail, Cost Explorer, Billing |
| Developer Tools & Support | 7 | IAM, MSK, Diagram, Code Doc Gen |
| Integration & Messaging | 5 | SNS/SQS, MQ, Step Functions, Location |
| Healthcare & Lifesciences | 3 | HealthOmics, HealthImaging, HealthLake |
| Core | 2 | AWS API, Core MCP |
| Documentation | 2 | AWS Documentation, Knowledge |
| Essential Setup | 1 | AWS MCP (unified proxy) |

---

## Project Structure

```
mcp-tool-forge/
├── .claude/skills/             # 9 AWS Skills (portable)
│   ├── aws-iam/                # IAM users, roles, policies
│   ├── aws-cloudwatch/         # Logs, metrics, alarms, CloudTrail
│   ├── aws-cost/               # Cost Explorer, billing, pricing
│   ├── aws-infra/              # CloudFormation, EKS, ECS, Lambda
│   ├── aws-messaging/          # SNS, SQS, MQ, Step Functions
│   ├── aws-network/            # VPC, Transit Gateway, Cloud WAN, VPN
│   ├── aws-ai/                 # Bedrock, SageMaker, Kendra, Q Business
│   ├── aws-data/               # DynamoDB, Aurora, Redshift, Neptune
│   └── aws-security/           # Account info, security audit
├── src/mcp_to_cli/
│   ├── cli.py                  # Click CLI entry point
│   ├── pipeline.py             # 3-phase orchestrator
│   ├── connector.py            # MCP SDK stdio_client
│   ├── registry.yaml           # 67 server configs
│   ├── llm_mapper.py           # Bedrock Claude Opus 4.6
│   ├── validator.py            # Generated code fixer
│   ├── generators/             # 5 output generators
│   ├── mappings/               # Static YAML (IAM, DynamoDB)
│   └── templates/              # 6 Jinja2 templates
├── tests/                      # 38 pytest tests
└── docs/                       # Architecture & plans
```

## Development

```bash
pip install -e ".[dev]"      # Install
python -m pytest tests/ -v   # Test (38 tests)
```

## Requirements

| Item | Skills Only | Full CLI Tool |
|------|------------|--------------|
| Python >= 3.11 | Not required | Required |
| AWS credentials | Required | Required |
| uvx / npx | Not required | Required (MCP server execution) |
| Bedrock access | Not required | Optional (LLM mapping) |

## License

MIT

---
---

# MCP Tool Forge (한국어)

MCP 서버의 도구를 추출하여 **boto3, AWS CLI, OpenAPI 스키마, AgentCore Gateway, Claude Code / Kiro-CLI Skill** 5가지 형식으로 변환하는 Python CLI 도구.
**9개 AWS Skills**을 포함하며 Claude Code와 Kiro-CLI 모두 지원합니다.

> **[English version above / 영어 버전은 위에 있습니다](#mcp-tool-forge)**

---

## 왜 필요한가?

### MCP의 토큰 비용 문제

MCP 프로토콜은 강력하지만, **모든 도구 정의와 요청/응답이 LLM 토큰으로 소모**됩니다.

```
매 대화마다 발생하는 토큰 소비:

┌─────────────┐     JSON Schema (도구 정의)      ┌─────────┐
│  LLM Agent  │ ◄──────── ~2,000 토큰/도구 ────── │   MCP   │
│             │ ──────── 요청 (함수 호출) ────────► │  Server │
│             │ ◄──────── 응답 (결과) ──────────── │         │
└─────────────┘                                   └─────────┘
```

**실제 측정 결과 (Kiro-CLI 기준):**

| 시나리오 | Credits | 토큰 사용량 |
|---------|---------|-----------|
| MCP 서버 4개 ON | 0.71 | 도구 스키마 로딩 + 응답 |
| MCP 서버 4개 OFF (Skills만) | **0.27** | 필요한 스킬만 선택 로딩 |
| **절감률** | **62%** | |

67개 AWS MCP 서버에서 792개 도구를 전부 로딩하면, 도구 정의만으로 **~150만 토큰**이 소모됩니다.

### MCP Tool Forge의 해법

```
한 번 추출 → 네이티브 코드로 변환 → MCP 없이 직접 실행

  MCP 방식:   Agent ←→ MCP Server ←→ AWS API  (매번 토큰 소비)
  Skill 방식:  Agent → boto3/CLI 코드 → AWS API  (토큰 0, 지연 0)
```

| 비교 | MCP 방식 | Skill 방식 |
|------|---------|-----------|
| 도구 정의 토큰 | ~2,000/도구 (매 대화) | **0** (코드에 내장) |
| 요청/응답 토큰 | JSON-RPC 왕복 | **0** (직접 실행) |
| 서버 의존성 | 항상 실행 필요 | **불필요** |
| 지연 시간 | MCP 서버 왕복 | **0** |
| 오프라인 동작 | 불가 | **가능** |

---

## Skills 설치 (3줄이면 끝)

> **MCP 서버 설치, Python 패키지, Bedrock 접근 모두 불필요.**
> AWS 자격 증명만 있으면 바로 사용할 수 있습니다.

### Claude Code

```bash
git clone https://github.com/whchoi98/mcp-tool-forge.git
mkdir -p .claude/skills
cp -r mcp-tool-forge/.claude/skills/aws-* .claude/skills/
```

### Kiro-CLI

```bash
git clone https://github.com/whchoi98/mcp-tool-forge.git
mkdir -p .kiro/skills
cp -r mcp-tool-forge/.claude/skills/aws-* .kiro/skills/
```

### 글로벌 설치 (모든 프로젝트에 적용)

```bash
# Claude Code
mkdir -p ~/.claude/skills
cp -r mcp-tool-forge/.claude/skills/aws-* ~/.claude/skills/

# Kiro-CLI
mkdir -p ~/.kiro/skills
cp -r mcp-tool-forge/.claude/skills/aws-* ~/.kiro/skills/
```

### 특정 스킬만 설치

```bash
# Claude Code 예시
cp -r mcp-tool-forge/.claude/skills/aws-iam .claude/skills/
cp -r mcp-tool-forge/.claude/skills/aws-cost .claude/skills/
cp -r mcp-tool-forge/.claude/skills/aws-network .claude/skills/

# Kiro-CLI 예시
cp -r mcp-tool-forge/.claude/skills/aws-iam .kiro/skills/
cp -r mcp-tool-forge/.claude/skills/aws-network .kiro/skills/
```

설치 후 자연어로 요청하면 스킬이 자동 활성화됩니다:

| 요청 예시 | 활성화 스킬 |
|----------|-----------|
| "IAM 사용자 목록 보여줘" | aws-iam |
| "이번 달 비용은?" | aws-cost |
| "CloudWatch 알람 확인" | aws-cloudwatch |
| "Lambda 함수 목록" | aws-infra |
| "SQS 큐 목록" | aws-messaging |
| "VPC 네트워크 확인" | aws-network |
| "Bedrock 모델 목록" | aws-ai |
| "DynamoDB 테이블 조회" | aws-data |
| "보안 감사 실행" | aws-security |

---

## 9개 AWS Skills

| Skill | 트리거 | 주요 작업 |
|-------|--------|----------|
| **aws-iam** | "IAM 사용자/역할/정책" | list_users, create_role, attach_policy, simulate_policy |
| **aws-cloudwatch** | "로그/메트릭/알람/감사" | Logs Insights, get_metric_data, describe_alarms, CloudTrail |
| **aws-cost** | "비용/청구/가격" | get_cost_and_usage, cost_forecast, pricing lookup |
| **aws-infra** | "리소스/스택/컨테이너" | Cloud Control API, CloudFormation, EKS, ECS, Lambda |
| **aws-messaging** | "큐/토픽/메시지/워크플로" | SNS publish, SQS send/receive, MQ, Step Functions |
| **aws-network** | "VPC/서브넷/TGW/VPN" | VPC, Transit Gateway, Cloud WAN, Network Firewall, VPN, Flow Logs |
| **aws-ai** | "Bedrock/SageMaker/Kendra" | Bedrock Converse, Knowledge Bases, Agents, SageMaker, Kendra, Q Business |
| **aws-data** | "DB/캐시/쿼리" | DynamoDB, Aurora, Redshift, ElastiCache, Neptune |
| **aws-security** | "계정/자격증명/보안감사" | get_caller_identity, credential audit, MFA check |

### Skills 커버리지

9개 수동 스킬은 67개 MCP 서버 중 **52개 (78%)**를 커버합니다.

미커버 15개 서버:

| 카테고리 | 미커버 서버 | 사유 |
|----------|-----------|------|
| Core / Essential | aws-api, core-mcp, aws-mcp | MCP 프록시/플래닝 — 특정 서비스가 아님 |
| Documentation | aws-documentation, aws-knowledge | 문서 검색 전용 — boto3/CLI 대상 아님 |
| Developer Tools | aws-diagram, aws-msk, code-doc-gen, frontend, git-repo-research, synthetic-data | 개발 도구 (다이어그램, Kafka, 코드 문서화 등) |
| Healthcare | aws-healthomics, healthimaging, healthlake | 헬스케어 전문 서비스 |
| Cost & Operations | aws-managed-prometheus | Prometheus 모니터링 |

> 미커버 서버도 `mcp-tool-forge convert`로 자동 생성된 **792개 개별 스킬**을 통해 사용 가능합니다.

### Skills 테스트 결과

실제 AWS 계정에서 테스트 (서울 리전, IAM 역할 인증):

| # | Skill | 테스트 | 결과 |
|---|-------|--------|------|
| 1 | aws-security | `sts get-caller-identity` | Pass |
| 2 | aws-iam | `list-users` | Pass (2 users) |
| 3 | aws-iam | `list-roles` | Pass (13 roles) |
| 4 | aws-cloudwatch | `describe-log-groups` | Pass |
| 5 | aws-cloudwatch | `describe-alarms` | Pass |
| 6 | aws-infra | Cloud Control EC2 | Pass |
| 7 | aws-infra | Cloud Control S3 | Pass (1 bucket) |
| 8 | aws-infra | CloudFormation stacks | Pass |
| 9 | aws-cost | `get-cost-and-usage` | Pass ($1,093) |
| 10 | aws-cost | Cost by service (top 5) | Pass |
| 11 | aws-security | MFA check (boto3) | Pass (2 NO MFA) |
| 12 | aws-security | Access key age (boto3) | Pass (23 days) |
| 13 | aws-security | Account summary (boto3) | Pass (Root MFA: NO) |
| 14 | aws-messaging | SNS topics | Pass |
| 15 | aws-messaging | SQS queues | Pass |
| 16 | aws-data | DynamoDB tables | Pass |
| 17 | aws-infra | Lambda functions | Pass |

**17/17 통과** — 모든 스킬이 표준 AWS 자격 증명으로 동작합니다.

---

## 토큰 경제학: MCP vs Skills

### 왜 MCP는 토큰을 많이 소모하는가?

MCP 서버가 로딩되면 **모든 도구의 JSON Schema가 LLM 컨텍스트에 주입**됩니다. 이는 LLM이 어떤 도구를 사용할 수 있는지 "알기 위해" 필요하지만, 대부분의 도구는 사용되지 않습니다.

```
예: IAM MCP 서버 로딩 시

  29개 도구 x ~2,000 토큰/도구 = ~58,000 토큰 (도구 정의만)
  + 요청/응답 JSON-RPC 왕복 = ~500 토큰/호출

  67개 서버 전체 로딩 시:
  792개 도구 x ~2,000 토큰 = ~1,584,000 토큰 (약 150만)
```

### Skills는 어떻게 토큰을 절약하는가?

Skills는 **필요한 스킬만 선택적으로 로딩**합니다.

```
예: "IAM 사용자 목록 보여줘" 요청 시

  MCP 방식:  29개 도구 스키마 전체 로딩 (58,000 토큰) -> 1개 사용
  Skill 방식: aws-iam SKILL.md 1개 로딩 (~3,000 토큰) -> 바로 실행
```

| 항목 | MCP (서버 1개) | MCP (67개 전체) | Skill |
|------|--------------|----------------|-------|
| 초기 로딩 | ~58,000 토큰 | ~1,584,000 토큰 | **~3,000 토큰** |
| 도구 호출 | ~500 토큰/회 | ~500 토큰/회 | **0 토큰** |
| 서버 프로세스 | 1개 필요 | 67개 필요 | **0개** |
| 콜드 스타트 | 2~5초 | 30초+ | **0초** |

### 비용 환산 (Claude Opus 4.6 기준)

| 시나리오 | 입력 토큰 | 비용 ($15/1M 토큰) |
|---------|---------|-------------------|
| MCP 1개 서버/대화 | 58,000 | $0.87/대화 |
| MCP 10개 서버/대화 | 580,000 | $8.70/대화 |
| **Skill 1개/대화** | **3,000** | **$0.045/대화** |
| **Skill 전체/대화** | **27,000** | **$0.41/대화** |

> **Skill 방식은 MCP 대비 토큰 비용을 95% 이상 절감합니다.**

---

## 빠른 시작 (CLI 도구)

> Skills만 사용하려면 이 섹션은 건너뛰어도 됩니다. 위의 [Skills 설치](#skills-설치-3줄이면-끝)만으로 충분합니다.

```bash
# 설치
pip install -e ".[dev]"

# 서버 목록 조회
mcp-tool-forge list-servers
mcp-tool-forge list-servers --category "Data & Analytics"

# 도구 확인 (실제 MCP 서버 연결)
mcp-tool-forge list-tools --server aws-iam-mcp-server

# 모든 형식으로 변환
mcp-tool-forge convert --server aws-iam-mcp-server --output all

# LLM 매핑 (Bedrock Claude)
mcp-tool-forge convert --server amazon-cloudwatch-mcp-server --output all --llm-assist

# 멀티 AWS 프로필 지원 (생성 코드에 기본 프로필 설정)
mcp-tool-forge convert --server aws-iam-mcp-server --output boto3 --aws-profile prod-account

# Claude Code에 스킬 등록
mcp-tool-forge register --server aws-iam-mcp-server -d output

# Kiro-CLI에 스킬 등록
mcp-tool-forge register --server aws-iam-mcp-server -d output --target kiro
```

### 멀티 AWS 프로필 지원

`--aws-profile` 옵션으로 생성되는 boto3 코드에 AWS 프로필을 설정할 수 있습니다.
AWS Organizations + SSO 환경에서 여러 계정을 사용하는 경우 유용합니다.

```python
# --aws-profile 없이 생성 (기본)
def list_users(profile_name: str | None = None, **kwargs) -> dict:
    session = boto3.Session(profile_name=profile_name)
    client = session.client('iam')
    ...

# --aws-profile prod-account 으로 생성
def list_users(profile_name: str | None = "prod-account", **kwargs) -> dict:
    session = boto3.Session(profile_name=profile_name)
    client = session.client('iam')
    ...

# 호출 시 프로필 오버라이드 가능
list_users()                                  # 기본 프로필 사용
list_users(profile_name="staging-account")    # 다른 계정으로 전환
```

### 출력 형식

| 형식 | 파일 | 용도 |
|------|------|------|
| **boto3** (.py) | `output/*/boto3/tools.py` | AgentCore Gateway Lambda에서 직접 호출 |
| **AWS CLI** (.sh) | `output/*/cli/tools.sh` | Shell 기반 에이전트, 자동화 스크립트 |
| **Schema** (.json) | `output/*/schema/tools.json` | OpenAPI 호환 도구 정의 |
| **AgentCore** (.json) | `output/*/agentcore/tool_config.json` | Bedrock AgentCore Gateway toolSpec |
| **Skill** (.md) | `output/*/skill/*.md` | Claude Code / Kiro-CLI 스킬 |

---

## 아키텍처

```
┌──────────────────────────────────────────────────────┐
│                    mcp-tool-forge                     │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Phase 1: 스키마 추출                                 │
│  ┌───────────┐  tools/list  ┌────────────────┐      │
│  │ MCP Server ├────────────►│ Schema Cache    │      │
│  │ (stdio)    │  MCP SDK    │(~/.mcp-tool-forge)│    │
│  └───────────┘              └───────┬────────┘      │
│                                      │               │
│  Phase 2: 정적 매핑                    │               │
│  ┌──────────────┐                    │               │
│  │ YAML Mappings │◄──────────────────┘               │
│  │ (iam, dynamo) │                                   │
│  └──────┬───────┘                                   │
│         │ unmapped                                   │
│  Phase 3: LLM 추론                                   │
│  ┌──────▼───────┐                                   │
│  │ Bedrock Claude│  tool schema → boto3 mapping      │
│  │ (Opus 4.6)    │                                   │
│  └──────┬───────┘                                   │
│         │                                            │
│  코드 생성                                            │
│  ┌──────▼───────┐                                   │
│  │  Generators   │  boto3 / cli / schema /           │
│  │  (Jinja2)     │  agentcore / skill                │
│  └──────────────┘                                   │
└──────────────────────────────────────────────────────┘
```

1. **추출** — MCP SDK `stdio_client`로 서버 연결, `tools/list`로 스키마 추출. `~/.mcp-tool-forge/cache/`에 캐시.
2. **정적 매핑** — `mappings/*.yaml`에서 알려진 매핑 조회 (IAM 29 + DynamoDB 6 = 35개).
3. **LLM 매핑** — 미매핑 도구를 Bedrock Claude Opus 4.6에 전송. `--llm-assist` 플래그.

---

## 추출 결과

| 지표 | 값 |
|------|------|
| 등록 서버 | **67개** |
| 연결 성공 | **55 / 67** (82%) |
| 도구 추출 | **792개** |
| boto3 함수 | **480+** |
| 생성된 스킬 | **792개** |
| 구문 통과율 | **91.4%** (자동 수정 후) |

## 지원 서버 (67개)

| 카테고리 | 수 | 서버 |
|----------|---|------|
| Data & Analytics | 18 | DynamoDB, Aurora, Redshift, ElastiCache, Neptune |
| Infrastructure & Deployment | 11 | EKS, ECS, CDK, CloudFormation, Network, Terraform, Serverless |
| AI & Machine Learning | 10 | Bedrock, SageMaker, Kendra, Nova Canvas |
| Cost & Operations | 8 | CloudWatch, CloudTrail, Cost Explorer, Billing |
| Developer Tools & Support | 7 | IAM, MSK, Diagram, Code Doc Gen |
| Integration & Messaging | 5 | SNS/SQS, MQ, Step Functions, Location |
| Healthcare & Lifesciences | 3 | HealthOmics, HealthImaging, HealthLake |
| Core | 2 | AWS API, Core MCP |
| Documentation | 2 | AWS Documentation, Knowledge |
| Essential Setup | 1 | AWS MCP (unified proxy) |

---

## 프로젝트 구조

```
mcp-tool-forge/
├── .claude/skills/             # 9개 AWS Skills (이식 가능)
│   ├── aws-iam/                # IAM 사용자, 역할, 정책
│   ├── aws-cloudwatch/         # 로그, 메트릭, 알람, CloudTrail
│   ├── aws-cost/               # 비용 탐색기, 청구, 가격
│   ├── aws-infra/              # CloudFormation, EKS, ECS, Lambda
│   ├── aws-messaging/          # SNS, SQS, MQ, Step Functions
│   ├── aws-network/            # VPC, Transit Gateway, Cloud WAN, VPN
│   ├── aws-ai/                 # Bedrock, SageMaker, Kendra, Q Business
│   ├── aws-data/               # DynamoDB, Aurora, Redshift, Neptune
│   └── aws-security/           # 계정 정보, 보안 감사
├── src/mcp_to_cli/
│   ├── cli.py                  # Click CLI 진입점
│   ├── pipeline.py             # 3단계 오케스트레이터
│   ├── connector.py            # MCP SDK stdio_client
│   ├── registry.yaml           # 67개 서버 설정
│   ├── llm_mapper.py           # Bedrock Claude Opus 4.6
│   ├── validator.py            # 생성 코드 검증/수정
│   ├── generators/             # 5가지 출력 생성기
│   ├── mappings/               # 정적 YAML (IAM, DynamoDB)
│   └── templates/              # 6개 Jinja2 템플릿
├── tests/                      # 38개 pytest 테스트
└── docs/                       # 아키텍처 및 설계 문서
```

## 개발

```bash
pip install -e ".[dev]"      # 설치
python -m pytest tests/ -v   # 테스트 (38개)
```

## 요구사항

| 항목 | Skills만 사용 | CLI 도구 전체 |
|------|-------------|-------------|
| Python >= 3.11 | 불필요 | 필요 |
| AWS 자격 증명 | 필요 | 필요 |
| uvx / npx | 불필요 | 필요 (MCP 서버 실행) |
| Bedrock 접근 | 불필요 | 선택 (LLM 매핑용) |

## 라이선스

MIT
