---
name: build-and-push-image-to-ecr
description: Creates ECR infrastructure and builds/pushes a Docker image to ECR.

This tool automates the complete ECR setup and image deployment process:
1. Creates ECR repository via CloudFormation
2. Creates IAM role with ECR push/pull permissions
3. Builds Docker image from your application
4. Pushes image to ECR

## Parameters:
- Required: app_name (Application name, 1-20 chars, lowercase letters/digits/hyphens only)
- Required: app_path (Path to application directory with Dockerfile)
- Optional: tag (Image tag, defaults to epoch timestamp)

## Prerequisites:
- Docker installed and running locally
- Dockerfile exists in the application directory
- AWS credentials configured with appropriate permissions

## Returns:
Dictionary containing:
- repository_uri: ECR repository URI
- image_tag: The tag of the pushed image
- full_image_uri: Complete image URI with tag (use this for deployment)
- ecr_push_pull_role_arn: ARN of the IAM role created for ECR access
- stack_name: Name of the CloudFormation stack created

## Usage Examples:
```
# Build and push with auto-generated tag
build_and_push_image_to_ecr(
    app_name="my-app",
    app_path="/home/user/my-flask-app"
)

# Build and push with specific tag
build_and_push_image_to_ecr(
    app_name="my-app",
    app_path="/home/user/my-flask-app",
    tag="v1.0.0"
)
```

Returns:
```
{
  "repository_uri": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app-repo",
  "image_tag": "1700000000",
  "full_image_uri": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app-repo:1700000000",
  "ecr_push_pull_role_arn": "arn:aws:iam::123456789012:role/my-app-ecr-push-pull-role",
  "stack_name": "my-app-ecr-infrastructure"
}
```
---

# Build And Push Image To Ecr

Creates ECR infrastructure and builds/pushes a Docker image to ECR.

This tool automates the complete ECR setup and image deployment process:
1. Creates ECR repository via CloudFormation
2. Creates IAM role with ECR push/pull permissions
3. Builds Docker image from your application
4. Pushes image to ECR

## Parameters:
- Required: app_name (Application name, 1-20 chars, lowercase letters/digits/hyphens only)
- Required: app_path (Path to application directory with Dockerfile)
- Optional: tag (Image tag, defaults to epoch timestamp)

## Prerequisites:
- Docker installed and running locally
- Dockerfile exists in the application directory
- AWS credentials configured with appropriate permissions

## Returns:
Dictionary containing:
- repository_uri: ECR repository URI
- image_tag: The tag of the pushed image
- full_image_uri: Complete image URI with tag (use this for deployment)
- ecr_push_pull_role_arn: ARN of the IAM role created for ECR access
- stack_name: Name of the CloudFormation stack created

## Usage Examples:
```
# Build and push with auto-generated tag
build_and_push_image_to_ecr(
    app_name="my-app",
    app_path="/home/user/my-flask-app"
)

# Build and push with specific tag
build_and_push_image_to_ecr(
    app_name="my-app",
    app_path="/home/user/my-flask-app",
    tag="v1.0.0"
)
```

Returns:
```
{
  "repository_uri": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app-repo",
  "image_tag": "1700000000",
  "full_image_uri": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app-repo:1700000000",
  "ecr_push_pull_role_arn": "arn:aws:iam::123456789012:role/my-app-ecr-push-pull-role",
  "stack_name": "my-app-ecr-infrastructure"
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `app_name` | string | Yes | Name of the application (used for ECR repository and stack names) |
| `app_path` | string | Yes | Absolute file path to the web application directory containing the Dockerfile |
| `tag` | string | No | Optional image tag (if None, uses epoch timestamp) |

