---
name: SearchAwsccProviderDocs
description: Search AWSCC provider documentation for resources and attributes.

    The AWSCC provider is based on the AWS Cloud Control API
    and provides a more consistent interface to AWS resources compared to the standard AWS provider.

    This tool searches the Terraform AWSCC provider documentation for information about
    a specific asset in the AWSCC Provider Documentation, assets can be either resources or data sources. It retrieves comprehensive details including descriptions, example code snippets, and schema references.

    Use the 'asset_type' parameter to specify if you are looking for information about provider resources, data sources, or both. Valid values are 'resource', 'data_source' or 'both'.

    The tool will automatically handle prefixes - you can search for either 'awscc_s3_bucket' or 's3_bucket'.

    Examples:
        - To get documentation for an S3 bucket resource:
          search_awscc_provider_docs(asset_name='awscc_s3_bucket')
          search_awscc_provider_docs(asset_name='awscc_s3_bucket', asset_type='resource')

        - To search only for data sources:
          search_aws_provider_docs(asset_name='awscc_appsync_api', kind='data_source')

        - To search for both resource and data source documentation of a given name:
          search_aws_provider_docs(asset_name='awscc_appsync_api', kind='both')

        - Search of a resource without the prefix:
          search_awscc_provider_docs(resource_type='ec2_instance')

    Parameters:
        asset_name: Name of the AWSCC Provider resource or data source to look for (e.g., 'awscc_s3_bucket', 'awscc_lambda_function')
        asset_type: Type of documentation to search - 'resource' (default), 'data_source', or 'both'. Some resources and data sources share the same name

    Returns:
        A list of matching documentation entries with details including:
        - Resource name and description
        - URL to the official documentation
        - Example code snippets
        - Schema information (required, optional, read-only, and nested structures attributes)
    
---

# Searchawsccproviderdocs

Search AWSCC provider documentation for resources and attributes.

    The AWSCC provider is based on the AWS Cloud Control API
    and provides a more consistent interface to AWS resources compared to the standard AWS provider.

    This tool searches the Terraform AWSCC provider documentation for information about
    a specific asset in the AWSCC Provider Documentation, assets can be either resources or data sources. It retrieves comprehensive details including descriptions, example code snippets, and schema references.

    Use the 'asset_type' parameter to specify if you are looking for information about provider resources, data sources, or both. Valid values are 'resource', 'data_source' or 'both'.

    The tool will automatically handle prefixes - you can search for either 'awscc_s3_bucket' or 's3_bucket'.

    Examples:
        - To get documentation for an S3 bucket resource:
          search_awscc_provider_docs(asset_name='awscc_s3_bucket')
          search_awscc_provider_docs(asset_name='awscc_s3_bucket', asset_type='resource')

        - To search only for data sources:
          search_aws_provider_docs(asset_name='awscc_appsync_api', kind='data_source')

        - To search for both resource and data source documentation of a given name:
          search_aws_provider_docs(asset_name='awscc_appsync_api', kind='both')

        - Search of a resource without the prefix:
          search_awscc_provider_docs(resource_type='ec2_instance')

    Parameters:
        asset_name: Name of the AWSCC Provider resource or data source to look for (e.g., 'awscc_s3_bucket', 'awscc_lambda_function')
        asset_type: Type of documentation to search - 'resource' (default), 'data_source', or 'both'. Some resources and data sources share the same name

    Returns:
        A list of matching documentation entries with details including:
        - Resource name and description
        - URL to the official documentation
        - Example code snippets
        - Schema information (required, optional, read-only, and nested structures attributes)
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `asset_name` | string | Yes | Name of the AWSCC service (asset) to look for (e.g., awscc_s3_bucket, awscc_lambda_function) |
| `asset_type` | string | No | Type of documentation to search - 'resource' (default), 'data_source', or 'both' |

