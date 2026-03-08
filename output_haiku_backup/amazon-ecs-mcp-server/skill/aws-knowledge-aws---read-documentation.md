---
name: aws-knowledge-aws---read-documentation
description: Fetch and convert an AWS documentation page to markdown format.

## Usage

This tool retrieves the content of an AWS documentation page and converts it to markdown format.
For long documents, you can make multiple calls with different start_index values to retrieve
the entire content in chunks.

## URL Requirements

Allow-listed URL prefixes:
- docs.aws.amazon.com
- aws.amazon.com
- repost.aws/knowledge-center
- docs.amplify.aws
- ui.docs.amplify.aws
- github.com/aws-cloudformation/aws-cloudformation-templates
- github.com/aws-samples/aws-cdk-examples
- github.com/aws-samples/generative-ai-cdk-constructs-samples
- github.com/aws-samples/serverless-patterns
- github.com/awsdocs/aws-cdk-guide
- github.com/awslabs/aws-solutions-constructs
- github.com/cdklabs/cdk-nag
- constructs.dev/packages/@aws-cdk-containers
- constructs.dev/packages/@aws-cdk
- constructs.dev/packages/@cdk-cloudformation
- constructs.dev/packages/aws-analytics-reference-architecture
- constructs.dev/packages/aws-cdk-lib
- constructs.dev/packages/cdk-amazon-chime-resources
- constructs.dev/packages/cdk-aws-lambda-powertools-layer
- constructs.dev/packages/cdk-ecr-deployment
- constructs.dev/packages/cdk-lambda-powertools-python-layer
- constructs.dev/packages/cdk-serverless-clamscan
- constructs.dev/packages/cdk8s
- constructs.dev/packages/cdk8s-plus-33

Deny-listed URL prefixes:
- aws.amazon.com/marketplace

## Example URLs

- https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html
- https://aws.amazon.com/about-aws/whats-new/2023/02/aws-telco-network-builder/
- https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/
- https://aws.amazon.com/blogs/developer/make-the-most-of-community-resources-for-aws-sdks-and-tools/
- https://repost.aws/knowledge-center/example-article
- https://docs.amplify.aws/react/build-a-backend/auth/
- https://ui.docs.amplify.aws/angular/connected-components/authenticator
- https://github.com/aws-samples/aws-cdk-examples/blob/main/README.md
- https://github.com/awslabs/aws-solutions-constructs/blob/main/README.md
- https://constructs.dev/packages/aws-cdk-lib/v/2.229.1?submodule=aws_lambda&lang=typescript
- https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/README.md

## Output Format

The output is formatted as markdown text with:
- Preserved headings and structure
- Code blocks for examples
- Lists and tables converted to markdown format

## Handling Long Documents

If the response indicates the document was truncated, you have several options:

1. **Continue Reading**: Make another call with start_index set to the end of the previous response
2. **Jump to Section**: If a Table of Contents is provided, you can jump directly to any section using the character positions shown (e.g., "char 1500-2800"). Note: Table of Contents length is not counted toward max_length.
3. **Stop Early**: For very long documents (>30,000 characters), if you've already found the specific information needed, you can stop reading

    ## ECS DOCUMENTATION GUIDANCE:
    This tool provides up-to-date ECS documentation and implementation guidance, including new ECS features beyond standard LLM training data.

    New ECS features include:
    - ECS Native Blue-Green Deployments (different from CodeDeploy blue-green, launched 2025)
    - ECS Managed Instances (launched 2025)
    - ECS Express Mode / Express Gateway Services (launched 2025)

---

# Aws Knowledge Aws   Read Documentation

Fetch and convert an AWS documentation page to markdown format.

## Usage

This tool retrieves the content of an AWS documentation page and converts it to markdown format.
For long documents, you can make multiple calls with different start_index values to retrieve
the entire content in chunks.

## URL Requirements

Allow-listed URL prefixes:
- docs.aws.amazon.com
- aws.amazon.com
- repost.aws/knowledge-center
- docs.amplify.aws
- ui.docs.amplify.aws
- github.com/aws-cloudformation/aws-cloudformation-templates
- github.com/aws-samples/aws-cdk-examples
- github.com/aws-samples/generative-ai-cdk-constructs-samples
- github.com/aws-samples/serverless-patterns
- github.com/awsdocs/aws-cdk-guide
- github.com/awslabs/aws-solutions-constructs
- github.com/cdklabs/cdk-nag
- constructs.dev/packages/@aws-cdk-containers
- constructs.dev/packages/@aws-cdk
- constructs.dev/packages/@cdk-cloudformation
- constructs.dev/packages/aws-analytics-reference-architecture
- constructs.dev/packages/aws-cdk-lib
- constructs.dev/packages/cdk-amazon-chime-resources
- constructs.dev/packages/cdk-aws-lambda-powertools-layer
- constructs.dev/packages/cdk-ecr-deployment
- constructs.dev/packages/cdk-lambda-powertools-python-layer
- constructs.dev/packages/cdk-serverless-clamscan
- constructs.dev/packages/cdk8s
- constructs.dev/packages/cdk8s-plus-33

Deny-listed URL prefixes:
- aws.amazon.com/marketplace

## Example URLs

- https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html
- https://aws.amazon.com/about-aws/whats-new/2023/02/aws-telco-network-builder/
- https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/
- https://aws.amazon.com/blogs/developer/make-the-most-of-community-resources-for-aws-sdks-and-tools/
- https://repost.aws/knowledge-center/example-article
- https://docs.amplify.aws/react/build-a-backend/auth/
- https://ui.docs.amplify.aws/angular/connected-components/authenticator
- https://github.com/aws-samples/aws-cdk-examples/blob/main/README.md
- https://github.com/awslabs/aws-solutions-constructs/blob/main/README.md
- https://constructs.dev/packages/aws-cdk-lib/v/2.229.1?submodule=aws_lambda&lang=typescript
- https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/README.md

## Output Format

The output is formatted as markdown text with:
- Preserved headings and structure
- Code blocks for examples
- Lists and tables converted to markdown format

## Handling Long Documents

If the response indicates the document was truncated, you have several options:

1. **Continue Reading**: Make another call with start_index set to the end of the previous response
2. **Jump to Section**: If a Table of Contents is provided, you can jump directly to any section using the character positions shown (e.g., "char 1500-2800"). Note: Table of Contents length is not counted toward max_length.
3. **Stop Early**: For very long documents (>30,000 characters), if you've already found the specific information needed, you can stop reading

    ## ECS DOCUMENTATION GUIDANCE:
    This tool provides up-to-date ECS documentation and implementation guidance, including new ECS features beyond standard LLM training data.

    New ECS features include:
    - ECS Native Blue-Green Deployments (different from CodeDeploy blue-green, launched 2025)
    - ECS Managed Instances (launched 2025)
    - ECS Express Mode / Express Gateway Services (launched 2025)


## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `start_index` | integer | No | On return output starting at this character index, useful if a previous fetch was truncated and more content is required. |
| `url` | string | No | URL of the AWS documentation page to read |
| `max_length` | integer | No | Maximum number of characters to return. |

