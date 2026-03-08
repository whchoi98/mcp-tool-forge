---
name: rabbitmq-broker-list-connections
description: List all connections on the RabbitMQ broker.
---

# Rabbitmq Broker List Connections

List all connections on the RabbitMQ broker.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

## AWS CLI

```bash
aws mq list-broker-connections
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.list_broker_connections(
)
```
