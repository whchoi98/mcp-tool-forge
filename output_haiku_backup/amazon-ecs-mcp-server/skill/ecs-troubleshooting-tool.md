---
name: ecs-troubleshooting-tool
description: ECS troubleshooting tool with multiple diagnostic actions.

This tool provides access to all ECS troubleshooting operations through a single interface.
Use the 'action' parameter to specify which troubleshooting operation to perform.

## Available Actions and Parameters:

### 1. get_ecs_troubleshooting_guidance
Initial assessment and data collection
- Required: ecs_cluster_name
- Optional: ecs_service_name (Name of the ECS Service to troubleshoot),
           symptoms_description (Description of symptoms experienced by the user)
- Example: action="get_ecs_troubleshooting_guidance",
           parameters={"ecs_cluster_name": "my-cluster", "ecs_service_name": "my-service",
                       "symptoms_description": "ALB returning 503 errors"}

### 2. fetch_cloudformation_status
Infrastructure-level diagnostics for CloudFormation Stacks
- Required: cfn_stack_name
- Example: action="fetch_cloudformation_status",
           parameters={"cfn_stack_name": "my-app-stack"}

### 3. fetch_service_events
Service-level diagnostics for ECS Services
- Required: ecs_cluster_name, ecs_service_name
- Optional: time_window (Time window in seconds to look back for events (default: 3600)),
            start_time (Explicit start time for the analysis window (UTC, takes
            precedence over time_window if provided)),
            end_time (Explicit end time for the analysis window (UTC, defaults to
            current time if not provided))
- Example: action="fetch_service_events",
           parameters={"ecs_cluster_name": "my-cluster",
                       "ecs_service_name": "my-service",
                       "time_window": 7200}

### 4. fetch_task_failures
Task-level diagnostics for ECS Task failures
- Required: ecs_cluster_name
- Optional: time_window (Time window in seconds to look back for failures (default: 3600)),
            start_time (Explicit start time for the analysis window (UTC, takes
            precedence over time_window if provided)),
            end_time (Explicit end time for the analysis window (UTC, defaults to
            current time if not provided))
- Example: action="fetch_task_failures",
           parameters={"ecs_cluster_name": "my-cluster",
                       "time_window": 3600}

### 5. fetch_task_logs
Application-level diagnostics through CloudWatch Logs
- Required: ecs_cluster_name
- Optional: ecs_task_id (Specific ECS Task ID to retrieve logs for),
            time_window (Time window in seconds to look back for logs (default: 3600)),
            filter_pattern (CloudWatch Logs filter pattern),
            start_time (Explicit start time for the analysis window (UTC, takes
            precedence over time_window if provided)),
            end_time (Explicit end time for the analysis window (UTC, defaults to
            current time if not provided))
- Example: action="fetch_task_logs",
           parameters={"ecs_cluster_name": "my-cluster",
                       "filter_pattern": "ERROR",
                       "time_window": 1800}

### 6. detect_image_pull_failures
Specialized tool for detecting container image pull failures
- Required: None (but at least one valid parameter combination must be provided)
- Valid combinations: ecs_cluster_name+ecs_service_name, ecs_cluster_name+ecs_task_id,
  cfn_stack_name,
  family_prefix
- Optional: ecs_cluster_name, ecs_service_name, cfn_stack_name, family_prefix, ecs_task_id
- Example: action="detect_image_pull_failures",
           parameters={"ecs_cluster_name": "my-cluster", "ecs_service_name": "my-service"}

### 7. fetch_network_configuration
Network-level diagnostics for ECS deployments
- Required: ecs_cluster_name
- Optional: vpc_id (Specific VPC ID to analyze)
- Example: action="fetch_network_configuration",
           parameters={"ecs_cluster_name": "my-cluster", "vpc_id": "vpc-12345678"}

## Resource Discovery:
If you don't know the cluster or service names, use `ecs_resource_management` tool first:

# List all clusters
ecs_resource_management(api_operation="ListClusters")

# List services in a cluster
ecs_resource_management(api_operation="ListServices", api_params={"cluster": "my-cluster"})

# Get detailed cluster information
ecs_resource_management(api_operation="DescribeClusters",
                       api_params={"clusters": ["my-cluster"]})

## Quick Usage Examples:
```
# Initial assessment and data collection
action: "get_ecs_troubleshooting_guidance"
parameters: {"ecs_cluster_name": "my-cluster",
            "symptoms_description": "ALB returning 503 errors"}

# Infrastructure-level diagnostics for CloudFormation Stacks
action: "fetch_cloudformation_status"
parameters: {"cfn_stack_name": "my-app-stack"}

# Service-level diagnostics for ECS Services
action: "fetch_service_events"
parameters: {"ecs_cluster_name": "my-cluster",
            "ecs_service_name": "my-service",
            "time_window": 7200}

# Task-level diagnostics for ECS Task failures
action: "fetch_task_failures"
parameters: {"ecs_cluster_name": "my-cluster",
            "time_window": 3600}

# Application-level diagnostics through CloudWatch Logs
action: "fetch_task_logs"
parameters: {"ecs_cluster_name": "my-cluster",
            "filter_pattern": "ERROR",
            "time_window": 1800}

# Specialized tool for detecting container image pull failures
action: "detect_image_pull_failures"
parameters: {"ecs_cluster_name": "my-cluster", "ecs_service_name": "my-service"}

# Network-level diagnostics for ECS deployments
action: "fetch_network_configuration"
parameters: {"ecs_cluster_name": "my-cluster", "vpc_id": "vpc-12345678"}
```

Parameters:
    action: The troubleshooting action to perform (see available actions above)
    parameters: Action-specific parameters (see parameter specifications above)

Returns:
    Results from the selected troubleshooting action
---

# Ecs Troubleshooting Tool

ECS troubleshooting tool with multiple diagnostic actions.

This tool provides access to all ECS troubleshooting operations through a single interface.
Use the 'action' parameter to specify which troubleshooting operation to perform.

## Available Actions and Parameters:

### 1. get_ecs_troubleshooting_guidance
Initial assessment and data collection
- Required: ecs_cluster_name
- Optional: ecs_service_name (Name of the ECS Service to troubleshoot),
           symptoms_description (Description of symptoms experienced by the user)
- Example: action="get_ecs_troubleshooting_guidance",
           parameters={"ecs_cluster_name": "my-cluster", "ecs_service_name": "my-service",
                       "symptoms_description": "ALB returning 503 errors"}

### 2. fetch_cloudformation_status
Infrastructure-level diagnostics for CloudFormation Stacks
- Required: cfn_stack_name
- Example: action="fetch_cloudformation_status",
           parameters={"cfn_stack_name": "my-app-stack"}

### 3. fetch_service_events
Service-level diagnostics for ECS Services
- Required: ecs_cluster_name, ecs_service_name
- Optional: time_window (Time window in seconds to look back for events (default: 3600)),
            start_time (Explicit start time for the analysis window (UTC, takes
            precedence over time_window if provided)),
            end_time (Explicit end time for the analysis window (UTC, defaults to
            current time if not provided))
- Example: action="fetch_service_events",
           parameters={"ecs_cluster_name": "my-cluster",
                       "ecs_service_name": "my-service",
                       "time_window": 7200}

### 4. fetch_task_failures
Task-level diagnostics for ECS Task failures
- Required: ecs_cluster_name
- Optional: time_window (Time window in seconds to look back for failures (default: 3600)),
            start_time (Explicit start time for the analysis window (UTC, takes
            precedence over time_window if provided)),
            end_time (Explicit end time for the analysis window (UTC, defaults to
            current time if not provided))
- Example: action="fetch_task_failures",
           parameters={"ecs_cluster_name": "my-cluster",
                       "time_window": 3600}

### 5. fetch_task_logs
Application-level diagnostics through CloudWatch Logs
- Required: ecs_cluster_name
- Optional: ecs_task_id (Specific ECS Task ID to retrieve logs for),
            time_window (Time window in seconds to look back for logs (default: 3600)),
            filter_pattern (CloudWatch Logs filter pattern),
            start_time (Explicit start time for the analysis window (UTC, takes
            precedence over time_window if provided)),
            end_time (Explicit end time for the analysis window (UTC, defaults to
            current time if not provided))
- Example: action="fetch_task_logs",
           parameters={"ecs_cluster_name": "my-cluster",
                       "filter_pattern": "ERROR",
                       "time_window": 1800}

### 6. detect_image_pull_failures
Specialized tool for detecting container image pull failures
- Required: None (but at least one valid parameter combination must be provided)
- Valid combinations: ecs_cluster_name+ecs_service_name, ecs_cluster_name+ecs_task_id,
  cfn_stack_name,
  family_prefix
- Optional: ecs_cluster_name, ecs_service_name, cfn_stack_name, family_prefix, ecs_task_id
- Example: action="detect_image_pull_failures",
           parameters={"ecs_cluster_name": "my-cluster", "ecs_service_name": "my-service"}

### 7. fetch_network_configuration
Network-level diagnostics for ECS deployments
- Required: ecs_cluster_name
- Optional: vpc_id (Specific VPC ID to analyze)
- Example: action="fetch_network_configuration",
           parameters={"ecs_cluster_name": "my-cluster", "vpc_id": "vpc-12345678"}

## Resource Discovery:
If you don't know the cluster or service names, use `ecs_resource_management` tool first:

# List all clusters
ecs_resource_management(api_operation="ListClusters")

# List services in a cluster
ecs_resource_management(api_operation="ListServices", api_params={"cluster": "my-cluster"})

# Get detailed cluster information
ecs_resource_management(api_operation="DescribeClusters",
                       api_params={"clusters": ["my-cluster"]})

## Quick Usage Examples:
```
# Initial assessment and data collection
action: "get_ecs_troubleshooting_guidance"
parameters: {"ecs_cluster_name": "my-cluster",
            "symptoms_description": "ALB returning 503 errors"}

# Infrastructure-level diagnostics for CloudFormation Stacks
action: "fetch_cloudformation_status"
parameters: {"cfn_stack_name": "my-app-stack"}

# Service-level diagnostics for ECS Services
action: "fetch_service_events"
parameters: {"ecs_cluster_name": "my-cluster",
            "ecs_service_name": "my-service",
            "time_window": 7200}

# Task-level diagnostics for ECS Task failures
action: "fetch_task_failures"
parameters: {"ecs_cluster_name": "my-cluster",
            "time_window": 3600}

# Application-level diagnostics through CloudWatch Logs
action: "fetch_task_logs"
parameters: {"ecs_cluster_name": "my-cluster",
            "filter_pattern": "ERROR",
            "time_window": 1800}

# Specialized tool for detecting container image pull failures
action: "detect_image_pull_failures"
parameters: {"ecs_cluster_name": "my-cluster", "ecs_service_name": "my-service"}

# Network-level diagnostics for ECS deployments
action: "fetch_network_configuration"
parameters: {"ecs_cluster_name": "my-cluster", "vpc_id": "vpc-12345678"}
```

Parameters:
    action: The troubleshooting action to perform (see available actions above)
    parameters: Action-specific parameters (see parameter specifications above)

Returns:
    Results from the selected troubleshooting action

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `action` | string | No |  |
| `parameters` | string | No |  |

