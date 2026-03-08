---
name: SearchAwsProviderDocs
description: Search AWS provider documentation for resources and attributes.

    This tool searches the Terraform AWS provider documentation for information about
    a specific asset in the AWS Provider Documentation, assets can be either resources or data sources. It retrieves comprehensive details including descriptions, example code snippets, argument references, and attribute references.

    Use the 'asset_type' parameter to specify if you are looking for information about provider resources, data sources, or both. Valid values are 'resource', 'data_source' or 'both'.

    The tool will automatically handle prefixes - you can search for either 'aws_s3_bucket' or 's3_bucket'.

    Examples:
        - To get documentation for an S3 bucket resource:
          search_aws_provider_docs(asset_name='aws_s3_bucket')

        - To search only for data sources:
          search_aws_provider_docs(asset_name='aws_ami', asset_type='data_source')

        - To search for both resource and data source documentation of a given name:
          search_aws_provider_docs(asset_name='aws_instance', asset_type='both')

    Parameters:
        asset_name: Name of the service (asset) to look for (e.g., 'aws_s3_bucket', 'aws_lambda_function')
        asset_type: Type of documentation to search - 'resource' (default), 'data_source', or 'both'

    Returns:
        A list of matching documentation entries with details including:
        - Resource name and description
        - URL to the official documentation
        - Example code snippets
        - Arguments with descriptions
        - Attributes with descriptions
    
---

# Searchawsproviderdocs

Search AWS provider documentation for resources and attributes.

    This tool searches the Terraform AWS provider documentation for information about
    a specific asset in the AWS Provider Documentation, assets can be either resources or data sources. It retrieves comprehensive details including descriptions, example code snippets, argument references, and attribute references.

    Use the 'asset_type' parameter to specify if you are looking for information about provider resources, data sources, or both. Valid values are 'resource', 'data_source' or 'both'.

    The tool will automatically handle prefixes - you can search for either 'aws_s3_bucket' or 's3_bucket'.

    Examples:
        - To get documentation for an S3 bucket resource:
          search_aws_provider_docs(asset_name='aws_s3_bucket')

        - To search only for data sources:
          search_aws_provider_docs(asset_name='aws_ami', asset_type='data_source')

        - To search for both resource and data source documentation of a given name:
          search_aws_provider_docs(asset_name='aws_instance', asset_type='both')

    Parameters:
        asset_name: Name of the service (asset) to look for (e.g., 'aws_s3_bucket', 'aws_lambda_function')
        asset_type: Type of documentation to search - 'resource' (default), 'data_source', or 'both'

    Returns:
        A list of matching documentation entries with details including:
        - Resource name and description
        - URL to the official documentation
        - Example code snippets
        - Arguments with descriptions
        - Attributes with descriptions
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `asset_name` | string | Yes | Name of the AWS service (asset) to look for (e.g., "aws_s3_bucket", "aws_lambda_function") |
| `asset_type` | string | No | Type of documentation to search - 'resource' (default), 'data_source', or 'both' |

