---
name: SearchSpecificAwsIaModules
description: Search for specific AWS-IA Terraform modules.

    This tool checks for information about four specific AWS-IA modules:
    - aws-ia/bedrock/aws - Amazon Bedrock module for generative AI applications
    - aws-ia/opensearch-serverless/aws - OpenSearch Serverless collection for vector search
    - aws-ia/sagemaker-endpoint/aws - SageMaker endpoint deployment module
    - aws-ia/serverless-streamlit-app/aws - Serverless Streamlit application deployment

    It returns detailed information about these modules, including their README content,
    variables.tf content, and submodules when available.

    The search is performed across module names, descriptions, README content, and variable
    definitions. This allows you to find modules based on their functionality or specific
    configuration options.

    Examples:
        - To get information about all four modules:
          search_specific_aws_ia_modules()

        - To find modules related to Bedrock:
          search_specific_aws_ia_modules(query='bedrock')

        - To find modules related to vector search:
          search_specific_aws_ia_modules(query='vector search')

        - To find modules with specific configuration options:
          search_specific_aws_ia_modules(query='endpoint_name')

    Parameters:
        query: Optional search term to filter modules (empty returns all four modules)

    Returns:
        A list of matching modules with their details, including:
        - Basic module information (name, namespace, version)
        - Module documentation (README content)
        - Input and output parameter counts
        - Variables from variables.tf with descriptions and default values
        - Submodules information
        - Version details and release information
    
---

# Searchspecificawsiamodules

Search for specific AWS-IA Terraform modules.

    This tool checks for information about four specific AWS-IA modules:
    - aws-ia/bedrock/aws - Amazon Bedrock module for generative AI applications
    - aws-ia/opensearch-serverless/aws - OpenSearch Serverless collection for vector search
    - aws-ia/sagemaker-endpoint/aws - SageMaker endpoint deployment module
    - aws-ia/serverless-streamlit-app/aws - Serverless Streamlit application deployment

    It returns detailed information about these modules, including their README content,
    variables.tf content, and submodules when available.

    The search is performed across module names, descriptions, README content, and variable
    definitions. This allows you to find modules based on their functionality or specific
    configuration options.

    Examples:
        - To get information about all four modules:
          search_specific_aws_ia_modules()

        - To find modules related to Bedrock:
          search_specific_aws_ia_modules(query='bedrock')

        - To find modules related to vector search:
          search_specific_aws_ia_modules(query='vector search')

        - To find modules with specific configuration options:
          search_specific_aws_ia_modules(query='endpoint_name')

    Parameters:
        query: Optional search term to filter modules (empty returns all four modules)

    Returns:
        A list of matching modules with their details, including:
        - Basic module information (name, namespace, version)
        - Module documentation (README content)
        - Input and output parameter counts
        - Variables from variables.tf with descriptions and default values
        - Submodules information
        - Version details and release information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | Yes | Optional search term to filter modules (empty returns all four modules) |

