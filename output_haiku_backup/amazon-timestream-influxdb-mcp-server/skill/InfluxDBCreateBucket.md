---
name: InfluxDBCreateBucket
description: Create a new bucket in InfluxDB.
---

# Influxdbcreatebucket

Create a new bucket in InfluxDB.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `bucket_name` | string | Yes | The name of the bucket to create. |
| `url` | string | No | The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided. |
| `token` | string | No | The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided. |
| `org` | string | No | The organization name. Falls back to INFLUXDB_ORG env var if not provided. |
| `retention_seconds` | string | No | Retention period in seconds. 0 or None means infinite retention. |
| `description` | string | No | Description of the bucket. |
| `verify_ssl` | boolean | No | Whether to verify SSL with https connections. |
| `tool_write_mode` | boolean | No | Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False) |

