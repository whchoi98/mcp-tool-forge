---
name: CreateAHOWorkflowVersion
description: Create a new version of an existing workflow.

    Args:
        ctx: MCP context for error reporting
        workflow_id: ID of the workflow
        version_name: Name for the new version
        definition_zip_base64: Base64-encoded workflow definition ZIP file. Cannot be used together with definition_uri or definition_repository
        description: Optional description of the workflow version
        parameter_template: Optional parameter template for the workflow
        storage_type: Storage type (STATIC or DYNAMIC)
        storage_capacity: Storage capacity in GB (required for STATIC)
        container_registry_map: Optional container registry map with registryMappings (upstreamRegistryUrl, ecrRepositoryPrefix, upstreamRepositoryPrefix, ecrAccountId) and imageMappings (sourceImage, destinationImage) arrays
        container_registry_map_uri: Optional S3 URI pointing to a JSON file containing container registry mappings. Cannot be used together with container_registry_map
        definition_uri: S3 URI of the workflow definition ZIP file. Cannot be used together with definition_zip_base64 or definition_repository
        path_to_main: Path to the main file in the workflow definition ZIP file. Not required if there is a top level main.wdl, main.cwl or main.nf files in the workflow package. Not required if there is only a single top level workflow file.
        readme: README documentation - can be markdown content, local .md file path, or S3 URI (s3://bucket/key)
        definition_repository: Git repository configuration with connection_arn, full_repository_id, source_reference, and optional exclude_file_patterns
        parameter_template_path: Path to parameter template JSON file within the repository (only valid with definition_repository)
        readme_path: Path to README markdown file within the repository (only valid with definition_repository)

    Returns:
        Dictionary containing the created workflow version information
    
---

# Createahoworkflowversion

Create a new version of an existing workflow.

    Args:
        ctx: MCP context for error reporting
        workflow_id: ID of the workflow
        version_name: Name for the new version
        definition_zip_base64: Base64-encoded workflow definition ZIP file. Cannot be used together with definition_uri or definition_repository
        description: Optional description of the workflow version
        parameter_template: Optional parameter template for the workflow
        storage_type: Storage type (STATIC or DYNAMIC)
        storage_capacity: Storage capacity in GB (required for STATIC)
        container_registry_map: Optional container registry map with registryMappings (upstreamRegistryUrl, ecrRepositoryPrefix, upstreamRepositoryPrefix, ecrAccountId) and imageMappings (sourceImage, destinationImage) arrays
        container_registry_map_uri: Optional S3 URI pointing to a JSON file containing container registry mappings. Cannot be used together with container_registry_map
        definition_uri: S3 URI of the workflow definition ZIP file. Cannot be used together with definition_zip_base64 or definition_repository
        path_to_main: Path to the main file in the workflow definition ZIP file. Not required if there is a top level main.wdl, main.cwl or main.nf files in the workflow package. Not required if there is only a single top level workflow file.
        readme: README documentation - can be markdown content, local .md file path, or S3 URI (s3://bucket/key)
        definition_repository: Git repository configuration with connection_arn, full_repository_id, source_reference, and optional exclude_file_patterns
        parameter_template_path: Path to parameter template JSON file within the repository (only valid with definition_repository)
        readme_path: Path to README markdown file within the repository (only valid with definition_repository)

    Returns:
        Dictionary containing the created workflow version information
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `workflow_id` | string | Yes | ID of the workflow |
| `version_name` | string | Yes | Name for the new version |
| `definition_zip_base64` | string | No | Base64-encoded workflow definition ZIP file. Cannot be used together with definition_uri or definition_repository |
| `description` | string | No | Optional description of the workflow version |
| `parameter_template` | string | No | Optional parameter template for the workflow |
| `storage_type` | string | No | Storage type (STATIC or DYNAMIC) |
| `storage_capacity` | string | No | Storage capacity in GB (required for STATIC) |
| `container_registry_map` | string | No | Optional container registry map with registryMappings (upstreamRegistryUrl, ecrRepositoryPrefix, upstreamRepositoryPrefix, ecrAccountId) and imageMappings (sourceImage, destinationImage) arrays |
| `container_registry_map_uri` | string | No | Optional S3 URI pointing to a JSON file containing container registry mappings. Cannot be used together with container_registry_map |
| `definition_uri` | string | No | S3 URI of the workflow definition ZIP file. Cannot be used together with definition_zip_base64 or definition_repository |
| `path_to_main` | string | No | Path to the main file in the workflow definition ZIP file. Not required if there is a top level main.wdl, main.cwl or main.nf files in the workflow package. Not required if there is only a single top level workflow file. |
| `readme` | string | No | README documentation: markdown content, local .md file path, or S3 URI (s3://bucket/key) |
| `definition_repository` | string | No | Git repository configuration with connection_arn, full_repository_id, source_reference (type and value), and optional exclude_file_patterns. Cannot be used together with definition_zip_base64 or definition_uri |
| `parameter_template_path` | string | No | Path to parameter template JSON file within the repository (only valid with definition_repository) |
| `readme_path` | string | No | Path to README markdown file within the repository (only valid with definition_repository) |

## AWS CLI

```bash
aws omics create-workflow-version --workflow-id <workflow_id> --name <version_name> --definition-zip <definition_zip_base64> --description <description> --parameter-template <parameter_template> --storage-type <storage_type> --storage-capacity <storage_capacity> --definition-uri <definition_uri> --container-registry-map <container_registry_map> --container-registry-map-uri <container_registry_map_uri> --path-to-main <path_to_main> --readme <readme>
```

## boto3

```python
import boto3

client = boto3.client('omics')
response = client.create_workflow_version(
    WorkflowId=workflow_id,
    Name=version_name,
    DefinitionZip=definition_zip_base64,
    Description=description,
    ParameterTemplate=parameter_template,
    StorageType=storage_type,
    StorageCapacity=storage_capacity,
    DefinitionUri=definition_uri,
    ContainerRegistryMap=container_registry_map,
    ContainerRegistryMapUri=container_registry_map_uri,
    PathToMain=path_to_main,
    Readme=readme,
)
```
