---
name: ecs-resource-management
description: Execute ECS API operations directly.

This tool allows direct execution of ECS API operations using boto3.

Supported operations:
- CreateCapacityProvider (requires WRITE permission)
- CreateCluster (requires WRITE permission)
- CreateExpressGatewayService (requires WRITE permission)
- CreateService (requires WRITE permission)
- CreateTaskSet (requires WRITE permission)
- DeleteAccountSetting (requires WRITE permission)
- DeleteAttributes (requires WRITE permission)
- DeleteCapacityProvider (requires WRITE permission)
- DeleteCluster (requires WRITE permission)
- DeleteExpressGatewayService (requires WRITE permission)
- DeleteService (requires WRITE permission)
- DeleteTaskDefinitions (requires WRITE permission)
- DeleteTaskSet (requires WRITE permission)
- DeregisterContainerInstance (requires WRITE permission)
- DeregisterTaskDefinition (requires WRITE permission)
- DescribeCapacityProviders (read-only)
- DescribeClusters (read-only)
- DescribeContainerInstances (read-only)
- DescribeExpressGatewayService (read-only)
- DescribeServiceDeployments (read-only)
- DescribeServiceRevisions (read-only)
- DescribeServices (read-only)
- DescribeTaskDefinition (read-only)
- DescribeTasks (read-only)
- DescribeTaskSets (read-only)
- DiscoverPollEndpoint (requires WRITE permission)
- ExecuteCommand (requires WRITE permission)
- GetTaskProtection (requires WRITE permission)
- ListAccountSettings (read-only)
- ListAttributes (read-only)
- ListClusters (read-only)
- ListContainerInstances (read-only)
- ListExpressGatewayServices (read-only)
- ListServiceDeployments (read-only)
- ListServices (read-only)
- ListServicesByNamespace (read-only)
- ListTagsForResource (read-only)
- ListTaskDefinitionFamilies (read-only)
- ListTaskDefinitions (read-only)
- ListTasks (read-only)
- PutAccountSetting (requires WRITE permission)
- PutAccountSettingDefault (requires WRITE permission)
- PutAttributes (requires WRITE permission)
- PutClusterCapacityProviders (requires WRITE permission)
- RegisterContainerInstance (requires WRITE permission)
- RegisterTaskDefinition (requires WRITE permission)
- RunTask (requires WRITE permission)
- StartTask (requires WRITE permission)
- StopServiceDeployment (requires WRITE permission)
- StopTask (requires WRITE permission)
- SubmitAttachmentStateChanges (requires WRITE permission)
- SubmitContainerStateChange (requires WRITE permission)
- SubmitTaskStateChange (requires WRITE permission)
- TagResource (requires WRITE permission)
- UntagResource (requires WRITE permission)
- UpdateCapacityProvider (requires WRITE permission)
- UpdateCluster (requires WRITE permission)
- UpdateClusterSettings (requires WRITE permission)
- UpdateContainerAgent (requires WRITE permission)
- UpdateContainerInstancesState (requires WRITE permission)
- UpdateExpressGatewayService (requires WRITE permission)
- UpdateService (requires WRITE permission)
- UpdateServicePrimaryTaskSet (requires WRITE permission)
- UpdateTaskProtection (requires WRITE permission)
- UpdateTaskSet (requires WRITE permission)

Parameters:
    api_operation: The ECS API operation to execute (CamelCase)
    api_params: Dictionary of parameters to pass to the API operation

Returns:
    Dictionary containing the API response
---

# Ecs Resource Management

Execute ECS API operations directly.

This tool allows direct execution of ECS API operations using boto3.

Supported operations:
- CreateCapacityProvider (requires WRITE permission)
- CreateCluster (requires WRITE permission)
- CreateExpressGatewayService (requires WRITE permission)
- CreateService (requires WRITE permission)
- CreateTaskSet (requires WRITE permission)
- DeleteAccountSetting (requires WRITE permission)
- DeleteAttributes (requires WRITE permission)
- DeleteCapacityProvider (requires WRITE permission)
- DeleteCluster (requires WRITE permission)
- DeleteExpressGatewayService (requires WRITE permission)
- DeleteService (requires WRITE permission)
- DeleteTaskDefinitions (requires WRITE permission)
- DeleteTaskSet (requires WRITE permission)
- DeregisterContainerInstance (requires WRITE permission)
- DeregisterTaskDefinition (requires WRITE permission)
- DescribeCapacityProviders (read-only)
- DescribeClusters (read-only)
- DescribeContainerInstances (read-only)
- DescribeExpressGatewayService (read-only)
- DescribeServiceDeployments (read-only)
- DescribeServiceRevisions (read-only)
- DescribeServices (read-only)
- DescribeTaskDefinition (read-only)
- DescribeTasks (read-only)
- DescribeTaskSets (read-only)
- DiscoverPollEndpoint (requires WRITE permission)
- ExecuteCommand (requires WRITE permission)
- GetTaskProtection (requires WRITE permission)
- ListAccountSettings (read-only)
- ListAttributes (read-only)
- ListClusters (read-only)
- ListContainerInstances (read-only)
- ListExpressGatewayServices (read-only)
- ListServiceDeployments (read-only)
- ListServices (read-only)
- ListServicesByNamespace (read-only)
- ListTagsForResource (read-only)
- ListTaskDefinitionFamilies (read-only)
- ListTaskDefinitions (read-only)
- ListTasks (read-only)
- PutAccountSetting (requires WRITE permission)
- PutAccountSettingDefault (requires WRITE permission)
- PutAttributes (requires WRITE permission)
- PutClusterCapacityProviders (requires WRITE permission)
- RegisterContainerInstance (requires WRITE permission)
- RegisterTaskDefinition (requires WRITE permission)
- RunTask (requires WRITE permission)
- StartTask (requires WRITE permission)
- StopServiceDeployment (requires WRITE permission)
- StopTask (requires WRITE permission)
- SubmitAttachmentStateChanges (requires WRITE permission)
- SubmitContainerStateChange (requires WRITE permission)
- SubmitTaskStateChange (requires WRITE permission)
- TagResource (requires WRITE permission)
- UntagResource (requires WRITE permission)
- UpdateCapacityProvider (requires WRITE permission)
- UpdateCluster (requires WRITE permission)
- UpdateClusterSettings (requires WRITE permission)
- UpdateContainerAgent (requires WRITE permission)
- UpdateContainerInstancesState (requires WRITE permission)
- UpdateExpressGatewayService (requires WRITE permission)
- UpdateService (requires WRITE permission)
- UpdateServicePrimaryTaskSet (requires WRITE permission)
- UpdateTaskProtection (requires WRITE permission)
- UpdateTaskSet (requires WRITE permission)

Parameters:
    api_operation: The ECS API operation to execute (CamelCase)
    api_params: Dictionary of parameters to pass to the API operation

Returns:
    Dictionary containing the API response

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `api_operation` | string | Yes | The ECS API operation to execute (CamelCase) |
| `api_params` | object | No | Dictionary of parameters to pass to the API operation |

## AWS CLI

```bash
aws ecs --operation <api_operation>
```

## boto3

```python
import boto3

client = boto3.client('ecs')
response = client.api_operation(
    ApiOperation=api_operation,
    Params=api_params,
)
```
