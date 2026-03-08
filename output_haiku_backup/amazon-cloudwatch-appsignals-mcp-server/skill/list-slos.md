---
name: list-slos
description: List all Service Level Objectives (SLOs) in Application Signals.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the list_slos tool in the cloudwatch-applicationsignals-mcp-server instead.

    Use this tool to:
    - Get a complete list of all SLOs in your account
    - Discover SLO names and ARNs for use with other tools
    - Filter SLOs by service attributes
    - See basic SLO information including creation time and operation names

    Returns a formatted list showing:
    - SLO name and ARN
    - Associated service key attributes
    - Operation name being monitored
    - Creation timestamp
    - Total count of SLOs found

    This tool is useful for:
    - SLO discovery and inventory
    - Finding SLO names to use with get_slo() or audit_service_health()
    - Understanding what operations are being monitored
    
---

# List Slos

List all Service Level Objectives (SLOs) in Application Signals.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the list_slos tool in the cloudwatch-applicationsignals-mcp-server instead.

    Use this tool to:
    - Get a complete list of all SLOs in your account
    - Discover SLO names and ARNs for use with other tools
    - Filter SLOs by service attributes
    - See basic SLO information including creation time and operation names

    Returns a formatted list showing:
    - SLO name and ARN
    - Associated service key attributes
    - Operation name being monitored
    - Creation timestamp
    - Total count of SLOs found

    This tool is useful for:
    - SLO discovery and inventory
    - Finding SLO names to use with get_slo() or audit_service_health()
    - Understanding what operations are being monitored
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key_attributes` | string | No | JSON string of key attributes to filter SLOs (e.g., '{"Name": "my-service", "Environment": "ecs:my-cluster"}'. Defaults to empty object to list all SLOs. |
| `include_linked_accounts` | boolean | No | Whether to include SLOs from linked accounts (default: True) |
| `max_results` | integer | No | Maximum number of SLOs to return (default: 50, max: 50) |

## AWS CLI

```bash
aws cloudwatch list-service-level-objectives --key-attributes <key_attributes> --include-linked-accounts <include_linked_accounts> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.list_service_level_objectives(
    KeyAttributes=key_attributes,
    IncludeLinkedAccounts=include_linked_accounts,
    MaxResults=max_results,
)
```
