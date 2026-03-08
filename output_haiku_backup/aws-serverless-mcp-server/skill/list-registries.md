---
name: list-registries
description: Lists the registries in your account.

        REQUIREMENTS:
        - For AWS service events, you MUST use the aws.events registry directly
        - For custom schemas, you MAY use LOCAL scope to manage your own registries
        - When searching AWS service events, you SHOULD use the AWS scope

        USAGE PATTERNS:
        1. Finding AWS Service Event Schemas:
        - Use aws.events registry directly instead of searching
        - Filter by AWS scope to see only AWS-provided schemas

        2. Managing Custom Schemas:
        - Use LOCAL scope to view your custom registries
        - Apply registry_name_prefix to find specific registry groups
        
---

# List Registries

Lists the registries in your account.

        REQUIREMENTS:
        - For AWS service events, you MUST use the aws.events registry directly
        - For custom schemas, you MAY use LOCAL scope to manage your own registries
        - When searching AWS service events, you SHOULD use the AWS scope

        USAGE PATTERNS:
        1. Finding AWS Service Event Schemas:
        - Use aws.events registry directly instead of searching
        - Filter by AWS scope to see only AWS-provided schemas

        2. Managing Custom Schemas:
        - Use LOCAL scope to view your custom registries
        - Apply registry_name_prefix to find specific registry groups
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `registry_name_prefix` | string | No | Specifying this limits the results to only those registry names that start with the specified prefix. For EventBridge events, use aws.events registry directly instead of searching. |
| `scope` | string | No | Can be set to Local or AWS to limit responses to your custom registries, or the ones provided by AWS.
            LOCAL: The registry is created in your account.
            AWS: The registry is created by AWS.

            For EventBridge events, use aws.events registry which is an AWS-managed registry containing all AWS service event schemas. |
| `limit` | string | No | Maximum number of results to return. If you specify 0, the operation returns up to 10 results. |
| `next_token` | string | No | Next token returned by the previous operation. |

## AWS CLI

```bash
aws eventbridge list-registries --name-prefix <registry_name_prefix> --scope <scope> --limit <limit> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('eventbridge')
response = client.list_registries(
    NamePrefix=registry_name_prefix,
    Scope=scope,
    Limit=limit,
    NextToken=next_token,
)
```
