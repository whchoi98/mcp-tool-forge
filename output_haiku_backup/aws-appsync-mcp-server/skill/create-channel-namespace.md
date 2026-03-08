---
name: create-channel-namespace
description: Creates a ChannelNamespace for an Api.

        This operation creates a channel namespace for the specified GraphQL API.
        Channel namespaces provide a way to organize and manage real-time subscriptions
        in AppSync APIs, enabling event-driven architectures and real-time data updates.
        
---

# Create Channel Namespace

Creates a ChannelNamespace for an Api.

        This operation creates a channel namespace for the specified GraphQL API.
        Channel namespaces provide a way to organize and manage real-time subscriptions
        in AppSync APIs, enabling event-driven architectures and real-time data updates.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `api_id` | string | Yes | The ID of the Api associated with the ChannelNamespace |
| `name` | string | Yes | The name of the ChannelNamespace |
| `subscribe_auth_modes` | string | No | The authorization mode to use for subscribing to messages on the channel namespace |
| `publish_auth_modes` | string | No | The authorization mode to use for publishing messages on the channel namespace |
| `code_handlers` | string | No | The event handler functions that run custom business logic to process published events and subscribe requests |
| `handler_configs` | string | No | Configuration for event handlers that process published events and subscribe requests |
| `tags` | string | No | A map of tags to assign to the resource |

## AWS CLI

```bash
aws appsync create-channel-namespace --api-id <api_id> --name <name> --subscribe-auth-mode <subscribe_auth_modes> --publish-auth-mode <publish_auth_modes> --code-handlers <code_handlers> --handler-configs <handler_configs> --tags <tags>
```

## boto3

```python
import boto3

client = boto3.client('appsync')
response = client.create_channel_namespace(
    ApiId=api_id,
    Name=name,
    SubscribeAuthMode=subscribe_auth_modes,
    PublishAuthMode=publish_auth_modes,
    CodeHandlers=code_handlers,
    HandlerConfigs=handler_configs,
    Tags=tags,
)
```
