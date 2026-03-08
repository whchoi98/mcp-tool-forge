---
name: rabbimq-broker-initialize-connection
description: Connect to a new RabbitMQ broker which authentication strategy is SIMPLE.

            broker_hostname: The hostname of the broker. For example, b-a9565a64-da39-4afc-9239-c43a9376b5ba.mq.us-east-1.on.aws, b-9560b8e1-3d33-4d91-9488-a3dc4a61dfe7.mq.us-east-1.amazonaws.com
            username: The username of user
            password: The password of user
            
---

# Rabbimq Broker Initialize Connection

Connect to a new RabbitMQ broker which authentication strategy is SIMPLE.

            broker_hostname: The hostname of the broker. For example, b-a9565a64-da39-4afc-9239-c43a9376b5ba.mq.us-east-1.on.aws, b-9560b8e1-3d33-4d91-9488-a3dc4a61dfe7.mq.us-east-1.amazonaws.com
            username: The username of user
            password: The password of user
            

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `broker_hostname` | string | Yes |  |
| `username` | string | Yes |  |
| `password` | string | Yes |  |

## AWS CLI

```bash
aws mq create-broker-connection --broker-hostname <broker_hostname> --username <username> --password <password>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.create_broker_connection(
    BrokerHostname=broker_hostname,
    Username=username,
    Password=password,
)
```
