---
name: get-iac-guidance
description: Returns guidance on selecting an infrastructure as code (IaC) platform to deploy Serverless applications to AWS.

        Using IaC is a best practice when managing AWS resources. IaC platform choices include AWS SAM, CDK, and CloudFormation.
        Use this tool to decide which IaC tool to use for your Serverless deployments based on your specific use case and requirements.
        By default, SAM is the recomended framework.

        Returns:
            Dict: IaC guidance information
        
---

# Get Iac Guidance

Returns guidance on selecting an infrastructure as code (IaC) platform to deploy Serverless applications to AWS.

        Using IaC is a best practice when managing AWS resources. IaC platform choices include AWS SAM, CDK, and CloudFormation.
        Use this tool to decide which IaC tool to use for your Serverless deployments based on your specific use case and requirements.
        By default, SAM is the recomended framework.

        Returns:
            Dict: IaC guidance information
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `iac_tool` | string | No | IaC tool to use |
| `include_examples` | string | No | Whether to include examples |

