---
name: get-policies-for-role
description: Get all policies attached to an IAM role.

        This tool retrieves all policies associated with an IAM role, providing a comprehensive view
        of the role's permissions and trust relationships. It helps you understand the current
        permissions, identify missing or excessive permissions, troubleshoot EKS cluster issues,
        and verify trust relationships for service roles.

        IMPORTANT: Use this tool instead of 'aws iam get-role', 'aws iam list-attached-role-policies',
        'aws iam list-role-policies', and 'aws iam get-role-policy' commands.

        ## Requirements
        - The role must exist in your AWS account
        - Valid AWS credentials with permissions to read IAM role information

        ## Response Information
        The response includes role ARN, assume role policy document (trust relationships),
        role description, managed policies with their documents, and inline policies with
        their documents.

        ## Usage Tips
        - Use this tool before adding new permissions to understand existing access
        - Check the assume role policy to verify which services or roles can assume this role
        - Look for overly permissive policies that might pose security risks
        - Use with add_inline_policy to implement least-privilege permissions

        Args:
            ctx: The MCP context
            role_name: Name of the IAM role to get policies for

        Returns:
            RoleDescriptionResponse: Detailed information about the role's policies
        
---

# Get Policies For Role

Get all policies attached to an IAM role.

        This tool retrieves all policies associated with an IAM role, providing a comprehensive view
        of the role's permissions and trust relationships. It helps you understand the current
        permissions, identify missing or excessive permissions, troubleshoot EKS cluster issues,
        and verify trust relationships for service roles.

        IMPORTANT: Use this tool instead of 'aws iam get-role', 'aws iam list-attached-role-policies',
        'aws iam list-role-policies', and 'aws iam get-role-policy' commands.

        ## Requirements
        - The role must exist in your AWS account
        - Valid AWS credentials with permissions to read IAM role information

        ## Response Information
        The response includes role ARN, assume role policy document (trust relationships),
        role description, managed policies with their documents, and inline policies with
        their documents.

        ## Usage Tips
        - Use this tool before adding new permissions to understand existing access
        - Check the assume role policy to verify which services or roles can assume this role
        - Look for overly permissive policies that might pose security risks
        - Use with add_inline_policy to implement least-privilege permissions

        Args:
            ctx: The MCP context
            role_name: Name of the IAM role to get policies for

        Returns:
            RoleDescriptionResponse: Detailed information about the role's policies
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `role_name` | string | Yes | Name of the IAM role to get policies for. The role must exist in your AWS account. |

## AWS CLI

```bash
aws iam list-attached-role-policies --role-name <role_name>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.list_attached_role_policies(
    RoleName=role_name,
)
```
