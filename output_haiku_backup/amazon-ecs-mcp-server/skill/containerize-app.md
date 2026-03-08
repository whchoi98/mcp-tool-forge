---
name: containerize-app
description: Start here if a user wants to run their application locally or deploy an app to the cloud.
Provides guidance for containerizing a web application.

This tool provides guidance on how to build Docker images for web applications,
including recommendations for base images, build tools, and architecture choices.

USAGE INSTRUCTIONS:
1. Run this tool to get guidance on how to configure your application for ECS.
2. Follow the steps generated from the tool.
3. Proceed to create_ecs_infrastructure tool.

The guidance includes:
- Example Dockerfile content
- Example docker-compose.yml content
- Build commands for different container tools
- Architecture recommendations
- Troubleshooting tips

Parameters:
    app_path: Path to the web application directory
    port: Port the application listens on

Returns:
    Dictionary containing containerization guidance
---

# Containerize App

Start here if a user wants to run their application locally or deploy an app to the cloud.
Provides guidance for containerizing a web application.

This tool provides guidance on how to build Docker images for web applications,
including recommendations for base images, build tools, and architecture choices.

USAGE INSTRUCTIONS:
1. Run this tool to get guidance on how to configure your application for ECS.
2. Follow the steps generated from the tool.
3. Proceed to create_ecs_infrastructure tool.

The guidance includes:
- Example Dockerfile content
- Example docker-compose.yml content
- Build commands for different container tools
- Architecture recommendations
- Troubleshooting tips

Parameters:
    app_path: Path to the web application directory
    port: Port the application listens on

Returns:
    Dictionary containing containerization guidance

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `app_path` | string | Yes | Absolute file path to the web application directory |
| `port` | integer | Yes | Port the application listens on |

