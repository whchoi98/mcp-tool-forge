---
name: explain
description: MANDATORY: Explain any data in clear, human-readable format.

    For infrastructure operations (create/update/delete):
    - CONSUMES generated_code_token and returns explained_token
    - You MUST immediately display the returned explanation to user
    - You MUST use the returned explained_token for create/update/delete operations

    For general data explanation:
    - Pass any data in 'content' parameter
    - Provides comprehensive explanation of the data structure

    CRITICAL: You MUST immediately display the full explanation content to the user after calling this tool.
    The response contains an 'explanation' field that you MUST show to the user - this is MANDATORY.
    Never proceed with create/update/delete operations without first showing the user what will happen.

    Returns:
        explanation: Comprehensive explanation you MUST display to user
        explained_token: New token for infrastructure operations (if applicable)
    
---

# Explain

MANDATORY: Explain any data in clear, human-readable format.

    For infrastructure operations (create/update/delete):
    - CONSUMES generated_code_token and returns explained_token
    - You MUST immediately display the returned explanation to user
    - You MUST use the returned explained_token for create/update/delete operations

    For general data explanation:
    - Pass any data in 'content' parameter
    - Provides comprehensive explanation of the data structure

    CRITICAL: You MUST immediately display the full explanation content to the user after calling this tool.
    The response contains an 'explanation' field that you MUST show to the user - this is MANDATORY.
    Never proceed with create/update/delete operations without first showing the user what will happen.

    Returns:
        explanation: Comprehensive explanation you MUST display to user
        explained_token: New token for infrastructure operations (if applicable)
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | string | No | Any data to explain - infrastructure properties, JSON, dict, list, etc. |
| `generated_code_token` | string | No | Generated code token from generate_infrastructure_code (for infrastructure operations) |
| `context` | string | No | Context about what this data represents (e.g., 'KMS key creation', 'S3 bucket update') |
| `operation` | string | No | Operation type: create, update, delete, analyze |
| `format` | string | No | Explanation format: detailed, summary, technical |
| `user_intent` | string | No | Optional: User's stated purpose |

