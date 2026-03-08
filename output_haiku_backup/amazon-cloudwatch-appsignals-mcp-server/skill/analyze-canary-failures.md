---
name: analyze-canary-failures
description: Comprehensive canary failure analysis with deep dive into issues.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the analyze_canary_failures tool in the cloudwatch-applicationsignals-mcp-server instead.

    Use this tool to:
    - Deep dive into canary failures with root cause identification
    - Analyze historical patterns and specific incident details
    - Get comprehensive artifact analysis including logs, screenshots, and HAR files
    - Receive actionable recommendations based on AWS debugging methodology
    - Correlate canary failures with Application Signals telemetry data
    - Identify performance degradation and availability issues across service dependencies

    Key Features:
    - **Failure Pattern Analysis**: Identifies recurring failure modes and temporal patterns
    - **Artifact Deep Dive**: Analyzes canary logs, screenshots, and network traces for root causes
    - **Service Correlation**: Links canary failures to upstream/downstream service issues using Application Signals
    - **Performance Insights**: Detects latency spikes, fault rates, and connection issues
    - **Actionable Remediation**: Provides specific steps based on AWS operational best practices

    Common Use Cases:
    1. **Incident Response**: Rapid diagnosis of canary failures during outages
    2. **Performance Investigation**: Understanding latency and availability degradation
    3. **Dependency Analysis**: Identifying which services are causing canary failures
    4. **Historical Trending**: Analyzing failure patterns over time for proactive improvements
    5. **Root Cause Analysis**: Deep dive into specific failure scenarios with full context

    Output Includes:
    - Severity-ranked findings with immediate action items
    - Service-level telemetry insights with trace analysis
    - Exception details and stack traces from canary artifacts
    - Network connectivity and performance metrics
    - Correlation with Application Signals audit findings
    - Historical failure patterns and recovery recommendations

    Args:
        canary_name (str): Name of the CloudWatch Synthetics canary to analyze
        region (str, optional): AWS region where the canary is deployed.

    Returns:
        dict: Comprehensive failure analysis containing:
            - Failure severity assessment and immediate recommendations
            - Detailed artifact analysis (logs, screenshots, HAR files)
            - Service dependency health and performance metrics
            - Root cause identification with specific remediation steps
            - Historical pattern analysis and trend insights
    
---

# Analyze Canary Failures

Comprehensive canary failure analysis with deep dive into issues.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the analyze_canary_failures tool in the cloudwatch-applicationsignals-mcp-server instead.

    Use this tool to:
    - Deep dive into canary failures with root cause identification
    - Analyze historical patterns and specific incident details
    - Get comprehensive artifact analysis including logs, screenshots, and HAR files
    - Receive actionable recommendations based on AWS debugging methodology
    - Correlate canary failures with Application Signals telemetry data
    - Identify performance degradation and availability issues across service dependencies

    Key Features:
    - **Failure Pattern Analysis**: Identifies recurring failure modes and temporal patterns
    - **Artifact Deep Dive**: Analyzes canary logs, screenshots, and network traces for root causes
    - **Service Correlation**: Links canary failures to upstream/downstream service issues using Application Signals
    - **Performance Insights**: Detects latency spikes, fault rates, and connection issues
    - **Actionable Remediation**: Provides specific steps based on AWS operational best practices

    Common Use Cases:
    1. **Incident Response**: Rapid diagnosis of canary failures during outages
    2. **Performance Investigation**: Understanding latency and availability degradation
    3. **Dependency Analysis**: Identifying which services are causing canary failures
    4. **Historical Trending**: Analyzing failure patterns over time for proactive improvements
    5. **Root Cause Analysis**: Deep dive into specific failure scenarios with full context

    Output Includes:
    - Severity-ranked findings with immediate action items
    - Service-level telemetry insights with trace analysis
    - Exception details and stack traces from canary artifacts
    - Network connectivity and performance metrics
    - Correlation with Application Signals audit findings
    - Historical failure patterns and recovery recommendations

    Args:
        canary_name (str): Name of the CloudWatch Synthetics canary to analyze
        region (str, optional): AWS region where the canary is deployed.

    Returns:
        dict: Comprehensive failure analysis containing:
            - Failure severity assessment and immediate recommendations
            - Detailed artifact analysis (logs, screenshots, HAR files)
            - Service dependency health and performance metrics
            - Root cause identification with specific remediation steps
            - Historical pattern analysis and trend insights
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `canary_name` | string | Yes |  |
| `region` | string | No |  |

## AWS CLI

```bash
aws cloudwatch describe-canaries-last-run --canary-name <canary_name> --region <region>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.describe_canaries_last_run(
    CanaryName=canary_name,
    RegionName=region,
)
```
