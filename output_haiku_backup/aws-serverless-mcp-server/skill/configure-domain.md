---
name: configure-domain
description: Configures a custom domain for a deployed web application on AWS Serverless.

        Before using this tool, you must already own the domain name and have a Route53 hosted zone in your account.
        This tool does not register domain names.
        This tool sets up Route 53 DNS records, ACM certificates, and CloudFront custom domain mappings as needed.
        Use this tool after deploying your web application to associate it with your own domain name.

        Returns:
            Dict: Domain configuration result
        
---

# Configure Domain

Configures a custom domain for a deployed web application on AWS Serverless.

        Before using this tool, you must already own the domain name and have a Route53 hosted zone in your account.
        This tool does not register domain names.
        This tool sets up Route 53 DNS records, ACM certificates, and CloudFront custom domain mappings as needed.
        Use this tool after deploying your web application to associate it with your own domain name.

        Returns:
            Dict: Domain configuration result
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `project_name` | string | Yes | Project name |
| `domain_name` | string | Yes | Custom domain name to use for the CloudFront distribution . You must already own the domain name
            and have a Route 53 hosted zone in your account. This tool does not register domain names. |
| `create_certificate` | string | No | Whether to create a ACM certificate |
| `create_route53_record` | string | No | Whether to create a Route 53 record. When set to True, this tool creates a DNS A record
                that points to the CloudFront distribution associated with this project |
| `region` | string | No | AWS region to use (e.g., us-east-1) |

