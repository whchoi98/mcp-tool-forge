---
name: rabbitmq-broker-list-queues
description: List all the queues in the broker.
---

# Rabbitmq Broker List Queues

List all the queues in the broker.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

## AWS CLI

```bash
aws mq list-queues
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.list_queues(
)
```
