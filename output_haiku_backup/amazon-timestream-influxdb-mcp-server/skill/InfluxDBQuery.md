---
name: InfluxDBQuery
description: Query data from InfluxDB using Flux query language.
---

# Influxdbquery

Query data from InfluxDB using Flux query language.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `url` | string | No | The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided. |
| `token` | string | No | The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided. |
| `org` | string | No | The organization name. Falls back to INFLUXDB_ORG env var if not provided. |
| `query` | string | Yes | The Flux query string. |
| `verify_ssl` | boolean | No | Whether to verify SSL with https connections. |

