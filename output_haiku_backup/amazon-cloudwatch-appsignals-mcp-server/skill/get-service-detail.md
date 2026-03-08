---
name: get-service-detail
description: Get detailed information about a specific Application Signals service.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the get_service_detail tool in the cloudwatch-applicationsignals-mcp-server instead.

    **IMPORTANT: For operation auditing, use audit_services() as the PRIMARY tool instead.**

    **RECOMMENDED WORKFLOW FOR OPERATION AUDITING:**
    1. **Use audit_services() FIRST** for comprehensive operation discovery and analysis
    2. **Only use this tool** for basic service metadata and configuration details
    3. **This tool does NOT provide operation names** - it only shows service-level metrics

    **What this tool provides:**
    - Service metadata and configuration
    - Platform information (EKS, Lambda, etc.)
    - Service-level metrics (Latency, Error, Fault aggregates)
    - Log groups associated with the service
    - Key attributes (Type, Environment, Platform)

    **What this tool does NOT provide:**
    - Operation names (GET, POST, etc.)
    - Operation-specific metrics
    - Operation-level performance data

    **For operation auditing, use audit_services() instead:**
    ```
    audit_services(
        service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"your-service"}}}]',
        auditors='all',
    )
    ```

    This tool is useful for understanding service deployment details and basic configuration,
    but audit_services() is the primary tool for operation discovery and performance analysis.
    
---

# Get Service Detail

Get detailed information about a specific Application Signals service.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the get_service_detail tool in the cloudwatch-applicationsignals-mcp-server instead.

    **IMPORTANT: For operation auditing, use audit_services() as the PRIMARY tool instead.**

    **RECOMMENDED WORKFLOW FOR OPERATION AUDITING:**
    1. **Use audit_services() FIRST** for comprehensive operation discovery and analysis
    2. **Only use this tool** for basic service metadata and configuration details
    3. **This tool does NOT provide operation names** - it only shows service-level metrics

    **What this tool provides:**
    - Service metadata and configuration
    - Platform information (EKS, Lambda, etc.)
    - Service-level metrics (Latency, Error, Fault aggregates)
    - Log groups associated with the service
    - Key attributes (Type, Environment, Platform)

    **What this tool does NOT provide:**
    - Operation names (GET, POST, etc.)
    - Operation-specific metrics
    - Operation-level performance data

    **For operation auditing, use audit_services() instead:**
    ```
    audit_services(
        service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"your-service"}}}]',
        auditors='all',
    )
    ```

    This tool is useful for understanding service deployment details and basic configuration,
    but audit_services() is the primary tool for operation discovery and performance analysis.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `service_name` | string | Yes | Name of the service to get details for (case-sensitive) |

## AWS CLI

```bash
aws cloudwatch describe-services --service-name <service_name>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.describe_services(
    ServiceName=service_name,
)
```
