---
name: wait-for-service-ready
description: Waits for ECS tasks in a service to reach RUNNING status.

This tool polls the service every 10 seconds to check if tasks are running.
It will wait up to the specified timeout before returning a timeout status.

## Parameters:
- Required: cluster (ECS cluster name)
- Required: service_name (ECS service name)
- Optional: timeout_seconds (Max wait time, defaults to 300 seconds)

## Returns:
Dictionary containing:
- status: "success" if tasks are running, "timeout" if timeout reached,
  "failed" if an error occurred
- message: Human-readable status message

## Usage Examples:
```
# Wait for service with default 5-minute timeout
wait_for_service_ready(
    cluster="my-cluster",
    service_name="my-service"
)

# Wait for service with custom timeout
wait_for_service_ready(
    cluster="my-cluster",
    service_name="my-service",
    timeout_seconds=600
)
```

Returns on success:
```
{
  "status": "success",
  "message": "Service is ready with 2 running task(s)"
}
```

Returns on timeout:
```
{
  "status": "timeout",
  "message": "Timeout after 300s - service not ready"
}
```
---

# Wait For Service Ready

Waits for ECS tasks in a service to reach RUNNING status.

This tool polls the service every 10 seconds to check if tasks are running.
It will wait up to the specified timeout before returning a timeout status.

## Parameters:
- Required: cluster (ECS cluster name)
- Required: service_name (ECS service name)
- Optional: timeout_seconds (Max wait time, defaults to 300 seconds)

## Returns:
Dictionary containing:
- status: "success" if tasks are running, "timeout" if timeout reached,
  "failed" if an error occurred
- message: Human-readable status message

## Usage Examples:
```
# Wait for service with default 5-minute timeout
wait_for_service_ready(
    cluster="my-cluster",
    service_name="my-service"
)

# Wait for service with custom timeout
wait_for_service_ready(
    cluster="my-cluster",
    service_name="my-service",
    timeout_seconds=600
)
```

Returns on success:
```
{
  "status": "success",
  "message": "Service is ready with 2 running task(s)"
}
```

Returns on timeout:
```
{
  "status": "timeout",
  "message": "Timeout after 300s - service not ready"
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cluster` | string | Yes | Name of the ECS cluster |
| `service_name` | string | Yes | Name of the ECS service |
| `timeout_seconds` | integer | No | Maximum time to wait in seconds (default: 300 = 5 minutes) |

## AWS CLI

```bash
aws ecs wait services-stable --cluster <cluster> --services <service_name>
```

## boto3

```python
import boto3

client = boto3.client('ecs')
response = client.wait_for_service_stable(
    ClusterName=cluster,
    ServiceName=service_name,
    WaiterConfig={'Delay': 15, 'MaxAttempts': 20},
)
```
