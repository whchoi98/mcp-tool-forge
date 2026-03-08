---
name: sam-build
description: Builds a serverless application using AWS SAM (Serverless Application Model) CLI.

        Requirements:
        - AWS SAM CLI MUST be installed and configured in your environment
        - An application MUST already be initialized with 'sam_init' tool to create sam project structure.

        This command compiles your Lambda function and layer code, creates deployment artifacts, and prepares your application for deployment and local testing.
        It creates a .aws-sam directory that structures your application in a format and location that sam local and sam deploy require. For Zip
        functions, a .zip file archive is created, which contains your application code and its dependencies. For Image functions, a container image is created,
        which includes the base operating system, runtime, and extensions, in addition to your application code and its dependencies.

        By default, the functions and layers are built in parallel for faster builds.

        Usage tips:
        - Don't edit any code under the .aws-sam/build directory. Instead, update your original source code in
        your project folder and run sam build to update the .aws-sam/build directory.
        - When you modify your original files, run sam build to update the .aws-sam/build directory.
        - You may want the AWS SAM CLI to reference your project's original root directory
        instead of the .aws-sam directory, such as when developing and testing with sam local. Delete the .aws-sam directory
        or the AWS SAM template in the .aws-sam directory to have the AWS SAM CLI recognize your original project directory as
        the root project directory. When ready, run sam build again to create the .aws-sam directory.
        - When you run sam build, the .aws-sam/build directory gets overwritten each time.
        The .aws-sam directory does not. If you want to store files, such as logs, store them in .aws-sam to
        prevent them from being overwritten.

        Returns:
            Dict: SAM init command output
        
---

# Sam Build

Builds a serverless application using AWS SAM (Serverless Application Model) CLI.

        Requirements:
        - AWS SAM CLI MUST be installed and configured in your environment
        - An application MUST already be initialized with 'sam_init' tool to create sam project structure.

        This command compiles your Lambda function and layer code, creates deployment artifacts, and prepares your application for deployment and local testing.
        It creates a .aws-sam directory that structures your application in a format and location that sam local and sam deploy require. For Zip
        functions, a .zip file archive is created, which contains your application code and its dependencies. For Image functions, a container image is created,
        which includes the base operating system, runtime, and extensions, in addition to your application code and its dependencies.

        By default, the functions and layers are built in parallel for faster builds.

        Usage tips:
        - Don't edit any code under the .aws-sam/build directory. Instead, update your original source code in
        your project folder and run sam build to update the .aws-sam/build directory.
        - When you modify your original files, run sam build to update the .aws-sam/build directory.
        - You may want the AWS SAM CLI to reference your project's original root directory
        instead of the .aws-sam directory, such as when developing and testing with sam local. Delete the .aws-sam directory
        or the AWS SAM template in the .aws-sam directory to have the AWS SAM CLI recognize your original project directory as
        the root project directory. When ready, run sam build again to create the .aws-sam directory.
        - When you run sam build, the .aws-sam/build directory gets overwritten each time.
        The .aws-sam directory does not. If you want to store files, such as logs, store them in .aws-sam to
        prevent them from being overwritten.

        Returns:
            Dict: SAM init command output
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `project_directory` | string | Yes | Absolute path to directory containing the SAM project |
| `template_file` | string | No | Absolute path to the template file (defaults to template.yaml) |
| `base_dir` | string | No | Resolve relative paths to function's source code with respect to this folder.
             Use this option if you want to change how relative paths to source code folders are resolved.
             By default, relative paths are resolved with respect to the AWS SAM template's location. |
| `build_dir` | string | No | The absolute path to a directory where the built artifacts are stored
                This directory and all of its content are removed with this option |
| `use_container` | boolean | No | Use a Lambda-like container to build the function. Use this option if your function requires a specific
                runtime environment or dependencies that are not available on the local machine. Docker must be installed |
| `no_use_container` | boolean | No | Run build in local machine instead of Docker container. |
| `parallel` | boolean | No | Build your AWS SAM application in parallel. |
| `container_env_vars` | string | No | Environment variables to pass to the build container.
                Each instance takes a key-value pair, where the key is the resource and environment variable, and the
                value is the environment variable's value.
                For example: --container-env-var Function1.GITHUB_TOKEN=TOKEN1 --container-env-var Function2.GITHUB_TOKEN=TOKEN2. |
| `container_env_var_file` | string | No | Absolute path to a JSON file containing container environment variables. You can provide a single environment variable that applies to all serverless resources,
                or different environment variables for each resource.
                For example, for all resources:
                {
                    "Parameters": {
                        "GITHUB_TOKEN": "TOKEN_GLOBAL"
                    }
                }
                For individual resources:
                {
                    "MyFunction1": {
                        "GITHUB_TOKEN": "TOKEN1"
                    },
                    "MyFunction2": {
                        "GITHUB_TOKEN": "TOKEN2"
                    }
                }
                 |
| `build_image` | string | No | The URI of the container image that you want to pull for the build. By default, AWS SAM pulls the
             container image from Amazon ECR Public. Use this option to pull the image from another location |
| `debug` | boolean | No | Turn on debug logging |
| `manifest` | string | No | Absolute path to a custom dependency manifest file (e.g., package.json) instead of the default.
             For example: 'ParameterKey=KeyPairName, ParameterValue=MyKey ParameterKey=InstanceType, ParameterValue=t1.micro. |
| `parameter_overrides` | string | No | CloudFormation parameter overrides encoded as key-value pairs.
                For example: 'ParameterKey=KeyPairName, ParameterValue=MyKey ParameterKey=InstanceType, ParameterValue=t1.micro |
| `region` | string | No | AWS Region to deploy to (e.g., us-east-1) |
| `save_params` | boolean | No | Save parameters to the SAM configuration file |
| `profile` | string | No | AWS profile to use |

