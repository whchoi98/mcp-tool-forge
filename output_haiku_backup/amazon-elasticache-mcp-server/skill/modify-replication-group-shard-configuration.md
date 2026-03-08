---
name: modify-replication-group-shard-configuration
description: Modify the shard configuration of an existing Amazon ElastiCache replication group.

    This tool modifies the shard configuration of an existing replication group by:
    - Modifying the number of replicas in a shard
    - Specifying preferred availability zones for replicas

    Parameters:
        replication_group_id (str): The identifier of the replication group to modify.
        node_group_count (int): The number of node groups (shards) in the replication group.
        apply_immediately (Optional[bool]): Whether to apply changes immediately or during maintenance window.
        resharding_configuration (Optional[Union[str, List[Dict]]]): Resharding configuration in either shorthand string format or list of dictionaries format.
            Shorthand format: "NodeGroupId=string,NewShardConfiguration={NewReplicaCount=integer,PreferredAvailabilityZones=string1,string2}"
            Multiple configurations can be separated by spaces.
            JSON format: List of dictionaries with required fields:
            - NodeGroupId: string
            - NewShardConfiguration:
                - NewReplicaCount: integer
                - PreferredAvailabilityZones: list of strings (optional)

    Returns:
        Dict containing information about the modified replication group.
    
---

# Modify-Replication-Group-Shard-Configuration

Modify the shard configuration of an existing Amazon ElastiCache replication group.

    This tool modifies the shard configuration of an existing replication group by:
    - Modifying the number of replicas in a shard
    - Specifying preferred availability zones for replicas

    Parameters:
        replication_group_id (str): The identifier of the replication group to modify.
        node_group_count (int): The number of node groups (shards) in the replication group.
        apply_immediately (Optional[bool]): Whether to apply changes immediately or during maintenance window.
        resharding_configuration (Optional[Union[str, List[Dict]]]): Resharding configuration in either shorthand string format or list of dictionaries format.
            Shorthand format: "NodeGroupId=string,NewShardConfiguration={NewReplicaCount=integer,PreferredAvailabilityZones=string1,string2}"
            Multiple configurations can be separated by spaces.
            JSON format: List of dictionaries with required fields:
            - NodeGroupId: string
            - NewShardConfiguration:
                - NewReplicaCount: integer
                - PreferredAvailabilityZones: list of strings (optional)

    Returns:
        Dict containing information about the modified replication group.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `replication_group_id` | string | Yes |  |
| `node_group_count` | integer | Yes |  |
| `apply_immediately` | string | No |  |
| `resharding_configuration` | string | No |  |

## AWS CLI

```bash
aws elasticache modify-replication-group-shard-configuration --replication-group-id <replication_group_id> --node-group-count <node_group_count> --apply-immediately <apply_immediately> --resharding-configuration <resharding_configuration>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.modify_replication_group_shard_configuration(
    ReplicationGroupId=replication_group_id,
    NodeGroupCount=node_group_count,
    ApplyImmediately=apply_immediately,
    ReshardingConfiguration=resharding_configuration,
)
```
