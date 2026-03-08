---
name: create-datastore
description: Create a new data store in AWS HealthImaging.
---

# Create Datastore

Create a new data store in AWS HealthImaging.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_name` | string | Yes | Name for the new datastore |
| `kms_key_arn` | string | No | KMS key ARN for encryption |
| `tags` | string | No | Tags to apply to the datastore |

## AWS CLI

```bash
aws medical-imaging create-datastore --datastore-name <datastore_name> --kms-key-arn <kms_key_arn> --tags <tags>
```

## boto3

```python
import boto3

client = boto3.client('medical-imaging')
response = client.create_datastore(
    DatastoreName=datastore_name,
    KmsKeyArn=kms_key_arn,
    Tags=tags,
)
```
