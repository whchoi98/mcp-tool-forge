---
name: finch-build-container-image
description: Build a container image using Finch.

    This tool builds a Docker image using the specified Dockerfile and context directory.
    It supports a range of build options including tags, platforms, and more.
    If the Dockerfile contains references to ECR repositories, it verifies that
    ecr login cred helper is properly configured before proceeding with the build.

    Note: for ecr-login to work server needs access to AWS credentials/profile which are configured
    in the server mcp configuration file.

    Returns:
        Result: An object containing:
            - status (str): "success" if the operation succeeded, "error" otherwise
            - message (str): A descriptive message about the result of the operation

    Example response:
        Result(status="success", message="Successfully built image from /path/to/Dockerfile")

    
---

# Finch Build Container Image

Build a container image using Finch.

    This tool builds a Docker image using the specified Dockerfile and context directory.
    It supports a range of build options including tags, platforms, and more.
    If the Dockerfile contains references to ECR repositories, it verifies that
    ecr login cred helper is properly configured before proceeding with the build.

    Note: for ecr-login to work server needs access to AWS credentials/profile which are configured
    in the server mcp configuration file.

    Returns:
        Result: An object containing:
            - status (str): "success" if the operation succeeded, "error" otherwise
            - message (str): A descriptive message about the result of the operation

    Example response:
        Result(status="success", message="Successfully built image from /path/to/Dockerfile")

    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `dockerfile_path` | string | Yes | Absolute path to the Dockerfile |
| `context_path` | string | Yes | Absolute path to the build context directory |
| `tags` | string | No | List of tags to apply to the image (e.g., ['myimage:latest', 'myimage:v1']) |
| `platforms` | string | No | List of target platforms (e.g., ['linux/amd64', 'linux/arm64']) |
| `target` | string | No | Target build stage to build |
| `no_cache` | string | No | Whether to disable cache |
| `pull` | string | No | Whether to always pull base images |
| `build_contexts` | string | No | List of additional build contexts |
| `outputs` | string | No | Output destination |
| `cache_from` | string | No | List of external cache sources |
| `quiet` | string | No | Whether to suppress build output |
| `progress` | string | No | Type of progress output |

