---
name: get-managed-policy-document
description: Retrieve the policy document for a managed policy.

    This tool retrieves the policy document for a specific managed policy version.
    Use this to examine the actual permissions and wildcards in managed policies.

    Args:
        policy_arn: The ARN of the managed policy
        version_id: Optional version ID (defaults to current version)

    Returns:
        ManagedPolicyResponse containing the policy document and details
    
---

# Get Managed Policy Document

Retrieve the policy document for a managed policy.

    This tool retrieves the policy document for a specific managed policy version.
    Use this to examine the actual permissions and wildcards in managed policies.

    Args:
        policy_arn: The ARN of the managed policy
        version_id: Optional version ID (defaults to current version)

    Returns:
        ManagedPolicyResponse containing the policy document and details
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `policy_arn` | string | Yes | The ARN of the managed policy |
| `version_id` | string | No | The version ID of the policy (defaults to current version) |

## AWS CLI

```bash
aws iam get-policy-version --policy-arn <policy_arn> --version-id <version_id>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.get_policy_version(
    PolicyArn=policy_arn,
    VersionId=version_id,
)
```
