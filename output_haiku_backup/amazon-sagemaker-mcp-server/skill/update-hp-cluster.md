---
name: update-hp-cluster
description: Update a SageMaker HyperPod clusters.

        Notes:
            - before using this tool, ensure you first have the most recent cluster instance group configurations by first calling the describe_hp_cluster tool first.
            - modify the instance group configuration based on user's request
            - important: Use "InstanceCount" (NOT "CurrentCount" or "TargetCount") for desired target count
            - pass the configuration back in the instance group parameter
            - IMPORTANT: if user wants to do scheduled updates for their cluster nodes/AMI, also add the ScheduledUpdateConfig configs for the instance group they specified; the scheduled update time can be one-time or recurring based on user provided valid cron experssion;Times are in the UTC-00:00 time zone.
             - example cron expressions for parameter ScheduleExpression - cron(Minutes Hours Day-of-month Month Day-of-week Year)
              - one-time update on December 25, 2025 at 2:00 AM UTC: cron(0 2 25 12 ? 2025)
              - First day of every month at midnight UTC: cron(0 0 1 * ? *)
              - Every Saturday at 4:30 AM UTC: cron(30 4 ? * SAT *)
            - example instance groups parameter
            "instance_groups": [
        ⋮        {
        ⋮          "OverrideVpcConfig": {
        ⋮            "SecurityGroupIds": [
        ⋮              "<>"
        ⋮            ],
        ⋮            "Subnets": [
        ⋮              "<>"
        ⋮            ]
        ⋮          },
        ⋮          "InstanceCount": <>,
        ⋮          "InstanceGroupName": "<>",
        ⋮          "InstanceStorageConfigs": [
        ⋮            {
        ⋮              "EbsVolumeConfig": {
        ⋮                "VolumeSizeInGB": <>
        ⋮              }
        ⋮            }
        ⋮          ],
        ⋮          "LifeCycleConfig": {
        ⋮            "SourceS3Uri": "<>",
        ⋮            "OnCreate": "<>"
        ⋮          },
        ⋮          "InstanceType": "<>",
        ⋮          "ThreadsPerCore": <>,
        ⋮          "ExecutionRole": "<>"
        ⋮        }
        ⋮      ],

        ## Fallback Options:
        - If this tool fails, advise using AWS SageMaker CLI option: `aws sagemaker update-cluster  --region <cluster_region>` with all appropriate parameters
        - Or as another alternative, advise making updates directly in the SageMaker HyperPod console (Amazon SageMaker AI → HyperPod Clusters → Cluster Management → select cluster → Edit)
        - To verify results: use CLI `aws sagemaker describe-cluster --cluster-name <name>` or directly verify in console

        Args:
            ctx: MCP context
            cluster_name: REQUIRED: cluster name to update
            instance_groups: REQUIRED: instance group configurations
            region_name: REQUIRED - AWS region name
            profile_name: AWS profile name (optional)

        Returns:
            update cluster response
        
---

# Update Hp Cluster

Update a SageMaker HyperPod clusters.

        Notes:
            - before using this tool, ensure you first have the most recent cluster instance group configurations by first calling the describe_hp_cluster tool first.
            - modify the instance group configuration based on user's request
            - important: Use "InstanceCount" (NOT "CurrentCount" or "TargetCount") for desired target count
            - pass the configuration back in the instance group parameter
            - IMPORTANT: if user wants to do scheduled updates for their cluster nodes/AMI, also add the ScheduledUpdateConfig configs for the instance group they specified; the scheduled update time can be one-time or recurring based on user provided valid cron experssion;Times are in the UTC-00:00 time zone.
             - example cron expressions for parameter ScheduleExpression - cron(Minutes Hours Day-of-month Month Day-of-week Year)
              - one-time update on December 25, 2025 at 2:00 AM UTC: cron(0 2 25 12 ? 2025)
              - First day of every month at midnight UTC: cron(0 0 1 * ? *)
              - Every Saturday at 4:30 AM UTC: cron(30 4 ? * SAT *)
            - example instance groups parameter
            "instance_groups": [
        ⋮        {
        ⋮          "OverrideVpcConfig": {
        ⋮            "SecurityGroupIds": [
        ⋮              "<>"
        ⋮            ],
        ⋮            "Subnets": [
        ⋮              "<>"
        ⋮            ]
        ⋮          },
        ⋮          "InstanceCount": <>,
        ⋮          "InstanceGroupName": "<>",
        ⋮          "InstanceStorageConfigs": [
        ⋮            {
        ⋮              "EbsVolumeConfig": {
        ⋮                "VolumeSizeInGB": <>
        ⋮              }
        ⋮            }
        ⋮          ],
        ⋮          "LifeCycleConfig": {
        ⋮            "SourceS3Uri": "<>",
        ⋮            "OnCreate": "<>"
        ⋮          },
        ⋮          "InstanceType": "<>",
        ⋮          "ThreadsPerCore": <>,
        ⋮          "ExecutionRole": "<>"
        ⋮        }
        ⋮      ],

        ## Fallback Options:
        - If this tool fails, advise using AWS SageMaker CLI option: `aws sagemaker update-cluster  --region <cluster_region>` with all appropriate parameters
        - Or as another alternative, advise making updates directly in the SageMaker HyperPod console (Amazon SageMaker AI → HyperPod Clusters → Cluster Management → select cluster → Edit)
        - To verify results: use CLI `aws sagemaker describe-cluster --cluster-name <name>` or directly verify in console

        Args:
            ctx: MCP context
            cluster_name: REQUIRED: cluster name to update
            instance_groups: REQUIRED: instance group configurations
            region_name: REQUIRED - AWS region name
            profile_name: AWS profile name (optional)

        Returns:
            update cluster response
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster_name` | string | Yes | The name of the cluster to update. |
| `instance_groups` | array | Yes | List of instance groups to update. |
| `region_name` | string | Yes | AWS region name. Default is us-east-1. |
| `profile_name` | string | No | AWS profile name. If not provided, uses the default profile. |

## AWS CLI

```bash
aws sagemaker update-cluster --cluster-name <cluster_name> --instance-groups <instance_groups> --region <region_name>
```

## boto3

```python
import boto3

client = boto3.client('sagemaker')
response = client.update_cluster(
    ClusterName=cluster_name,
    InstanceGroups=instance_groups,
    Region=region_name,
)
```
