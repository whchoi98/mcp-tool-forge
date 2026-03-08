---
name: compute-optimizer
description: Retrieves recommendations from AWS Compute Optimizer.

IMPORTANT USAGE GUIDELINES:
- Focus on recommendations with the highest estimated savings first
- Include all relevant details when presenting specific recommendations

USE THIS TOOL FOR:
- **Performance optimization** (CPU, memory, network utilization analysis)
- **Performance-based rightsizing** (not cost-based)

DO NOT USE FOR: Cost optimization or idle detection (use cost-optimization-hub)

This tool supports the following operations:
1. get_ec2_instance_recommendations: Get recommendations for EC2 instances
2. get_auto_scaling_group_recommendations: Get recommendations for Auto Scaling groups
3. get_ebs_volume_recommendations: Get recommendations for EBS volumes
4. get_lambda_function_recommendations: Get recommendations for Lambda functions
5. get_rds_recommendations: Get recommendations for RDS instances
6. get_ecs_service_recommendations: Get recommendations for ECS services

Each operation can be filtered by AWS account IDs, regions, finding types, and more.

Common finding types include:
- UNDERPROVISIONED: The resource doesn't have enough capacity
- OVERPROVISIONED: The resource has excess capacity and could be downsized
- OPTIMIZED: The resource is already optimized
- NOT_OPTIMIZED: The resource can be optimized but specific finding type isn't available
---

# Compute-Optimizer

Retrieves recommendations from AWS Compute Optimizer.

IMPORTANT USAGE GUIDELINES:
- Focus on recommendations with the highest estimated savings first
- Include all relevant details when presenting specific recommendations

USE THIS TOOL FOR:
- **Performance optimization** (CPU, memory, network utilization analysis)
- **Performance-based rightsizing** (not cost-based)

DO NOT USE FOR: Cost optimization or idle detection (use cost-optimization-hub)

This tool supports the following operations:
1. get_ec2_instance_recommendations: Get recommendations for EC2 instances
2. get_auto_scaling_group_recommendations: Get recommendations for Auto Scaling groups
3. get_ebs_volume_recommendations: Get recommendations for EBS volumes
4. get_lambda_function_recommendations: Get recommendations for Lambda functions
5. get_rds_recommendations: Get recommendations for RDS instances
6. get_ecs_service_recommendations: Get recommendations for ECS services

Each operation can be filtered by AWS account IDs, regions, finding types, and more.

Common finding types include:
- UNDERPROVISIONED: The resource doesn't have enough capacity
- OVERPROVISIONED: The resource has excess capacity and could be downsized
- OPTIMIZED: The resource is already optimized
- NOT_OPTIMIZED: The resource can be optimized but specific finding type isn't available

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operation` | string | Yes |  |
| `max_results` | string | No |  |
| `filters` | string | No |  |
| `account_ids` | string | No |  |
| `next_token` | string | No |  |

## AWS CLI

```bash
aws compute-optimizer get-ec2-instance-recommendations --max-results <max_results> --filters <filters> --account-ids <account_ids> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('compute-optimizer')
response = client.get_ec2_instance_recommendations(
    MaxResults=max_results,
    Filters=filters,
    AccountIds=account_ids,
    NextToken=next_token,
)
```
