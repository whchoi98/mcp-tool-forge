---
name: delete-app
description: Deletes a complete Express Mode deployment including service and ECR infrastructure.

This tool performs complete cleanup of an Express Mode deployment:
1. Deletes the Express Gateway Service
2. Deletes the ECR CloudFormation stack (ECR repository + IAM role)

## Parameters:
- Required: service_arn (ARN of Express Gateway Service)
- Required: app_name (Application name used during deployment)

## What Gets Deleted:
- Express Gateway Service and all provisioned infrastructure
  (ALB, target groups, security groups)
- CloudFormation stack for ECR resources, including ECR repo and container images

## Returns:
Dictionary containing:
- service_deletion: Status and details of service deletion
- ecr_deletion: Status and details of ECR stack deletion
- summary: Overall deletion summary with list of deleted resources
- errors: List of any errors encountered

## Usage Examples:
```
# Delete complete deployment
delete_app(
    service_arn="arn:aws:ecs:us-west-2:123456789012:express-service/my-api",
    app_name="my-app"
)
```

Returns on success:
```
{
  "service_deletion": {
    "status": "deleted",
    "service_arn": "arn:aws:ecs:us-west-2:123456789012:express-service/my-api",
    "message": "Express Gateway Service deleted successfully"
  },
  "ecr_deletion": {
    "status": "deleted",
    "stack_name": "my-app-ecr-infrastructure",
    "message": "ECR stack deleted successfully",
    "deleted_resources": [
      "ECR repository: my-app-repo",
      "IAM role: my-app-ecr-push-pull-role"
    ]
  },
  "summary": {
    "status": "success",
    "message": "Successfully deleted Express Mode deployment for my-app",
    "deleted_resources": [
      "Express Gateway Service: arn:aws:ecs:...",
      "ECR repository: my-app-repo",
      "IAM role: my-app-ecr-push-pull-role"
    ]
  },
  "errors": []
}
```

## Important Notes:
- This operation requires WRITE permission (ALLOW_WRITE=true)
- Deletion is irreversible - all container images will be deleted
- Service deletion may take a few minutes as infrastructure is deprovisioned
- If errors occur, partial deletion is possible (check summary for details)
---

# Delete App

Deletes a complete Express Mode deployment including service and ECR infrastructure.

This tool performs complete cleanup of an Express Mode deployment:
1. Deletes the Express Gateway Service
2. Deletes the ECR CloudFormation stack (ECR repository + IAM role)

## Parameters:
- Required: service_arn (ARN of Express Gateway Service)
- Required: app_name (Application name used during deployment)

## What Gets Deleted:
- Express Gateway Service and all provisioned infrastructure
  (ALB, target groups, security groups)
- CloudFormation stack for ECR resources, including ECR repo and container images

## Returns:
Dictionary containing:
- service_deletion: Status and details of service deletion
- ecr_deletion: Status and details of ECR stack deletion
- summary: Overall deletion summary with list of deleted resources
- errors: List of any errors encountered

## Usage Examples:
```
# Delete complete deployment
delete_app(
    service_arn="arn:aws:ecs:us-west-2:123456789012:express-service/my-api",
    app_name="my-app"
)
```

Returns on success:
```
{
  "service_deletion": {
    "status": "deleted",
    "service_arn": "arn:aws:ecs:us-west-2:123456789012:express-service/my-api",
    "message": "Express Gateway Service deleted successfully"
  },
  "ecr_deletion": {
    "status": "deleted",
    "stack_name": "my-app-ecr-infrastructure",
    "message": "ECR stack deleted successfully",
    "deleted_resources": [
      "ECR repository: my-app-repo",
      "IAM role: my-app-ecr-push-pull-role"
    ]
  },
  "summary": {
    "status": "success",
    "message": "Successfully deleted Express Mode deployment for my-app",
    "deleted_resources": [
      "Express Gateway Service: arn:aws:ecs:...",
      "ECR repository: my-app-repo",
      "IAM role: my-app-ecr-push-pull-role"
    ]
  },
  "errors": []
}
```

## Important Notes:
- This operation requires WRITE permission (ALLOW_WRITE=true)
- Deletion is irreversible - all container images will be deleted
- Service deletion may take a few minutes as infrastructure is deprovisioned
- If errors occur, partial deletion is possible (check summary for details)

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `service_arn` | string | Yes | ARN of the Express Gateway Service to delete |
| `app_name` | string | Yes | Name of the application (used to identify ECR stack to delete) |

## AWS CLI

```bash
aws ecs delete-service --service-arn <service_arn> --force <True>
```

## boto3

```python
import boto3

client = boto3.client('ecs')
response = client.delete_service(
    ServiceArn=service_arn,
    Force=True,
)
```
