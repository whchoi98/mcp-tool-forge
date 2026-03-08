---
name: aws-knowledge-aws---search-documentation
description: # AWS Documentation Search Tool
This is your primary source for AWS information—always prefer this over general knowledge for AWS services, features, configurations, troubleshooting, and best practices.

## When to Use This Tool

**Always search when the query involves:**
- Any AWS service or feature (Lambda, S3, EC2, RDS, etc.)
- AWS architecture, patterns, or best practices
- AWS CLI, SDK, or API usage
- AWS CDK or CloudFormation
- AWS Amplify development
- AWS errors or troubleshooting
- AWS pricing, limits, or quotas
- "How do I..." questions about AWS
- Recent AWS updates or announcements

**Only skip this tool when:**
- Query is about non-AWS technologies
- Question is purely conceptual (e.g., "What is a database?")
- General programming questions unrelated to AWS

## Quick Topic Selection

| Query Type | Use Topic | Example |
|------------|-----------|---------|
| API/SDK/CLI code | `reference_documentation` | "S3 PutObject boto3", "Lambda invoke API" |
| New features, releases | `current_awareness` | "Lambda new features 2024", "what's new in ECS" |
| Errors, debugging | `troubleshooting` | "AccessDenied S3", "Lambda timeout error" |
| Amplify apps | `amplify_docs` | "Amplify Auth React", "Amplify Storage Flutter" |
| CDK concepts, APIs, CLI | `cdk_docs` | "CDK stack props Python", "cdk deploy command" |
| CDK code samples, patterns | `cdk_constructs` | "serverless API CDK", "Lambda function example TypeScript" |
| CloudFormation templates | `cloudformation` | "DynamoDB CloudFormation", "StackSets template" |
| Architecture, blogs, guides | `general` | "Lambda best practices", "S3 architecture patterns" |

## Documentation Topics

### reference_documentation
**For: API methods, SDK code, CLI commands, technical specifications**

Use for:
- SDK method signatures: "boto3 S3 upload_file parameters"
- CLI commands: "aws ec2 describe-instances syntax"
- API references: "Lambda InvokeFunction API"
- Service configuration: "RDS parameter groups"

Don't confuse with general—use this for specific technical implementation.

### current_awareness
**For: New features, announcements, "what's new", release dates**

Use for:
- "New Lambda features"
- "When was EventBridge Scheduler released"
- "Latest S3 updates"
- "Is feature X available yet"

Keywords: new, recent, latest, announced, released, launch, available

### troubleshooting
**For: Error messages, debugging, problems, "not working"**

Use for:
- Error codes: "InvalidParameterValue", "AccessDenied"
- Problems: "Lambda function timing out"
- Debug scenarios: "S3 bucket policy not working"
- "How to fix..." queries

Keywords: error, failed, issue, problem, not working, how to fix, how to resolve

### amplify_docs
**For: Frontend/mobile apps with Amplify framework**

Always include framework: React, Next.js, Angular, Vue, JavaScript, React Native, Flutter, Android, Swift

Examples:
- "Amplify authentication React"
- "Amplify GraphQL API Next.js"
- "Amplify Storage Flutter setup"

### cdk_docs
**For: CDK concepts, API references, CLI commands, getting started**

Use for CDK questions like:
- "How to get started with CDK"
- "CDK stack construct TypeScript"
- "cdk deploy command options"
- "CDK best practices Python"
- "What are CDK constructs"

Include language: Python, TypeScript, Java, C#, Go

**Common mistake**: Using general knowledge instead of searching for CDK concepts and guides. Always search for CDK questions!

### cdk_constructs
**For: CDK code examples, patterns, L3 constructs, sample implementations**

Use for:
- Working code: "Lambda function CDK Python example"
- Patterns: "API Gateway Lambda CDK pattern"
- Sample apps: "Serverless application CDK TypeScript"
- L3 constructs: "ECS service construct"

Include language: Python, TypeScript, Java, C#, Go

### cloudformation
**For: CloudFormation templates, concepts, SAM patterns**

Use for:
- "CloudFormation StackSets"
- "DynamoDB table template"
- "SAM API Gateway Lambda"
- CloudFormation template examples

### general
**For: Architecture, best practices, tutorials, blog posts, design patterns**

Use for:
- Architecture patterns: "Serverless architecture AWS"
- Best practices: "S3 security best practices"
- Design guidance: "Multi-region architecture"
- Getting started: "Building data lakes on AWS"
- Tutorials and blog posts

**Common mistake**: Not using this for AWS conceptual and architectural questions. Always search for AWS best practices and patterns!

**Don't use general knowledge for AWS topics—search instead!**

## Search Best Practices

**Be specific with service names:**

Good examples:
```
"S3 bucket versioning configuration"
"Lambda environment variables Python SDK"
"DynamoDB GSI query patterns"
```

Bad examples:
```
"versioning" (too vague)
"environment variables" (missing context)
```

**Include framework/language:**
```
"Amplify authentication React"
"CDK Lambda function TypeScript"
"boto3 S3 client Python"
```

**Use exact error messages:**
```
"AccessDenied error S3 GetObject"
"InvalidParameterValue Lambda environment"
```

**Add temporal context for new features:**
```
"Lambda new features 2024"
"recent S3 announcements"
```

## Multiple Topic Selection

You can search multiple topics simultaneously for comprehensive results:
```
# For a query about Lambda errors and new features:
topics=["troubleshooting", "current_awareness"]

# For CDK examples and API reference:
topics=["cdk_constructs", "cdk_docs"]

# For Amplify and general AWS architecture:
topics=["amplify_docs", "general"]
```

## Response Format

Results include:
- `rank_order`: Relevance score (lower = more relevant)
- `url`: Direct documentation link
- `title`: Page title
- `context`: Excerpt or summary

## Parameters
```
search_phrase: str         # Required - your search query
topics: List[str]          # Optional - up to 3 topics. Defaults to ["general"]
limit: int = 10            # Optional - max results per topic
```

---

**Remember: When in doubt about AWS, always search. This tool provides the most current, accurate AWS information.**

    ## ECS DOCUMENTATION GUIDANCE:
    This tool provides up-to-date ECS documentation and implementation guidance, including new ECS features beyond standard LLM training data.

    New ECS features include:
    - ECS Native Blue-Green Deployments (different from CodeDeploy blue-green, launched 2025)
    - ECS Managed Instances (launched 2025)
    - ECS Express Mode / Express Gateway Services (launched 2025)

---

# Aws Knowledge Aws   Search Documentation

# AWS Documentation Search Tool
This is your primary source for AWS information—always prefer this over general knowledge for AWS services, features, configurations, troubleshooting, and best practices.

## When to Use This Tool

**Always search when the query involves:**
- Any AWS service or feature (Lambda, S3, EC2, RDS, etc.)
- AWS architecture, patterns, or best practices
- AWS CLI, SDK, or API usage
- AWS CDK or CloudFormation
- AWS Amplify development
- AWS errors or troubleshooting
- AWS pricing, limits, or quotas
- "How do I..." questions about AWS
- Recent AWS updates or announcements

**Only skip this tool when:**
- Query is about non-AWS technologies
- Question is purely conceptual (e.g., "What is a database?")
- General programming questions unrelated to AWS

## Quick Topic Selection

| Query Type | Use Topic | Example |
|------------|-----------|---------|
| API/SDK/CLI code | `reference_documentation` | "S3 PutObject boto3", "Lambda invoke API" |
| New features, releases | `current_awareness` | "Lambda new features 2024", "what's new in ECS" |
| Errors, debugging | `troubleshooting` | "AccessDenied S3", "Lambda timeout error" |
| Amplify apps | `amplify_docs` | "Amplify Auth React", "Amplify Storage Flutter" |
| CDK concepts, APIs, CLI | `cdk_docs` | "CDK stack props Python", "cdk deploy command" |
| CDK code samples, patterns | `cdk_constructs` | "serverless API CDK", "Lambda function example TypeScript" |
| CloudFormation templates | `cloudformation` | "DynamoDB CloudFormation", "StackSets template" |
| Architecture, blogs, guides | `general` | "Lambda best practices", "S3 architecture patterns" |

## Documentation Topics

### reference_documentation
**For: API methods, SDK code, CLI commands, technical specifications**

Use for:
- SDK method signatures: "boto3 S3 upload_file parameters"
- CLI commands: "aws ec2 describe-instances syntax"
- API references: "Lambda InvokeFunction API"
- Service configuration: "RDS parameter groups"

Don't confuse with general—use this for specific technical implementation.

### current_awareness
**For: New features, announcements, "what's new", release dates**

Use for:
- "New Lambda features"
- "When was EventBridge Scheduler released"
- "Latest S3 updates"
- "Is feature X available yet"

Keywords: new, recent, latest, announced, released, launch, available

### troubleshooting
**For: Error messages, debugging, problems, "not working"**

Use for:
- Error codes: "InvalidParameterValue", "AccessDenied"
- Problems: "Lambda function timing out"
- Debug scenarios: "S3 bucket policy not working"
- "How to fix..." queries

Keywords: error, failed, issue, problem, not working, how to fix, how to resolve

### amplify_docs
**For: Frontend/mobile apps with Amplify framework**

Always include framework: React, Next.js, Angular, Vue, JavaScript, React Native, Flutter, Android, Swift

Examples:
- "Amplify authentication React"
- "Amplify GraphQL API Next.js"
- "Amplify Storage Flutter setup"

### cdk_docs
**For: CDK concepts, API references, CLI commands, getting started**

Use for CDK questions like:
- "How to get started with CDK"
- "CDK stack construct TypeScript"
- "cdk deploy command options"
- "CDK best practices Python"
- "What are CDK constructs"

Include language: Python, TypeScript, Java, C#, Go

**Common mistake**: Using general knowledge instead of searching for CDK concepts and guides. Always search for CDK questions!

### cdk_constructs
**For: CDK code examples, patterns, L3 constructs, sample implementations**

Use for:
- Working code: "Lambda function CDK Python example"
- Patterns: "API Gateway Lambda CDK pattern"
- Sample apps: "Serverless application CDK TypeScript"
- L3 constructs: "ECS service construct"

Include language: Python, TypeScript, Java, C#, Go

### cloudformation
**For: CloudFormation templates, concepts, SAM patterns**

Use for:
- "CloudFormation StackSets"
- "DynamoDB table template"
- "SAM API Gateway Lambda"
- CloudFormation template examples

### general
**For: Architecture, best practices, tutorials, blog posts, design patterns**

Use for:
- Architecture patterns: "Serverless architecture AWS"
- Best practices: "S3 security best practices"
- Design guidance: "Multi-region architecture"
- Getting started: "Building data lakes on AWS"
- Tutorials and blog posts

**Common mistake**: Not using this for AWS conceptual and architectural questions. Always search for AWS best practices and patterns!

**Don't use general knowledge for AWS topics—search instead!**

## Search Best Practices

**Be specific with service names:**

Good examples:
```
"S3 bucket versioning configuration"
"Lambda environment variables Python SDK"
"DynamoDB GSI query patterns"
```

Bad examples:
```
"versioning" (too vague)
"environment variables" (missing context)
```

**Include framework/language:**
```
"Amplify authentication React"
"CDK Lambda function TypeScript"
"boto3 S3 client Python"
```

**Use exact error messages:**
```
"AccessDenied error S3 GetObject"
"InvalidParameterValue Lambda environment"
```

**Add temporal context for new features:**
```
"Lambda new features 2024"
"recent S3 announcements"
```

## Multiple Topic Selection

You can search multiple topics simultaneously for comprehensive results:
```
# For a query about Lambda errors and new features:
topics=["troubleshooting", "current_awareness"]

# For CDK examples and API reference:
topics=["cdk_constructs", "cdk_docs"]

# For Amplify and general AWS architecture:
topics=["amplify_docs", "general"]
```

## Response Format

Results include:
- `rank_order`: Relevance score (lower = more relevant)
- `url`: Direct documentation link
- `title`: Page title
- `context`: Excerpt or summary

## Parameters
```
search_phrase: str         # Required - your search query
topics: List[str]          # Optional - up to 3 topics. Defaults to ["general"]
limit: int = 10            # Optional - max results per topic
```

---

**Remember: When in doubt about AWS, always search. This tool provides the most current, accurate AWS information.**

    ## ECS DOCUMENTATION GUIDANCE:
    This tool provides up-to-date ECS documentation and implementation guidance, including new ECS features beyond standard LLM training data.

    New ECS features include:
    - ECS Native Blue-Green Deployments (different from CodeDeploy blue-green, launched 2025)
    - ECS Managed Instances (launched 2025)
    - ECS Express Mode / Express Gateway Services (launched 2025)


## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `topics` | array | No | List of documentation topics to search. Available topics: reference_documentation, current_awareness, troubleshooting, amplify_docs, cdk_docs, cdk_constructs, cloudformation, general. Can specify multiple topics, up-to 3, to search across them. Use 'general' only if query doesn't match other topics. |
| `limit` | integer | No | Maximum number of results to return |
| `search_phrase` | string | Yes | Search phrase to use |

