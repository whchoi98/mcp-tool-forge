---
name: list-monitored-services
description: OPTIONAL TOOL for service discovery - audit_services() can automatically discover services using wildcard patterns.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the list_monitored_services tool in the cloudwatch-applicationsignals-mcp-server instead.

    **IMPORTANT: For service auditing and operation analysis, use audit_services() as the PRIMARY tool instead.**

    **WHEN TO USE THIS TOOL:**
    - Getting a detailed overview of all monitored services in your environment
    - Discovering specific service names and environments for manual audit target construction
    - Understanding the complete service inventory before targeted analysis
    - When you need detailed service attributes beyond what wildcard expansion provides

    **RECOMMENDED WORKFLOW FOR SERVICE AND OPERATION AUDITING:**
    1. **Use audit_services() FIRST** with wildcard patterns for comprehensive service discovery AND analysis
    2. **Only use this tool** if you need basic service inventory without performance analysis
    3. **audit_services() is more comprehensive** - it discovers services AND provides performance insights

    **AUTOMATIC SERVICE DISCOVERY IN AUDIT:**
    The `audit_services()` tool automatically discovers services when you use wildcard patterns:
    - `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]` - Audits all services
    - `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]` - Audits services with "payment" in the name

    **What this tool provides:**
    - Basic service inventory (names, types, environments)
    - Service count and categorization
    - Key attributes for manual target construction

    **What this tool does NOT provide:**
    - Service performance analysis
    - Operation discovery and analysis
    - Root cause analysis
    - Actionable recommendations

    **For comprehensive service auditing, use audit_services() instead:**
    ```
    audit_services(
        service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]',
        auditors='all',
    )
    ```

    Returns a formatted list showing:
    - Service name and type
    - Key attributes (Name, Environment, Platform, etc.)
    - Total count of services

    **NOTE**: For operation auditing, use audit_services() as the primary tool instead of get_service_detail() or list_service_operations().
    
---

# List Monitored Services

OPTIONAL TOOL for service discovery - audit_services() can automatically discover services using wildcard patterns.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the list_monitored_services tool in the cloudwatch-applicationsignals-mcp-server instead.

    **IMPORTANT: For service auditing and operation analysis, use audit_services() as the PRIMARY tool instead.**

    **WHEN TO USE THIS TOOL:**
    - Getting a detailed overview of all monitored services in your environment
    - Discovering specific service names and environments for manual audit target construction
    - Understanding the complete service inventory before targeted analysis
    - When you need detailed service attributes beyond what wildcard expansion provides

    **RECOMMENDED WORKFLOW FOR SERVICE AND OPERATION AUDITING:**
    1. **Use audit_services() FIRST** with wildcard patterns for comprehensive service discovery AND analysis
    2. **Only use this tool** if you need basic service inventory without performance analysis
    3. **audit_services() is more comprehensive** - it discovers services AND provides performance insights

    **AUTOMATIC SERVICE DISCOVERY IN AUDIT:**
    The `audit_services()` tool automatically discovers services when you use wildcard patterns:
    - `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]` - Audits all services
    - `[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*payment*"}}}]` - Audits services with "payment" in the name

    **What this tool provides:**
    - Basic service inventory (names, types, environments)
    - Service count and categorization
    - Key attributes for manual target construction

    **What this tool does NOT provide:**
    - Service performance analysis
    - Operation discovery and analysis
    - Root cause analysis
    - Actionable recommendations

    **For comprehensive service auditing, use audit_services() instead:**
    ```
    audit_services(
        service_targets='[{"Type":"service","Data":{"Service":{"Type":"Service","Name":"*"}}}]',
        auditors='all',
    )
    ```

    Returns a formatted list showing:
    - Service name and type
    - Key attributes (Name, Environment, Platform, etc.)
    - Total count of services

    **NOTE**: For operation auditing, use audit_services() as the primary tool instead of get_service_detail() or list_service_operations().
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

