---
name: deploy-serverless-app-help
description: Provides instructions on how to deploy a serverless application to AWS Lambda.

        Deploying a Lambda application requires generating IaC templates, building the code, packaging
        the code, selecting a deployment tool, and executing the deployment commands. This tool walks through
        each step and links to tools in this MCP server. For deploying web applications specifically, use the deploy_webapp_tool.

        Returns:
            Dict[str, Any]: A dictionary containing the deployment help information.
        
---

# Deploy Serverless App Help

Provides instructions on how to deploy a serverless application to AWS Lambda.

        Deploying a Lambda application requires generating IaC templates, building the code, packaging
        the code, selecting a deployment tool, and executing the deployment commands. This tool walks through
        each step and links to tools in this MCP server. For deploying web applications specifically, use the deploy_webapp_tool.

        Returns:
            Dict[str, Any]: A dictionary containing the deployment help information.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `application_type` | string | Yes | Type of application to deploy |

