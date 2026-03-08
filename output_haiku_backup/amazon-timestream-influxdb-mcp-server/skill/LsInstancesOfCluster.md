---
name: LsInstancesOfCluster
description: List all Timestream for InfluxDB instances belonging to a specific DB cluster.
---

# Lsinstancesofcluster

List all Timestream for InfluxDB instances belonging to a specific DB cluster.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `db_cluster_id` | string | Yes | Service-generated unique identifier of the DB cluster. |
| `next_token` | string | No | The pagination token. To resume pagination, provide the next-token value as an argument of a subsequent API invocation. |
| `max_results` | string | No | The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output. |

## AWS CLI

```bash
aws timestream-influxdb list-db-instances --db-cluster-id <db_cluster_id> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.list_db_instances(
    DbClusterId=db_cluster_id,
    NextToken=next_token,
    MaxResults=max_results,
)
```
