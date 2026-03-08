# Mappings Module / 매핑 모듈

Static YAML mapping files for MCP tool -> boto3/CLI conversion.

MCP tool -> boto3/CLI 정적 매핑 YAML 파일.

## Files / 파일
- `dynamodb.yaml` - DynamoDB 6 tools / DynamoDB 6개 tool
- `iam.yaml` - IAM 29 tools / IAM 29개 tool

## Format / 형식
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

## Adding New Mappings / 새 매핑 추가 방법
1. Extract tool schema from real MCP server (`mcp-to-cli list-tools`) / 실제 MCP 서버에서 tool schema 추출 (`mcp-to-cli list-tools`)
2. Find the corresponding API method in boto3 docs / boto3 문서에서 해당 API 메서드 확인
3. Map parameter names (MCP snake_case -> boto3 PascalCase) / 파라미터 이름 매핑 (MCP snake_case -> boto3 PascalCase)
4. Exclude `ctx` parameter (MCP-only) / `ctx` 파라미터는 MCP 전용이므로 제외
