---
name: getprojects
description: Get a list of data automation projects.

    ## Usage

    Use this tool to retrieve a list of all available data automation projects in your account.
    This is typically the first step when working with data automation to discover what projects
    are available for use.

    ## Example

    ```python
    # Get all available data automation projects
    projects = await getprojects()
    ```

    ## Output Format

    The output is a dictionary containing:
    - `projects`: A list of project objects, each with:
      - `projectArn`: The Amazon Resource Name (ARN) of the project
      - `projectName`: The name of the project
      - `projectStage`: The stage of the project (e.g., DRAFT, PUBLISHED)
      - `creationTime`: When the project was created
      - `lastModifiedTime`: When the project was last modified

    Returns:
        A dict containing a list of data automation projects.
    
---

# Getprojects

Get a list of data automation projects.

    ## Usage

    Use this tool to retrieve a list of all available data automation projects in your account.
    This is typically the first step when working with data automation to discover what projects
    are available for use.

    ## Example

    ```python
    # Get all available data automation projects
    projects = await getprojects()
    ```

    ## Output Format

    The output is a dictionary containing:
    - `projects`: A list of project objects, each with:
      - `projectArn`: The Amazon Resource Name (ARN) of the project
      - `projectName`: The name of the project
      - `projectStage`: The stage of the project (e.g., DRAFT, PUBLISHED)
      - `creationTime`: When the project was created
      - `lastModifiedTime`: When the project was last modified

    Returns:
        A dict containing a list of data automation projects.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

## AWS CLI

```bash
aws bedrock list-projects
```

## boto3

```python
import boto3

client = boto3.client('bedrock')
response = client.list_projects(
)
```
