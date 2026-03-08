---
name: InfluxDBListBuckets
description: List all buckets in InfluxDB.
---

# Influxdblistbuckets

List all buckets in InfluxDB.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `url` | string | No | The URL of the InfluxDB server. Falls back to INFLUXDB_URL env var if not provided. |
| `token` | string | No | The authentication token. Falls back to INFLUXDB_TOKEN env var if not provided. |
| `org` | string | No | The organization name. Falls back to INFLUXDB_ORG env var if not provided. |
| `verify_ssl` | boolean | No | Whether to verify SSL with https connections. |

