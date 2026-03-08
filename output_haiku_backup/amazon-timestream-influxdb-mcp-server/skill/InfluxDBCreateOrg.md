---
name: InfluxDBCreateOrg
description: Create a new organization in InfluxDB.
---

# Influxdbcreateorg

Create a new organization in InfluxDB.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `org_name` | string | Yes | The name of the organization to create. |
| `url` | string | No | The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided. |
| `token` | string | No | The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided. |
| `verify_ssl` | boolean | No | Whether to verify SSL with https connections. |
| `tool_write_mode` | boolean | No | Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False) |

