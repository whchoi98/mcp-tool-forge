---
name: finch-create-ecr-repo
description: Check if an ECR repository exists and create it if it doesn't.

    This tool checks if the specified ECR repository exists using boto3.
    If the repository doesn't exist, it creates a new one with the given name.
    The tool requires appropriate AWS credentials configured.

    When the server is in read-only mode (which is the default unless --enable-aws-resource-write
    is specified), this tool will return an error and will not create any repositories.

    Returns:
        Result: An object containing:
            - status (str): "success" if the operation succeeded, "error" otherwise
            - message (str): A descriptive message about the result of the operation

    Example response:
        Result(status="success", message="Successfully created ECR repository 'my-app'.",
               repository_uri="123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app",
               exists=False)

    
---

# Finch Create Ecr Repo

Check if an ECR repository exists and create it if it doesn't.

    This tool checks if the specified ECR repository exists using boto3.
    If the repository doesn't exist, it creates a new one with the given name.
    The tool requires appropriate AWS credentials configured.

    When the server is in read-only mode (which is the default unless --enable-aws-resource-write
    is specified), this tool will return an error and will not create any repositories.

    Returns:
        Result: An object containing:
            - status (str): "success" if the operation succeeded, "error" otherwise
            - message (str): A descriptive message about the result of the operation

    Example response:
        Result(status="success", message="Successfully created ECR repository 'my-app'.",
               repository_uri="123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app",
               exists=False)

    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `repository_name` | string | Yes | The name of the repository to check or create in ECR |
| `region` | string | No | AWS region for the ECR repository. If not provided, uses the default region from AWS configuration |

