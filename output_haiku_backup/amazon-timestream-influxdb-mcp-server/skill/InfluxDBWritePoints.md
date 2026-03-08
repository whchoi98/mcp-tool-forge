---
name: InfluxDBWritePoints
description: Write data points to InfluxDB endpoint.
---

# Influxdbwritepoints

Write data points to InfluxDB endpoint.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `url` | string | No | The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided. |
| `token` | string | No | The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided. |
| `bucket` | string | Yes | The destination bucket for writes. |
| `org` | string | No | The organization name. Falls back to INFLUXDB_ORG env var if not provided. |
| `points` | array | Yes | List of data points to write. Each point should be a dictionary with measurement, tags, fields, and optional time. |
| `time_precision` | string | No | The precision for the unix timestamps within the body line-protocol. One of: ns, us, ms, s (default is ns). |
| `sync_mode` | string | No | The synchronization mode, either 'synchronous' or 'asynchronous'. |
| `verify_ssl` | boolean | No | Whether to verify SSL with https connections. |
| `tool_write_mode` | boolean | No | Tool is run in write mode and will be able to perform any create/update/delete operations. Default is read-only mode (False) |

