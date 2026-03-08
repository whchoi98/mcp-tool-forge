---
name: get-serverless-templates
description: Returns example SAM templates from the Serverless Land GitHub repo.

        Use this tool to get examples for building serverless applications with AWS Lambda and best practices of serverless architecture.
        The examples are centered on event-driven architecture that can help you boost agility and build reliable, scalable applications.
        Services like Lambda, EventBridge, Step Functions, SQS, SNS, and API Gateway are featured here. Examples can be deployed
        out of the box using the SAM CLI, or you can modify examples to fit your needs.

        Usage tips:
        - Each template includes a template.yml, example-pattern.json file, and src directory containing the Lambda function code. The example-pattern.json file
        contains metadata about the template, links to AWS documentation, SAM commands, and a description of the application.
        - Download the YAML template with the gitHubLink in the tool response using the GitHub API
        - Use the sam_build and sam_deploy tools to build and deploy the application to AWS Cloud

        Returns:
            Dict: List of matching Serverless templates with README content and GitHub link
        
---

# Get Serverless Templates

Returns example SAM templates from the Serverless Land GitHub repo.

        Use this tool to get examples for building serverless applications with AWS Lambda and best practices of serverless architecture.
        The examples are centered on event-driven architecture that can help you boost agility and build reliable, scalable applications.
        Services like Lambda, EventBridge, Step Functions, SQS, SNS, and API Gateway are featured here. Examples can be deployed
        out of the box using the SAM CLI, or you can modify examples to fit your needs.

        Usage tips:
        - Each template includes a template.yml, example-pattern.json file, and src directory containing the Lambda function code. The example-pattern.json file
        contains metadata about the template, links to AWS documentation, SAM commands, and a description of the application.
        - Download the YAML template with the gitHubLink in the tool response using the GitHub API
        - Use the sam_build and sam_deploy tools to build and deploy the application to AWS Cloud

        Returns:
            Dict: List of matching Serverless templates with README content and GitHub link
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template_type` | string | Yes | Template type (e.g., API, ETL, Web) |
| `runtime` | string | No | Lambda runtime (e.g., nodejs22.x, python3.13) |

