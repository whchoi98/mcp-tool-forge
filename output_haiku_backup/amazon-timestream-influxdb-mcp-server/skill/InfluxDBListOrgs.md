---
name: InfluxDBListOrgs
description: List all organizations in InfluxDB.
---

# Influxdblistorgs

List all organizations in InfluxDB.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `url` | string | No | The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided. |
| `token` | string | No | The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided. |
| `verify_ssl` | boolean | No | Whether to verify SSL with https connections. |

