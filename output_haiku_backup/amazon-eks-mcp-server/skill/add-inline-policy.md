---
name: add-inline-policy
description: Add a new inline policy to an IAM role.

        This tool creates a new inline policy with the specified permissions and adds it to an IAM role.
        Inline policies are embedded within the role and cannot be attached to multiple roles. Commonly used
        for granting EKS clusters access to AWS services, enabling worker nodes to access resources, and
        configuring permissions for CloudWatch logging and ECR access.

        IMPORTANT: Use this tool instead of 'aws iam put-role-policy' commands.

        ## Requirements
        - The server must be run with the `--allow-write` flag
        - The role must exist in your AWS account
        - The policy name must be unique within the role
        - You cannot modify existing policies with this tool

        ## Permission Format
        The permissions parameter can be either a single policy statement or a list of statements.

        ### Single Statement Example
        ```json
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject"],
            "Resource": "arn:aws:s3:::example-bucket/*"
        }
        ```

        ## Usage Tips
        - Follow the principle of least privilege by granting only necessary permissions
        - Use specific resources rather than "*" whenever possible
        - Consider using conditions to further restrict permissions
        - Group related permissions into logical policies with descriptive names

        Args:
            ctx: The MCP context
            policy_name: Name of the new inline policy to create
            role_name: Name of the role to add the policy to
            permissions: Permissions to include in the policy (in JSON format)

        Returns:
            AddInlinePolicyResponse: Information about the created policy
        
---

# Add Inline Policy

Add a new inline policy to an IAM role.

        This tool creates a new inline policy with the specified permissions and adds it to an IAM role.
        Inline policies are embedded within the role and cannot be attached to multiple roles. Commonly used
        for granting EKS clusters access to AWS services, enabling worker nodes to access resources, and
        configuring permissions for CloudWatch logging and ECR access.

        IMPORTANT: Use this tool instead of 'aws iam put-role-policy' commands.

        ## Requirements
        - The server must be run with the `--allow-write` flag
        - The role must exist in your AWS account
        - The policy name must be unique within the role
        - You cannot modify existing policies with this tool

        ## Permission Format
        The permissions parameter can be either a single policy statement or a list of statements.

        ### Single Statement Example
        ```json
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject"],
            "Resource": "arn:aws:s3:::example-bucket/*"
        }
        ```

        ## Usage Tips
        - Follow the principle of least privilege by granting only necessary permissions
        - Use specific resources rather than "*" whenever possible
        - Consider using conditions to further restrict permissions
        - Group related permissions into logical policies with descriptive names

        Args:
            ctx: The MCP context
            policy_name: Name of the new inline policy to create
            role_name: Name of the role to add the policy to
            permissions: Permissions to include in the policy (in JSON format)

        Returns:
            AddInlinePolicyResponse: Information about the created policy
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `policy_name` | string | Yes | Name of the inline policy to create. Must be unique within the role. |
| `role_name` | string | Yes | Name of the IAM role to add the policy to. The role must exist. |
| `permissions` | string | Yes | Permissions to include in the policy as IAM policy statements in JSON format.
            Can be either a single statement object or an array of statement objects. |

## AWS CLI

```bash
aws iam put-role-policy --role-name <role_name> --policy-name <policy_name> --policy-document <permissions>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.put_role_policy(
    RoleName=role_name,
    PolicyName=policy_name,
    PolicyDocument=permissions,
)
```
