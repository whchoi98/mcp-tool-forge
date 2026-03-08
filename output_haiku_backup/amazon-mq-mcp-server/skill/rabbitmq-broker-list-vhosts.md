---
name: rabbitmq-broker-list-vhosts
description: List all the virtual hosts (vhosts) in the broker.
---

# Rabbitmq Broker List Vhosts

List all the virtual hosts (vhosts) in the broker.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

## AWS CLI

```bash
aws mq list-vhosts
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.list_vhosts(
)
```
