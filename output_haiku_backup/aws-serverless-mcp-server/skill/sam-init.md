---
name: sam-init
description: Initializes a serverless application using AWS SAM (Serverless Application Model) CLI.

        Requirements:
        - AWS SAM CLI MUST be installed and configured in your environment

        This tool creates a new SAM project that consists of:
        - An AWS SAM template to define your infrastructure code
        - A folder structure that organizes your application
        - Configuration for your AWS Lambda functions

        Use this tool to initialize a new project when building a serverless application.
        This tool generates a project based on a pre-defined template. After calling this tool,
        modify the code and infrastructure templates to fit the requirements of your application.

        Usage tips:
        - Do not use this tool on existing projects as it creates brand new directory. Instead manually create SAM templates in the existing application's directory.
        - Either select from one of predefined templates, or from the SAM GitHub repo (https://github.com/aws/aws-sam-cli-app-templates)

        Returns:
            Dict[str, Any]: Result of the initialization
        
---

# Sam Init

Initializes a serverless application using AWS SAM (Serverless Application Model) CLI.

        Requirements:
        - AWS SAM CLI MUST be installed and configured in your environment

        This tool creates a new SAM project that consists of:
        - An AWS SAM template to define your infrastructure code
        - A folder structure that organizes your application
        - Configuration for your AWS Lambda functions

        Use this tool to initialize a new project when building a serverless application.
        This tool generates a project based on a pre-defined template. After calling this tool,
        modify the code and infrastructure templates to fit the requirements of your application.

        Usage tips:
        - Do not use this tool on existing projects as it creates brand new directory. Instead manually create SAM templates in the existing application's directory.
        - Either select from one of predefined templates, or from the SAM GitHub repo (https://github.com/aws/aws-sam-cli-app-templates)

        Returns:
            Dict[str, Any]: Result of the initialization
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `project_name` | string | Yes | Name of the SAM project to create |
| `runtime` | string | Yes | Runtime environment for the Lambda function.
                             This option applies only when the package type is Zip. |
| `project_directory` | string | Yes | Absolute path to directory where the SAM application will be initialized |
| `dependency_manager` | string | Yes | Dependency manager for the Lambda function (e.g. npm, pip) |
| `architecture` | string | No | Architecture for the Lambda function. |
| `package_type` | string | No | Package type for the Lambda function. Zip creates a .zip file archive, and Image creates a container image. |
| `application_template` | string | No | Template for the SAM application, e.g., hello-world, quick-start, etc.
             This parameter is required if location is not specified. |
| `application_insights` | string | No | Activate Amazon CloudWatch Application Insights monitoring.
                Helps you monitor the AWS resources in your applications to help identify potential issues.
                It can analyze AWS resource data for signs of problems and build automated CloudWatch dashboards to visualize them.
                 |
| `no_application_insights` | string | No | Deactivate Amazon CloudWatch Application Insights monitoring |
| `base_image` | string | No | Base image for the application when package type is Image.
                The AWS base images are preloaded with a language runtime, a runtime interface client to manage the
                interaction between Lambda and your function code, and a runtime interface emulator for local testing. |
| `config_env` | string | No | Environment name specifying default parameter values in the configuration file |
| `config_file` | string | No | Absolute path to configuration file containing default parameter values |
| `debug` | string | No | Turn on debug logging |
| `extra_content` | string | No | Override custom parameters in the template's cookiecutter.json |
| `location` | string | No | Template or application location (Git, HTTP/HTTPS, zip file path).
                This GitHub repo https://github.com/aws/aws-sam-cli-app-templates contains a collection of templates.
                This parameter is required if app_template is not specified. |
| `save_params` | string | No | Save parameters to the SAM configuration file |
| `tracing` | string | No | Activate AWS X-Ray tracing for Lambda functions. X-ray collects data about requests
            that your application serves and provides tools that you can use to view, filter, and gain insights into that data to identify issues
            and opportunities for optimization. |
| `no_tracing` | string | No | Deactivate AWS X-Ray tracing for Lambda functions |

