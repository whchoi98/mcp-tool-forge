---
name: describe-service-updates
description: Returns details of the service updates.

    Parameters:
        service_update_name (Optional[str]): The unique ID of the service update to describe.
        service_update_status (Optional[List[str]]): List of status values to filter by.
            Valid values: available | cancelled | expired | complete
        starting_token (Optional[str]): An optional token returned from a previous request.
            Use this token for pagination of results from this operation.
        page_size (Optional[int]): The maximum number of records to include in each page
            of results.
        max_items (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxItems value, a marker is included
            in the response so that the remaining results can be retrieved.

    Returns:
        Dict containing information about the service updates, including:
        - ServiceUpdates: List of service updates
        - NextToken: Token for next set of results
    
---

# Describe-Service-Updates

Returns details of the service updates.

    Parameters:
        service_update_name (Optional[str]): The unique ID of the service update to describe.
        service_update_status (Optional[List[str]]): List of status values to filter by.
            Valid values: available | cancelled | expired | complete
        starting_token (Optional[str]): An optional token returned from a previous request.
            Use this token for pagination of results from this operation.
        page_size (Optional[int]): The maximum number of records to include in each page
            of results.
        max_items (Optional[int]): The maximum number of records to include in the response.
            If more records exist than the specified MaxItems value, a marker is included
            in the response so that the remaining results can be retrieved.

    Returns:
        Dict containing information about the service updates, including:
        - ServiceUpdates: List of service updates
        - NextToken: Token for next set of results
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `service_update_name` | string | No |  |
| `service_update_status` | string | No |  |
| `starting_token` | string | No |  |
| `page_size` | string | No |  |
| `max_items` | string | No |  |

## AWS CLI

```bash
aws elasticache describe-service-updates --service-update-name <service_update_name> --service-update-status <service_update_status> --marker <starting_token> --max-records <page_size> --max-items <max_items>
```

## boto3

```python
import boto3

client = boto3.client('elasticache')
response = client.describe_service_updates(
    ServiceUpdateName=service_update_name,
    ServiceUpdateStatus=service_update_status,
    Marker=starting_token,
    MaxRecords=page_size,
    MaxItems=max_items,
)
```
