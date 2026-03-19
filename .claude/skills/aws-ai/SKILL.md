---
name: aws-ai
description: Manage AWS AI/ML services (Bedrock, SageMaker, Kendra, Q Business) without MCP. Use when the user asks about foundation models, knowledge bases, agents, embeddings, SageMaker endpoints, Kendra search, or Amazon Q.
---

# AWS AI & Machine Learning / AWS AI 및 머신러닝
# MCP 없이 boto3/CLI로 직접 AI/ML 서비스를 관리합니다.

## When to Use / 사용 시점
- "Bedrock 모델 목록" / "List Bedrock models"
- "Knowledge Base 조회" / "Query knowledge base"
- "SageMaker 엔드포인트 확인" / "Check SageMaker endpoints"
- "Kendra 인덱스 검색" / "Search Kendra index"
- "텍스트 임베딩 생성" / "Generate text embeddings"

## Amazon Bedrock / 파운데이션 모델

### 모델 목록 및 호출
```bash
# 사용 가능한 모델 목록
aws bedrock list-foundation-models --query 'modelSummaries[].{ID:modelId,Name:modelName,Provider:providerName}'

# 모델 상세
aws bedrock get-foundation-model --model-identifier anthropic.claude-sonnet-4-6-20250514-v1:0
```

```python
import boto3, json
bedrock = boto3.client('bedrock')
bedrock_runtime = boto3.client('bedrock-runtime')

# 모델 목록
bedrock.list_foundation_models()

# 모델 호출 (Converse API)
bedrock_runtime.converse(
    modelId='anthropic.claude-sonnet-4-6-20250514-v1:0',
    messages=[{'role': 'user', 'content': [{'text': 'Hello!'}]}],
    inferenceConfig={'maxTokens': 1024}
)

# 텍스트 임베딩
bedrock_runtime.invoke_model(
    modelId='amazon.titan-embed-text-v2:0',
    body=json.dumps({'inputText': 'AWS Bedrock is great'})
)
```

### Knowledge Bases / 지식 기반
```python
bedrock_agent = boto3.client('bedrock-agent')
bedrock_agent_runtime = boto3.client('bedrock-agent-runtime')

# Knowledge Base 목록
bedrock_agent.list_knowledge_bases()

# Knowledge Base 검색
bedrock_agent_runtime.retrieve(
    knowledgeBaseId='KB-xxxxx',
    retrievalQuery={'text': 'How to configure VPC?'}
)

# Knowledge Base + 모델 응답 (RAG)
bedrock_agent_runtime.retrieve_and_generate(
    input={'text': 'How to configure VPC?'},
    retrieveAndGenerateConfiguration={
        'type': 'KNOWLEDGE_BASE',
        'knowledgeBaseConfiguration': {
            'knowledgeBaseId': 'KB-xxxxx',
            'modelArn': 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-sonnet-4-6-20250514-v1:0'
        }
    }
)
```

### Bedrock Agents / 에이전트
```python
# 에이전트 목록
bedrock_agent.list_agents()

# 에이전트 상세
bedrock_agent.get_agent(agentId='AGENT-xxxxx')

# 에이전트 호출
bedrock_agent_runtime.invoke_agent(
    agentId='AGENT-xxxxx',
    agentAliasId='ALIAS-xxxxx',
    sessionId='session-123',
    inputText='What are the latest AWS announcements?'
)
```

### Guardrails / 가드레일
```python
# 가드레일 목록
bedrock.list_guardrails()

# 가드레일로 콘텐츠 필터링
bedrock_runtime.apply_guardrail(
    guardrailIdentifier='guardrail-xxxxx',
    guardrailVersion='DRAFT',
    source='INPUT',
    content=[{'text': {'text': 'User input to check'}}]
)
```

## Amazon SageMaker / 머신러닝 플랫폼

```bash
# 엔드포인트 목록
aws sagemaker list-endpoints --query 'Endpoints[].{Name:EndpointName,Status:EndpointStatus}'

# 모델 목록
aws sagemaker list-models --query 'Models[].{Name:ModelName,Created:CreationTime}'

# 학습 작업 목록
aws sagemaker list-training-jobs --status-equals InProgress
```

```python
sm = boto3.client('sagemaker')
sm_runtime = boto3.client('sagemaker-runtime')

# 엔드포인트 목록
sm.list_endpoints()

# 엔드포인트 상세
sm.describe_endpoint(EndpointName='my-endpoint')

# 엔드포인트 호출 (추론)
sm_runtime.invoke_endpoint(
    EndpointName='my-endpoint',
    ContentType='application/json',
    Body=json.dumps({'inputs': 'Hello world'})
)

# 학습 작업 상태
sm.describe_training_job(TrainingJobName='my-training-job')
```

## Amazon Kendra / 지능형 검색

```python
kendra = boto3.client('kendra')

# 인덱스 목록
kendra.list_indices()

# 검색
kendra.query(
    IndexId='index-xxxxx',
    QueryText='How to set up VPN?',
    PageSize=5
)

# 데이터 소스 목록
kendra.list_data_sources(IndexId='index-xxxxx')
```

## Amazon Q Business

```python
q = boto3.client('qbusiness')

# 애플리케이션 목록
q.list_applications()

# 대화
q.chat_sync(
    applicationId='app-xxxxx',
    userMessage='What is our company policy on remote work?'
)
```

## Notes / 참고
- Bedrock 모델 접근은 리전별로 활성화 필요 (Model access에서 요청)
- Converse API는 모든 Bedrock 모델에 통합 인터페이스 제공
- SageMaker 엔드포인트 호출은 `sagemaker-runtime` 클라이언트 사용
- Knowledge Base는 OpenSearch Serverless 또는 기타 벡터 DB 필요
