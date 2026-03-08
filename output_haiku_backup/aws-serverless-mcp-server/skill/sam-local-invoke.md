---
name: sam-local-invoke
description: Locally invokes a Lambda function using AWS SAM CLI.

        Requirements:
        - AWS SAM CLI MUST be installed and configured in your environment
        - Docker must be installed and running in your environment.

        This command runs your Lambda function locally in a Docker container that simulates the AWS Lambda environment.
        Use this tool to test your Lambda functions before deploying them to AWS. It allows you to test the logic of your function faster.
        Testing locally first reduces the likelihood of identifying issues when testing in the cloud or during deployment,
        which can help you avoid unnecessary costs. Additionally, local testing makes debugging easier to do.

        Returns:
            Dict: Local invoke result and the execution logs
        
---

# Sam Local Invoke

Locally invokes a Lambda function using AWS SAM CLI.

        Requirements:
        - AWS SAM CLI MUST be installed and configured in your environment
        - Docker must be installed and running in your environment.

        This command runs your Lambda function locally in a Docker container that simulates the AWS Lambda environment.
        Use this tool to test your Lambda functions before deploying them to AWS. It allows you to test the logic of your function faster.
        Testing locally first reduces the likelihood of identifying issues when testing in the cloud or during deployment,
        which can help you avoid unnecessary costs. Additionally, local testing makes debugging easier to do.

        Returns:
            Dict: Local invoke result and the execution logs
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `project_directory` | string | Yes | Absolute path to directory containing the SAM project |
| `resource_name` | string | Yes | Name of the Lambda function to invoke locally |
| `template_file` | string | No | Absolute path to the SAM template file (defaults to template.yaml) |
| `event_file` | string | No | Absolute path to a JSON file containing event data |
| `event_data` | string | No | JSON string containing event data (alternative to event_file) |
| `environment_variables_file` | string | No | Absolute path to a JSON file containing environment variables to pass to the function |
| `docker_network` | string | No | Docker network to run the Lambda function in |
| `container_env_vars` | string | No | Environment variables to pass to the container |
| `parameter` | string | No | Override parameters from the template file |
| `log_file` | string | No | Absolute path to a file where the function logs will be written |
| `layer_cache_basedir` | string | No | Directory where the layers will be cached |
| `region` | string | No | AWS region to use (e.g., us-east-1) |
| `profile` | string | No | AWS profile to use |

