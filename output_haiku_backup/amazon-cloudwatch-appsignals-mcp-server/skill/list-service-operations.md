---
name: list-service-operations
description: OPERATION DISCOVERY TOOL - For operation inventory only. Use audit_services() as PRIMARY tool for operation auditing.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the list_service_operations tool in the cloudwatch-applicationsignals-mcp-server instead.

    **IMPORTANT: For operation auditing and performance analysis, use audit_services() as the PRIMARY tool instead.**

    **CRITICAL LIMITATION: This tool only discovers operations that have been ACTIVELY INVOKED in the specified time window.**
    - **Maximum time window: 24 hours** (Application Signals limitation for operation discovery)
    - **No results = No operation invocations** in the time window (operations exist but weren't called)
    - **Empty results do NOT mean operations don't exist** - they may just be inactive
    - **For comprehensive operation analysis regardless of recent activity, use audit_services() instead**

    **RECOMMENDED WORKFLOW FOR OPERATION AUDITING:**
    1. **Use audit_services() FIRST** for comprehensive operation discovery AND performance analysis
    2. **Only use this tool** if you need a simple operation inventory of RECENTLY ACTIVE operations
    3. **audit_services() is more comprehensive** - it discovers operations AND provides performance insights even for inactive operations

    **What this tool provides:**
    - Basic operation inventory (names and available metric types) for RECENTLY INVOKED operations only
    - Operation count and categorization (GET, POST, etc.) for active operations
    - Time range for discovery (max 24 hours)

    **What this tool does NOT provide:**
    - Operations that exist but weren't invoked in the time window
    - Operation performance analysis
    - Latency, error rate, or fault analysis
    - Root cause analysis
    - Actionable recommendations

    **For comprehensive operation auditing, use audit_services() instead:**
    ```
    audit_services(
        service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"your-service"}}}]',
        auditors='all',
    )
    ```

    **OPERATION DISCOVERY USE CASES (when audit_services is not sufficient):**

    1. **Active operation inventory**: When you only need recently invoked operation names without performance data
    2. **Traffic pattern analysis**: To see which operations are currently being used
    3. **Quick active operation count**: To understand current operation activity of a service

    **RECOMMENDED WORKFLOW:**
    1. **Use audit_services() FIRST** for comprehensive operation discovery and analysis
    2. **Only use this tool** for basic inventory of recently active operations if audit_services() provides too much detail

    This tool provides basic operation discovery for ACTIVE operations only, but audit_services() is the primary tool for
    comprehensive operation auditing, performance analysis, and operation insights regardless of recent activity.
    
---

# List Service Operations

OPERATION DISCOVERY TOOL - For operation inventory only. Use audit_services() as PRIMARY tool for operation auditing.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the list_service_operations tool in the cloudwatch-applicationsignals-mcp-server instead.

    **IMPORTANT: For operation auditing and performance analysis, use audit_services() as the PRIMARY tool instead.**

    **CRITICAL LIMITATION: This tool only discovers operations that have been ACTIVELY INVOKED in the specified time window.**
    - **Maximum time window: 24 hours** (Application Signals limitation for operation discovery)
    - **No results = No operation invocations** in the time window (operations exist but weren't called)
    - **Empty results do NOT mean operations don't exist** - they may just be inactive
    - **For comprehensive operation analysis regardless of recent activity, use audit_services() instead**

    **RECOMMENDED WORKFLOW FOR OPERATION AUDITING:**
    1. **Use audit_services() FIRST** for comprehensive operation discovery AND performance analysis
    2. **Only use this tool** if you need a simple operation inventory of RECENTLY ACTIVE operations
    3. **audit_services() is more comprehensive** - it discovers operations AND provides performance insights even for inactive operations

    **What this tool provides:**
    - Basic operation inventory (names and available metric types) for RECENTLY INVOKED operations only
    - Operation count and categorization (GET, POST, etc.) for active operations
    - Time range for discovery (max 24 hours)

    **What this tool does NOT provide:**
    - Operations that exist but weren't invoked in the time window
    - Operation performance analysis
    - Latency, error rate, or fault analysis
    - Root cause analysis
    - Actionable recommendations

    **For comprehensive operation auditing, use audit_services() instead:**
    ```
    audit_services(
        service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"your-service"}}}]',
        auditors='all',
    )
    ```

    **OPERATION DISCOVERY USE CASES (when audit_services is not sufficient):**

    1. **Active operation inventory**: When you only need recently invoked operation names without performance data
    2. **Traffic pattern analysis**: To see which operations are currently being used
    3. **Quick active operation count**: To understand current operation activity of a service

    **RECOMMENDED WORKFLOW:**
    1. **Use audit_services() FIRST** for comprehensive operation discovery and analysis
    2. **Only use this tool** for basic inventory of recently active operations if audit_services() provides too much detail

    This tool provides basic operation discovery for ACTIVE operations only, but audit_services() is the primary tool for
    comprehensive operation auditing, performance analysis, and operation insights regardless of recent activity.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `service_name` | string | Yes | Name of the service to list operations for (case-sensitive) |
| `hours` | integer | No | Number of hours to look back for operation discovery (default 24, max 24 for Application Signals operation discovery) |

## AWS CLI

```bash
aws cloudwatch list-service-operations --service-name <service_name> --hours <hours>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.list_service_operations(
    ServiceName=service_name,
    Hours=hours,
)
```
