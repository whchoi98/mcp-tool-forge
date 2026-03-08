---
name: cost-optimization
description: Retrieves cost optimization recommendations from AWS Cost Optimization Hub.

IMPORTANT USAGE GUIDELINES:
- Focus on recommendations with the highest estimated savings first
- Include all relevant details when presenting specific recommendations

USE THIS TOOL FOR:
- **Idle/unused resource detection** (EC2, RDS, EBS, Lambda, etc.)
- **Cost savings recommendations** (rightsizing, stopping, deleting resources)
- **Reserved Instance and Savings Plans purchase recommendations**
- **Cross-service cost optimization analysis**
- **Monthly cost reduction opportunities**

DO NOT USE FOR: Performance optimization (use compute-optimizer)

Supported Operations:
1. list_recommendation_summaries: High-level overview of savings opportunities grouped by a dimension
2. list_recommendations: Detailed list of specific recommendations
3. get_recommendation: Get detailed information about a specific recommendation

IMPORTANT: 'list_recommendation_summaries' operation REQUIRES a 'group_by' parameter.
Valid 'group_by' values: AccountId, Region, ActionType, ResourceType, RestartNeeded, RollbackPossible, ImplementationEffort

CRITICAL PARAMETER REQUIREMENTS:
- 'filters' parameter must be passed as JSON string format
- 'max_results' must be integer (not string)
- 'get_recommendation' requires both 'resource_id' AND 'resource_type' parameters
- Service only available in us-east-1 region

Available Filter Parameters (pass as JSON string):
- resourceTypes: ['Ec2Instance', 'LambdaFunction', 'EbsVolume', 'EcsService', 'Ec2AutoScalingGroup', 'Ec2InstanceSavingsPlans', 'ComputeSavingsPlans', 'SageMakerSavingsPlans', 'Ec2ReservedInstances', 'RdsReservedInstances', 'OpenSearchReservedInstances', 'RedshiftReservedInstances', 'ElastiCacheReservedInstances', 'RdsDbInstanceStorage', 'RdsDbInstance', 'DynamoDbReservedCapacity', 'MemoryDbReservedInstances']
- actionTypes: ['Rightsize', 'Stop', 'Upgrade', 'PurchaseSavingsPlans', 'PurchaseReservedInstances', 'MigrateToGraviton', 'Delete', 'ScaleIn']
- implementationEfforts: ['VeryLow', 'Low', 'Medium', 'High', 'VeryHigh']
- regions: AWS region codes (e.g., ["us-east-1", "us-west-2"])
- accountIds: List of AWS account IDs
- restartNeeded: boolean
- rollbackPossible: boolean

Cost Optimization Hub provides recommendations across multiple AWS services, including:
- EC2 instances (right-sizing, Graviton migration)
- EBS volumes (unused volumes, IOPS optimization)
- RDS instances (right-sizing, engine optimization)
- Lambda functions (memory size optimization)
- SP/RI
- And more

Each recommendation includes:
- The resource ARN and ID
- The estimated monthly savings
- The current state of the resource
- The recommended state of the resource

---

# Cost-Optimization

Retrieves cost optimization recommendations from AWS Cost Optimization Hub.

IMPORTANT USAGE GUIDELINES:
- Focus on recommendations with the highest estimated savings first
- Include all relevant details when presenting specific recommendations

USE THIS TOOL FOR:
- **Idle/unused resource detection** (EC2, RDS, EBS, Lambda, etc.)
- **Cost savings recommendations** (rightsizing, stopping, deleting resources)
- **Reserved Instance and Savings Plans purchase recommendations**
- **Cross-service cost optimization analysis**
- **Monthly cost reduction opportunities**

DO NOT USE FOR: Performance optimization (use compute-optimizer)

Supported Operations:
1. list_recommendation_summaries: High-level overview of savings opportunities grouped by a dimension
2. list_recommendations: Detailed list of specific recommendations
3. get_recommendation: Get detailed information about a specific recommendation

IMPORTANT: 'list_recommendation_summaries' operation REQUIRES a 'group_by' parameter.
Valid 'group_by' values: AccountId, Region, ActionType, ResourceType, RestartNeeded, RollbackPossible, ImplementationEffort

CRITICAL PARAMETER REQUIREMENTS:
- 'filters' parameter must be passed as JSON string format
- 'max_results' must be integer (not string)
- 'get_recommendation' requires both 'resource_id' AND 'resource_type' parameters
- Service only available in us-east-1 region

Available Filter Parameters (pass as JSON string):
- resourceTypes: ['Ec2Instance', 'LambdaFunction', 'EbsVolume', 'EcsService', 'Ec2AutoScalingGroup', 'Ec2InstanceSavingsPlans', 'ComputeSavingsPlans', 'SageMakerSavingsPlans', 'Ec2ReservedInstances', 'RdsReservedInstances', 'OpenSearchReservedInstances', 'RedshiftReservedInstances', 'ElastiCacheReservedInstances', 'RdsDbInstanceStorage', 'RdsDbInstance', 'DynamoDbReservedCapacity', 'MemoryDbReservedInstances']
- actionTypes: ['Rightsize', 'Stop', 'Upgrade', 'PurchaseSavingsPlans', 'PurchaseReservedInstances', 'MigrateToGraviton', 'Delete', 'ScaleIn']
- implementationEfforts: ['VeryLow', 'Low', 'Medium', 'High', 'VeryHigh']
- regions: AWS region codes (e.g., ["us-east-1", "us-west-2"])
- accountIds: List of AWS account IDs
- restartNeeded: boolean
- rollbackPossible: boolean

Cost Optimization Hub provides recommendations across multiple AWS services, including:
- EC2 instances (right-sizing, Graviton migration)
- EBS volumes (unused volumes, IOPS optimization)
- RDS instances (right-sizing, engine optimization)
- Lambda functions (memory size optimization)
- SP/RI
- And more

Each recommendation includes:
- The resource ARN and ID
- The estimated monthly savings
- The current state of the resource
- The recommended state of the resource


## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes |  |
| `resource_id` | string | No |  |
| `resource_type` | string | No |  |
| `max_results` | string | No |  |
| `filters` | string | No |  |
| `group_by` | string | No |  |
| `include_all_recommendations` | string | No |  |

## AWS CLI

```bash
aws cost-optimization-hub list-recommendations --resource-id <resource_id> --resource-type <resource_type> --max-results <max_results> --filters <filters> --group-by <group_by> --include-all-recommendations <include_all_recommendations>
```

## boto3

```python
import boto3

client = boto3.client('cost-optimization-hub')
response = client.list_recommendations(
    ResourceId=resource_id,
    ResourceType=resource_type,
    MaxResults=max_results,
    Filters=filters,
    GroupBy=group_by,
    IncludeAllRecommendations=include_all_recommendations,
)
```
