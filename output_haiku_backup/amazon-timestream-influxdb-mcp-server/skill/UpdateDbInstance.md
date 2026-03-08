---
name: UpdateDbInstance
description: Updates a Timestream for InfluxDB DB instance.
---

# Updatedbinstance

Updates a Timestream for InfluxDB DB instance.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `identifier` | string | Yes | The id of the DB instance. |
| `db_instance_type` | string | No | Update the DB cluster to use the specified DB instance Type. |
| `db_parameter_group_identifier` | string | No | The id of the DB parameter group to assign to your DB. |
| `port` | string | No | The port number on which InfluxDB accepts connections. Default: 8086 |
| `allocated_storage_gb` | string | No | The amount of storage to allocate for your DB storage type (in gibibytes). |
| `db_storage_type` | string | No | The Timestream for InfluxDB DB storage type to read and write InfluxDB data. |
| `deployment_type` | string | No | Specifies whether the DB instance will be deployed as a standalone instance or with a Multi-AZ standby for high availability. |
| `log_delivery_configuration` | string | No | Configuration for sending InfluxDB engine logs to a specified S3 bucket. |
| `tool_write_mode` | boolean | No | Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False) |

## AWS CLI

```bash
aws timestream-influxdb update-db-instance --db-instance-identifier <identifier> --db-instance-type <db_instance_type> --db-parameter-group-identifier <db_parameter_group_identifier> --port <port> --allocated-storage-gb <allocated_storage_gb> --db-storage-type <db_storage_type> --deployment-type <deployment_type> --log-delivery-configuration <log_delivery_configuration>
```

## boto3

```python
import boto3

client = boto3.client('timestream-influxdb')
response = client.update_db_instance(
    DbInstanceIdentifier=identifier,
    DbInstanceType=db_instance_type,
    DbParameterGroupIdentifier=db_parameter_group_identifier,
    Port=port,
    AllocatedStorageGb=allocated_storage_gb,
    DbStorageType=db_storage_type,
    DeploymentType=deployment_type,
    LogDeliveryConfiguration=log_delivery_configuration,
)
```
