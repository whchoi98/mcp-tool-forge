---
name: CreateDbCluster
description: Create a new Timestream for InfluxDB database cluster.
---

# Createdbcluster

Create a new Timestream for InfluxDB database cluster.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | string | Yes | The name that uniquely identifies the DB cluster when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint. |
| `db_instance_type` | string | Yes | The Timestream for InfluxDB DB instance type to run InfluxDB on. |
| `password` | string | Yes | The password of the initial admin user created in InfluxDB. This password will allow you to access the InfluxDB UI to perform various administrative task and also use the InfluxDB CLI to create an operator token. |
| `allocated_storage_gb` | integer | Yes | The amount of storage to allocate for your DB storage type in GiB (gibibytes). |
| `vpc_security_group_ids` | array | Yes | A list of VPC security group IDs to associate with the DB. |
| `vpc_subnet_ids` | array | Yes | A list of VPC subnet IDs to associate with the DB. Provide at least two VPC subnet IDs in different Availability Zones when deploying with a Multi-AZ standby. |
| `publicly_accessible` | boolean | No | Configures the DB with a public IP to facilitate access from outside the VPC. |
| `username` | string | No | The username of the initial admin user created in InfluxDB. |
| `organization` | string | No | The name of the initial organization for the initial admin user in InfluxDB.An InfluxDB organization is a workspace for a group of users |
| `bucket` | string | No | The name of the initial InfluxDB bucket. |
| `db_storage_type` | string | No | The Timestream for InfluxDB DB storage type to read and write InfluxDB data. |
| `deployment_type` | string | No | Specifies whether the DB instance will be deployed as a standalone instance or with a Multi-AZ standby for high availability. |
| `networkType` | string | No | Specifies whether the network type of the Timestream for InfluxDB cluster is IPv4 or DUAL. |
| `port` | string | No | The port number on which InfluxDB accepts connections. Default: 8086 |
| `db_parameter_group_identifier` | string | No | The id of the DB parameter group to assign to your DB. |
| `failover_mode` | string | No | Specifies the behavior of failure recovery when the primary node of the cluster fails. |
| `tags` | string | No | A list of tags to assign to the DB. |
| `log_delivery_configuration` | string | No | Configuration for sending InfluxDB engine logs to a specified S3 bucket. |
| `tool_write_mode` | boolean | No | Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False) |

