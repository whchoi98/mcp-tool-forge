---
name: list-delivery-streams
description: List your delivery streams.

    Args:
        limit: The maximum number of delivery streams to list
        delivery_stream_type: The delivery stream type. This can be one of the following values:
            DirectPut - Provider data is sent directly to the Firehose stream
            KinesisStreamAsSource - Data is sourced from an existing Kinesis stream
        exclusive_start_delivery_stream_name: The name of the delivery stream to start the list after

    Returns:
        Dict containing the list of delivery streams and whether there are more streams available
    
---

# List-Delivery-Streams

List your delivery streams.

    Args:
        limit: The maximum number of delivery streams to list
        delivery_stream_type: The delivery stream type. This can be one of the following values:
            DirectPut - Provider data is sent directly to the Firehose stream
            KinesisStreamAsSource - Data is sourced from an existing Kinesis stream
        exclusive_start_delivery_stream_name: The name of the delivery stream to start the list after

    Returns:
        Dict containing the list of delivery streams and whether there are more streams available
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `limit` | string | No |  |
| `delivery_stream_type` | string | No |  |
| `exclusive_start_delivery_stream_name` | string | No |  |

## AWS CLI

```bash
aws firehose list-delivery-streams --limit <limit> --delivery-stream-type <delivery_stream_type> --exclusive-start-delivery-stream-name <exclusive_start_delivery_stream_name>
```

## boto3

```python
import boto3

client = boto3.client('firehose')
response = client.list_delivery_streams(
    Limit=limit,
    DeliveryStreamType=delivery_stream_type,
    ExclusiveStartDeliveryStreamName=exclusive_start_delivery_stream_name,
)
```
