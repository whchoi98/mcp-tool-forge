---
name: get-group
description: Get detailed information about a specific IAM group.

    This tool retrieves comprehensive information about an IAM group including
    group members, attached policies, and inline policies. Use this to get
    a complete picture of a group's configuration and membership.

    ## Usage Tips:
    - Use this after list_groups to get detailed information about specific groups
    - Review attached policies to understand group permissions
    - Check group members to see who has these permissions

    Args:
        group_name: The name of the IAM group

    Returns:
        GroupDetailsResponse containing comprehensive group information
    
---

# Get Group

Get detailed information about a specific IAM group.

    This tool retrieves comprehensive information about an IAM group including
    group members, attached policies, and inline policies. Use this to get
    a complete picture of a group's configuration and membership.

    ## Usage Tips:
    - Use this after list_groups to get detailed information about specific groups
    - Review attached policies to understand group permissions
    - Check group members to see who has these permissions

    Args:
        group_name: The name of the IAM group

    Returns:
        GroupDetailsResponse containing comprehensive group information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `group_name` | string | Yes | The name of the IAM group to retrieve |

## AWS CLI

```bash
aws iam get-group --group-name <group_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.get_group(
    GroupName=group_name,
)
```
