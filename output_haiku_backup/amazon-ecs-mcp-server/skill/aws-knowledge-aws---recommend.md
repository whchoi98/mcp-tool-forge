---
name: aws-knowledge-aws---recommend
description: Get content recommendations for an AWS documentation page.

## Usage

This tool provides recommendations for related AWS documentation pages based on a given URL.
Use it to discover additional relevant content that might not appear in search results.
URL must be from the docs.aws.amazon.com domain.

## Recommendation Types

The recommendations include four categories:

1. **Highly Rated**: Popular pages within the same AWS service
2. **New**: Recently added pages within the same AWS service - useful for finding newly released features
3. **Similar**: Pages covering similar topics to the current page
4. **Journey**: Pages commonly viewed next by other users

## When to Use

- After reading a documentation page to find related content
- When exploring a new AWS service to discover important pages
- To find alternative explanations of complex concepts
- To discover the most popular pages for a service
- To find newly released information by using a service's welcome page URL and checking the **New** recommendations

## Finding New Features

To find newly released information about a service:
1. Find any page belong to that service, typically you can try the welcome page
2. Call this tool with that URL
3. Look specifically at the **New** recommendation type in the results

## Result Interpretation

Each recommendation includes:
- url: The documentation page URL
- title: The page title
- context: A brief description (if available)

    ## ECS DOCUMENTATION GUIDANCE:
    This tool provides up-to-date ECS documentation and implementation guidance, including new ECS features beyond standard LLM training data.

    New ECS features include:
    - ECS Native Blue-Green Deployments (different from CodeDeploy blue-green, launched 2025)
    - ECS Managed Instances (launched 2025)
    - ECS Express Mode / Express Gateway Services (launched 2025)

---

# Aws Knowledge Aws   Recommend

Get content recommendations for an AWS documentation page.

## Usage

This tool provides recommendations for related AWS documentation pages based on a given URL.
Use it to discover additional relevant content that might not appear in search results.
URL must be from the docs.aws.amazon.com domain.

## Recommendation Types

The recommendations include four categories:

1. **Highly Rated**: Popular pages within the same AWS service
2. **New**: Recently added pages within the same AWS service - useful for finding newly released features
3. **Similar**: Pages covering similar topics to the current page
4. **Journey**: Pages commonly viewed next by other users

## When to Use

- After reading a documentation page to find related content
- When exploring a new AWS service to discover important pages
- To find alternative explanations of complex concepts
- To discover the most popular pages for a service
- To find newly released information by using a service's welcome page URL and checking the **New** recommendations

## Finding New Features

To find newly released information about a service:
1. Find any page belong to that service, typically you can try the welcome page
2. Call this tool with that URL
3. Look specifically at the **New** recommendation type in the results

## Result Interpretation

Each recommendation includes:
- url: The documentation page URL
- title: The page title
- context: A brief description (if available)

    ## ECS DOCUMENTATION GUIDANCE:
    This tool provides up-to-date ECS documentation and implementation guidance, including new ECS features beyond standard LLM training data.

    New ECS features include:
    - ECS Native Blue-Green Deployments (different from CodeDeploy blue-green, launched 2025)
    - ECS Managed Instances (launched 2025)
    - ECS Express Mode / Express Gateway Services (launched 2025)


## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `url` | string | Yes | URL of the AWS documentation page to get recommendations for |

