---
name: describe-log-groups
description: Describe CloudWatch Logs log groups.

    Args:
        account_identifiers: List of account IDs to filter log groups
        log_group_name_prefix: Prefix to filter log groups by name
        log_group_name_pattern: Pattern to match log group names
        include_linked_accounts: Whether to include log groups from linked accounts
        log_group_class: Filter by log group class (STANDARD or INFREQUENT_ACCESS)
        log_group_identifiers: List of log group identifiers to describe
        starting_token: Token for starting the list from a specific page
        page_size: Number of records to include in each page
        max_items: Maximum number of records to return in total

    Returns:
        Dict containing log groups information or error details
    
---

# Describe-Log-Groups

Describe CloudWatch Logs log groups.

    Args:
        account_identifiers: List of account IDs to filter log groups
        log_group_name_prefix: Prefix to filter log groups by name
        log_group_name_pattern: Pattern to match log group names
        include_linked_accounts: Whether to include log groups from linked accounts
        log_group_class: Filter by log group class (STANDARD or INFREQUENT_ACCESS)
        log_group_identifiers: List of log group identifiers to describe
        starting_token: Token for starting the list from a specific page
        page_size: Number of records to include in each page
        max_items: Maximum number of records to return in total

    Returns:
        Dict containing log groups information or error details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_identifiers` | string | No |  |
| `log_group_name_prefix` | string | No |  |
| `log_group_name_pattern` | string | No |  |
| `include_linked_accounts` | string | No |  |
| `log_group_class` | string | No |  |
| `log_group_identifiers` | string | No |  |
| `starting_token` | string | No |  |
| `page_size` | string | No |  |
| `max_items` | string | No |  |

## AWS CLI

```bash
aws logs describe-log-groups --log-group-name-prefix <log_group_name_prefix> --log-group-name-pattern <log_group_name_pattern> --log-group-class <log_group_class> --log-group-identifiers <log_group_identifiers> --starting-token <starting_token> --max-items <max_items> --page-size <page_size>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.describe_log_groups(
    LogGroupNamePrefix=log_group_name_prefix,
    LogGroupNamePattern=log_group_name_pattern,
    LogGroupClass=log_group_class,
    LogGroupIdentifiers=log_group_identifiers,
    NextToken=starting_token,
    Limit=page_size,
)
```
