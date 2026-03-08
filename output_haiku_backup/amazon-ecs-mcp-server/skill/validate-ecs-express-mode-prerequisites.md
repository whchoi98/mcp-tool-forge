---
name: validate-ecs-express-mode-prerequisites
description: Validates prerequisites for ECS Express Mode deployment.

This tool checks that all required resources exist and are properly configured
before deploying an ECS Express Gateway Service.

## Validation Checks:
1. Task Execution Role exists (checks default 'ecsTaskExecutionRole' if not provided)
2. Infrastructure Role exists (checks default 'ecsInfrastructureRoleForExpressServices'
   if not provided)
3. Docker image exists in the specified ECR repository

## Parameters:
- Required: image_uri (Full ECR image URI including tag)
- Optional: execution_role_arn (ARN of task execution role,
  defaults to 'ecsTaskExecutionRole')
- Optional: infrastructure_role_arn (ARN of infrastructure role,
  defaults to 'ecsInfrastructureRoleForExpressServices')

## Required IAM Roles:

### Task Execution Role:
- Allows ECS tasks to pull images and write logs
- Must have trust policy for ecs-tasks.amazonaws.com
- Should have AmazonECSTaskExecutionRolePolicy attached

### Infrastructure Role:
- Allows ECS to provision infrastructure
- Must have trust policy for ecs.amazonaws.com
- Should have AmazonECSInfrastructureRoleforExpressGatewayServices attached

## Returns:
Dictionary containing:
- valid: Boolean indicating if all prerequisites are met
- errors: List of error messages if validation fails
- warnings: List of warning messages
- details: Detailed validation results for each check

## Usage Examples:
```
# Validate with default role names
validate_ecs_express_mode_prerequisites(
    image_uri="123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:1700000000"
)

# Validate with custom role ARNs
validate_ecs_express_mode_prerequisites(
    image_uri="123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:1700000000",
    execution_role_arn="arn:aws:iam::123456789012:role/custom-execution-role",
    infrastructure_role_arn="arn:aws:iam::123456789012:role/custom-infra-role"
)
```

Returns when successful:
```
{
  "valid": true,
  "errors": [],
  "warnings": [],
  "details": {
    "execution_role": {
      "status": "valid",
      "arn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
      "name": "ecsTaskExecutionRole",
      "message": "Task Execution Role is valid"
    },
    "infrastructure_role": {
      "status": "valid",
      "arn": "arn:aws:iam::123456789012:role/ecsInfrastructureRoleForExpressServices",
      "name": "ecsInfrastructureRoleForExpressServices",
      "message": "Infrastructure Role is valid"
    },
    "image": {
      "status": "exists",
      "uri": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:1700000000",
      "repository": "my-app",
      "tag": "1700000000",
      "message": "Image found in ECR"
    }
  }
}
```

Returns when validation fails:
```
{
  "valid": false,
  "errors": [
    "Infrastructure Role not found: "
    "arn:aws:iam::123456789012:role/ecsInfrastructureRoleForExpressServices"
  ],
  "warnings": [],
  "details": {
    "execution_role": {"status": "valid", ...},
    "infrastructure_role": {"status": "not_found", ...},
    "image": {"status": "exists", ...}
  }
}
```
---

# Validate Ecs Express Mode Prerequisites

Validates prerequisites for ECS Express Mode deployment.

This tool checks that all required resources exist and are properly configured
before deploying an ECS Express Gateway Service.

## Validation Checks:
1. Task Execution Role exists (checks default 'ecsTaskExecutionRole' if not provided)
2. Infrastructure Role exists (checks default 'ecsInfrastructureRoleForExpressServices'
   if not provided)
3. Docker image exists in the specified ECR repository

## Parameters:
- Required: image_uri (Full ECR image URI including tag)
- Optional: execution_role_arn (ARN of task execution role,
  defaults to 'ecsTaskExecutionRole')
- Optional: infrastructure_role_arn (ARN of infrastructure role,
  defaults to 'ecsInfrastructureRoleForExpressServices')

## Required IAM Roles:

### Task Execution Role:
- Allows ECS tasks to pull images and write logs
- Must have trust policy for ecs-tasks.amazonaws.com
- Should have AmazonECSTaskExecutionRolePolicy attached

### Infrastructure Role:
- Allows ECS to provision infrastructure
- Must have trust policy for ecs.amazonaws.com
- Should have AmazonECSInfrastructureRoleforExpressGatewayServices attached

## Returns:
Dictionary containing:
- valid: Boolean indicating if all prerequisites are met
- errors: List of error messages if validation fails
- warnings: List of warning messages
- details: Detailed validation results for each check

## Usage Examples:
```
# Validate with default role names
validate_ecs_express_mode_prerequisites(
    image_uri="123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:1700000000"
)

# Validate with custom role ARNs
validate_ecs_express_mode_prerequisites(
    image_uri="123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:1700000000",
    execution_role_arn="arn:aws:iam::123456789012:role/custom-execution-role",
    infrastructure_role_arn="arn:aws:iam::123456789012:role/custom-infra-role"
)
```

Returns when successful:
```
{
  "valid": true,
  "errors": [],
  "warnings": [],
  "details": {
    "execution_role": {
      "status": "valid",
      "arn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
      "name": "ecsTaskExecutionRole",
      "message": "Task Execution Role is valid"
    },
    "infrastructure_role": {
      "status": "valid",
      "arn": "arn:aws:iam::123456789012:role/ecsInfrastructureRoleForExpressServices",
      "name": "ecsInfrastructureRoleForExpressServices",
      "message": "Infrastructure Role is valid"
    },
    "image": {
      "status": "exists",
      "uri": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:1700000000",
      "repository": "my-app",
      "tag": "1700000000",
      "message": "Image found in ECR"
    }
  }
}
```

Returns when validation fails:
```
{
  "valid": false,
  "errors": [
    "Infrastructure Role not found: "
    "arn:aws:iam::123456789012:role/ecsInfrastructureRoleForExpressServices"
  ],
  "warnings": [],
  "details": {
    "execution_role": {"status": "valid", ...},
    "infrastructure_role": {"status": "not_found", ...},
    "image": {"status": "exists", ...}
  }
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `image_uri` | string | Yes | Full ECR image URI with tag (e.g., 123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:tag) |
| `execution_role_arn` | string | No | Optional ARN of the ECS task execution role (defaults to ecsTaskExecutionRole) |
| `infrastructure_role_arn` | string | No | Optional ARN of the infrastructure role for Express Gateway (defaults to ecsInfrastructureRoleForExpressServices) |

