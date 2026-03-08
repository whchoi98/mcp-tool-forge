---
name: analyzeasset
description: Analyze an asset using a data automation project.

    This tool extracts insights from unstructured content (documents, images, videos, audio)
    using Amazon Bedrock Data Automation.

    ## Usage

    Use this tool to analyze various types of assets (documents, images, videos, audio files)
    using a data automation project. You can specify a particular project to use for analysis
    or let the system use a default public project if none is provided.

    ## Supported Asset Types

    - Documents: PDF, DOCX, TXT, etc.
    - Images: JPG, PNG, etc.
    - Videos: MP4, MOV, etc.
    - Audio: MP3, WAV, etc.

    ## Examples

    ```python
    # Analyze a document using the default public project
    results = await analyzeasset(assetPath='/path/to/document.pdf')

    # Analyze an image using a specific project
    results = await analyzeasset(
        assetPath='/path/to/image.jpg',
        projectArn='arn:aws:bedrock:us-west-2:123456789012:data-automation-project/my-project',
    )
    ```

    ## Output Format

    The output is a dictionary containing the analysis results, which vary based on:
    - The type of asset being analyzed
    - The capabilities of the data automation project used
    - The specific insights extracted (text, entities, sentiment, etc.)

    Args:
        assetPath: The path to the asset.
        projectArn: The ARN of the project. Uses default public project if not provided.

    Returns:
        The analysis results.
    
---

# Analyzeasset

Analyze an asset using a data automation project.

    This tool extracts insights from unstructured content (documents, images, videos, audio)
    using Amazon Bedrock Data Automation.

    ## Usage

    Use this tool to analyze various types of assets (documents, images, videos, audio files)
    using a data automation project. You can specify a particular project to use for analysis
    or let the system use a default public project if none is provided.

    ## Supported Asset Types

    - Documents: PDF, DOCX, TXT, etc.
    - Images: JPG, PNG, etc.
    - Videos: MP4, MOV, etc.
    - Audio: MP3, WAV, etc.

    ## Examples

    ```python
    # Analyze a document using the default public project
    results = await analyzeasset(assetPath='/path/to/document.pdf')

    # Analyze an image using a specific project
    results = await analyzeasset(
        assetPath='/path/to/image.jpg',
        projectArn='arn:aws:bedrock:us-west-2:123456789012:data-automation-project/my-project',
    )
    ```

    ## Output Format

    The output is a dictionary containing the analysis results, which vary based on:
    - The type of asset being analyzed
    - The capabilities of the data automation project used
    - The specific insights extracted (text, entities, sentiment, etc.)

    Args:
        assetPath: The path to the asset.
        projectArn: The ARN of the project. Uses default public project if not provided.

    Returns:
        The analysis results.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assetPath` | string | Yes | The path to the asset |
| `projectArn` | string | No | The ARN of the project. Uses default public project if not provided |

## AWS CLI

```bash
aws bedrock analyze-asset --asset-path <assetPath> --project-arn <projectArn>
```

## boto3

```python
import boto3

client = boto3.client('bedrock')
response = client.analyze_asset(
    AssetPath=assetPath,
    ProjectArn=projectArn,
)
```
