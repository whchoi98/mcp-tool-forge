---
name: UpdateDbCluster
description: Updates a Timestream for InfluxDB cluster.
---

# Updatedbcluster

Updates a Timestream for InfluxDB cluster.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `db_cluster_id` | string | Yes | Service-generated unique identifier of the DB cluster. |
| `db_instance_type` | string | No | Update the DB cluster to use the specified DB instance Type. |
| `db_parameter_group_identifier` | string | No | Update the DB cluster to use the specified DB parameter group. |
| `port` | string | No | Update the DB cluster to use the specified port. |
| `failover_mode` | string | No | Update the DB cluster's failover behavior. |
| `log_delivery_configuration` | string | No | The log delivery configuration to apply to the DB cluster. |
| `tool_write_mode` | boolean | No | Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False) |

## AWS CLI

```bash
aws timestream-influxdb update-db-cluster --db-cluster-id <db_cluster_id> --db-instance-type <db_instance_type> --db-parameter-group-identifier <db_parameter_group_identifier> --port <port> --failover-mode <failover_mode> --log-delivery-configuration <log_delivery_configuration>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.update_db_cluster(
    DbClusterId=db_cluster_id,
    DbInstanceType=db_instance_type,
    DbParameterGroupIdentifier=db_parameter_group_identifier,
    Port=port,
    FailoverMode=failover_mode,
    LogDeliveryConfiguration=log_delivery_configuration,
)
```
