---
name: getprojectdetails
description: Get details of a data automation project.

    ## Usage

    Use this tool to retrieve detailed information about a specific data automation project
    after you've identified its ARN using the `getprojects` tool.

    ## Example

    ```python
    # Get details for a specific project
    project_details = await getprojectdetails(
        projectArn='arn:aws:bedrock:us-west-2:123456789012:data-automation-project/my-project'
    )
    ```

    ## Output Format

    The output is a dictionary containing comprehensive project details including:
    - Basic project information (name, ARN, stage)
    - Configuration settings
    - Input/output specifications
    - Associated blueprints
    - Creation and modification timestamps

    Args:
        projectArn: The ARN of the project.

    Returns:
        The project details.
    
---

# Getprojectdetails

Get details of a data automation project.

    ## Usage

    Use this tool to retrieve detailed information about a specific data automation project
    after you've identified its ARN using the `getprojects` tool.

    ## Example

    ```python
    # Get details for a specific project
    project_details = await getprojectdetails(
        projectArn='arn:aws:bedrock:us-west-2:123456789012:data-automation-project/my-project'
    )
    ```

    ## Output Format

    The output is a dictionary containing comprehensive project details including:
    - Basic project information (name, ARN, stage)
    - Configuration settings
    - Input/output specifications
    - Associated blueprints
    - Creation and modification timestamps

    Args:
        projectArn: The ARN of the project.

    Returns:
        The project details.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `projectArn` | string | Yes | The ARN of the project |

## AWS CLI

```bash
aws bedrock get-project --project-arn <projectArn>
```

## boto3

```python
import boto3

client = boto3.client('bedrock')
response = client.get_project(
    ProjectArn=projectArn,
)
```
