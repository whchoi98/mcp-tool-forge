---
name: list-users
description: Execute the AWS AmazonMQ `list_users` operation.
---

# List Users

Execute the AWS AmazonMQ `list_users` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `BrokerId` | string | Yes |  |
| `MaxResults` | integer | No | <p>The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.</p> |
| `NextToken` | string | No | <p>The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.</p> |

## AWS CLI

```bash
aws iam list-users --path-prefix <path_prefix> --max-items <max_items>
```

## boto3

```python
import boto3

client = boto3.client('iam')
response = client.list_users(
    PathPrefix=path_prefix,
    MaxItems=max_items,
)
```
