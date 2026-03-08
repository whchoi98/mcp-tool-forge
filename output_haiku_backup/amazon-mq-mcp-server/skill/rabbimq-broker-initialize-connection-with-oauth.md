---
name: rabbimq-broker-initialize-connection-with-oauth
description: Connect to a new RabbitMQ broker using OAuth. It only applies to RabbitMQ broker which authentication strategy is config_managed.

            broker_hostname: The hostname of the broker. For example, b-a9565a64-da39-4afc-9239-c43a9376b5ba.mq.us-east-1.on.aws, b-9560b8e1-3d33-4d91-9488-a3dc4a61dfe7.mq.us-east-1.amazonaws.com
            oauth_token: A valid access token
            
---

# Rabbimq Broker Initialize Connection With Oauth

Connect to a new RabbitMQ broker using OAuth. It only applies to RabbitMQ broker which authentication strategy is config_managed.

            broker_hostname: The hostname of the broker. For example, b-a9565a64-da39-4afc-9239-c43a9376b5ba.mq.us-east-1.on.aws, b-9560b8e1-3d33-4d91-9488-a3dc4a61dfe7.mq.us-east-1.amazonaws.com
            oauth_token: A valid access token
            

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `broker_hostname` | string | Yes |  |
| `oauth_token` | string | Yes |  |

## AWS CLI

```bash
aws mq create-broker-connection --broker-hostname <broker_hostname> --oauth-token <oauth_token>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.create_broker_connection(
    BrokerHostname=broker_hostname,
    AuthenticationStrategy=config_managed,
    OAuthToken=oauth_token,
)
```
