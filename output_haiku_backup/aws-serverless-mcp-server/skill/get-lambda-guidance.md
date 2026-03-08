---
name: get-lambda-guidance
description: Use this tool to determine if AWS Lambda is suitable platform to deploy an application.

        Returns a comprehensive guide on when to choose AWS Lambda as a deployment platform.
        It includes scenarios when to use and not use Lambda, advantages and disadvantages,
        decision criteria, and specific guidance for various use cases (e.g. scheduled tasks, event-driven application).

        Returns:
            Dict: Lambda guidance information
        
---

# Get Lambda Guidance

Use this tool to determine if AWS Lambda is suitable platform to deploy an application.

        Returns a comprehensive guide on when to choose AWS Lambda as a deployment platform.
        It includes scenarios when to use and not use Lambda, advantages and disadvantages,
        decision criteria, and specific guidance for various use cases (e.g. scheduled tasks, event-driven application).

        Returns:
            Dict: Lambda guidance information
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `use_case` | string | Yes | Description of the use case. (e.g. scheduled tasks, event-driven application) |
| `include_examples` | string | No | Whether to include examples |

