---
name: deploy-webapp
description: Deploy web applications to AWS Serverless, including Lambda as compute, DynamoDB as databases, API GW, ACM Certificates, and Route 53 DNS records.

        This tool uses the Lambda Web Adapter framework so that applications can be written in a standard web framework like Express or Next.js can be easily
        deployed to Lambda. You do not need to use integrate the code with any adapter framework before using this tool.

        Returns:
            Dict: Deployment result and link to pending deployment resource
        
---

# Deploy Webapp

Deploy web applications to AWS Serverless, including Lambda as compute, DynamoDB as databases, API GW, ACM Certificates, and Route 53 DNS records.

        This tool uses the Lambda Web Adapter framework so that applications can be written in a standard web framework like Express or Next.js can be easily
        deployed to Lambda. You do not need to use integrate the code with any adapter framework before using this tool.

        Returns:
            Dict: Deployment result and link to pending deployment resource
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `deployment_type` | string | Yes | Type of deployment |
| `project_name` | string | Yes | Project name |
| `project_root` | string | Yes | Absolute path to the project root directory |
| `region` | string | No | AWS Region to deploy to (e.g., us-east-1) |
| `backend_configuration` | string | No | Backend configuration |
| `frontend_configuration` | string | No | Frontend configuration |

