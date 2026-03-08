---
name: disconnect
description: Close a connection to DocumentDB.

    This tool closes a previously established connection to DocumentDB.

    Returns:
        Dict[str, Any]: Confirmation of successful disconnection
    
---

# Disconnect

Close a connection to DocumentDB.

    This tool closes a previously established connection to DocumentDB.

    Returns:
        Dict[str, Any]: Confirmation of successful disconnection
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |

## AWS CLI

```bash
aws docdb close-connection --connection-id <connection_id>
```

## boto3

```python
import boto3

client = boto3.client('docdb')
response = client.close_connection(
    ConnectionId=connection_id,
)
```
