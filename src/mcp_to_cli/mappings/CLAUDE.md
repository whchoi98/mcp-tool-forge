# Mappings Module

MCP tool -> boto3/CLI 정적 매핑 YAML 파일.

## Files
- `dynamodb.yaml` - DynamoDB 6개 tool
- `iam.yaml` - IAM 29개 tool

## Format
```yaml
tools:
  tool_name:
    boto3:
      client: <service>
      method: <method_name>
      params:
        BotoParamName: mcp_param_name
    cli:
      command: "aws <service> <command>"
      params:
        --flag: mcp_param_name
```

## Adding New Mappings
1. 실제 MCP 서버에서 tool schema 추출 (`mcp-to-cli list-tools`)
2. boto3 문서에서 해당 API 메서드 확인
3. 파라미터 이름 매핑 (MCP snake_case -> boto3 PascalCase)
4. `ctx` 파라미터는 MCP 전용이므로 제외
