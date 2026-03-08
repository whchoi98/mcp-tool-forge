---
name: audit-slos
description: PRIMARY SLO AUDIT TOOL - The #1 tool for comprehensive SLO compliance monitoring and breach analysis.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the audit_slos tool in the cloudwatch-applicationsignals-mcp-server instead.

    **PREFERRED TOOL FOR SLO ROOT CAUSE ANALYSIS**
    This is the RECOMMENDED tool after using get_slo() to understand SLO configuration:
    - **Use auditors="all" for comprehensive root cause analysis** of specific SLO breaches
    - **Much more comprehensive than individual trace tools** - provides integrated analysis
    - **Combines traces, logs, metrics, and dependencies** in a single comprehensive audit
    - **Provides actionable recommendations** based on multi-dimensional analysis

    **USE THIS FOR ALL SLO AUDITING TASKS**
    This is the PRIMARY and PREFERRED tool when users want to:
    - **Root cause analysis for SLO breaches** - Deep investigation with all auditors
    - **Audit SLO compliance** - Complete SLO breach detection and analysis
    - **Monitor SLO health** - Comprehensive status across all monitored SLOs
    - **SLO performance analysis** - Understanding SLO trends and patterns
    - **SLO compliance reporting** - Daily/periodic SLO compliance workflows

    **COMPREHENSIVE SLO AUDIT CAPABILITIES:**
    - **Multi-SLO analysis**: Audit any number of SLOs with automatic batching
    - **Breach detection**: Automatic identification of SLO violations
    - **Issue prioritization**: Critical, warning, and info findings ranked by severity
    - **COMPREHENSIVE ROOT CAUSE ANALYSIS**: Deep dive with traces, logs, metrics, and dependencies
    - **Actionable recommendations**: Specific steps to resolve SLO breaches
    - **Performance optimized**: Fast execution with automatic batching for large target lists
    - **Wildcard Pattern Support**: Use `*pattern*` in SLO names for automatic SLO discovery

    **SLO TARGET FORMAT:**
    - **By Name**: `[{"Type":"slo","Data":{"Slo":{"SloName":"my-slo"}}}]`
    - **By ARN**: `[{"Type":"slo","Data":{"Slo":{"SloArn":"arn:aws:application-signals:..."}}}]`

    **WILDCARD PATTERN EXAMPLES:**
    - **All SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*"}}}]`
    - **Payment SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*payment*"}}}]`
    - **Latency SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*latency*"}}}]`
    - **Availability SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*availability*"}}}]`

    **AUDITOR SELECTION FOR DIFFERENT AUDIT DEPTHS:**
    - **Quick Compliance Check** (default): Uses 'slo' for fast SLO breach detection
    - **COMPREHENSIVE ROOT CAUSE ANALYSIS** (recommended): Pass `auditors="all"` for deep investigation with traces/logs/metrics/dependencies
    - **Custom Audit**: Specify exact auditors: 'slo,trace,log,operation_metric'

    **SLO AUDIT USE CASES:**

    4. **Audit all SLOs**:
       `slo_targets='[{"Type":"slo","Data":{"Slo":{"SloName":"*"}}}]'`

    22. **Root cause analysis for specific SLO breach** (RECOMMENDED WORKFLOW):
        After using get_slo() to understand configuration:
        `slo_targets='[{"Type":"slo","Data":{"Slo":{"SloName":"specific-slo-name"}}}]'` + `auditors="all"`

    14. **Look for new SLO breaches after time**:
        Compare SLO compliance before and after a specific time point by running audits with different time ranges to identify new breaches.

    **TYPICAL SLO AUDIT WORKFLOWS:**
    1. **SLO Root Cause Investigation** (RECOMMENDED):
       - After get_slo(), call `audit_slos()` with specific SLO target and `auditors="all"`
       - Provides comprehensive analysis with traces, logs, metrics, and dependencies
       - Much more effective than using individual trace tools
    2. **Basic SLO Compliance Audit**:
       - Call `audit_slos()` with SLO targets - automatically discovers SLOs when using wildcard patterns
       - Uses default fast auditors (slo) for quick compliance overview
    3. **Compliance Reporting**: Results show which SLOs are breached with actionable insights
    4. **Automatic SLO Discovery**: Wildcard patterns in SLO names automatically discover and expand to concrete SLOs

    **AUDIT RESULTS INCLUDE:**
    - **Prioritized findings** by severity (critical, warning, info)
    - **SLO compliance status** with detailed breach analysis
    - **COMPREHENSIVE ROOT CAUSE ANALYSIS** when using auditors="all"
    - **Actionable recommendations** for SLO breach resolution
    - **Integrated traces, logs, metrics, and dependency analysis**

    **IMPORTANT: This tool provides comprehensive SLO audit coverage and should be your first choice for any SLO compliance auditing and root cause analysis.**

    **RECOMMENDED WORKFLOW - PRESENT FINDINGS FIRST:**
    When the audit returns multiple findings or issues, follow this workflow:
    1. **Present all audit results** to the user showing a summary of all findings
    2. **Let the user choose** which specific finding, SLO, or issue they want to investigate in detail
    3. **Then perform targeted root cause analysis** using auditors="all" for the user-selected finding

    **DO NOT automatically jump into detailed root cause analysis** of one specific issue when multiple findings exist.
    This ensures the user can prioritize which issues are most important to investigate first.

    **Example workflow:**
    - First call: `audit_slos()` with default auditors for compliance overview
    - Present findings summary to user
    - User selects specific SLO breach to investigate
    - Follow-up call: `audit_slos()` with `auditors="all"` for selected SLO only
    
---

# Audit Slos

PRIMARY SLO AUDIT TOOL - The #1 tool for comprehensive SLO compliance monitoring and breach analysis.

    **IMPORTANT**: This tool and server is being deprecated. If available, please use the audit_slos tool in the cloudwatch-applicationsignals-mcp-server instead.

    **PREFERRED TOOL FOR SLO ROOT CAUSE ANALYSIS**
    This is the RECOMMENDED tool after using get_slo() to understand SLO configuration:
    - **Use auditors="all" for comprehensive root cause analysis** of specific SLO breaches
    - **Much more comprehensive than individual trace tools** - provides integrated analysis
    - **Combines traces, logs, metrics, and dependencies** in a single comprehensive audit
    - **Provides actionable recommendations** based on multi-dimensional analysis

    **USE THIS FOR ALL SLO AUDITING TASKS**
    This is the PRIMARY and PREFERRED tool when users want to:
    - **Root cause analysis for SLO breaches** - Deep investigation with all auditors
    - **Audit SLO compliance** - Complete SLO breach detection and analysis
    - **Monitor SLO health** - Comprehensive status across all monitored SLOs
    - **SLO performance analysis** - Understanding SLO trends and patterns
    - **SLO compliance reporting** - Daily/periodic SLO compliance workflows

    **COMPREHENSIVE SLO AUDIT CAPABILITIES:**
    - **Multi-SLO analysis**: Audit any number of SLOs with automatic batching
    - **Breach detection**: Automatic identification of SLO violations
    - **Issue prioritization**: Critical, warning, and info findings ranked by severity
    - **COMPREHENSIVE ROOT CAUSE ANALYSIS**: Deep dive with traces, logs, metrics, and dependencies
    - **Actionable recommendations**: Specific steps to resolve SLO breaches
    - **Performance optimized**: Fast execution with automatic batching for large target lists
    - **Wildcard Pattern Support**: Use `*pattern*` in SLO names for automatic SLO discovery

    **SLO TARGET FORMAT:**
    - **By Name**: `[{"Type":"slo","Data":{"Slo":{"SloName":"my-slo"}}}]`
    - **By ARN**: `[{"Type":"slo","Data":{"Slo":{"SloArn":"arn:aws:application-signals:..."}}}]`

    **WILDCARD PATTERN EXAMPLES:**
    - **All SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*"}}}]`
    - **Payment SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*payment*"}}}]`
    - **Latency SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*latency*"}}}]`
    - **Availability SLOs**: `[{"Type":"slo","Data":{"Slo":{"SloName":"*availability*"}}}]`

    **AUDITOR SELECTION FOR DIFFERENT AUDIT DEPTHS:**
    - **Quick Compliance Check** (default): Uses 'slo' for fast SLO breach detection
    - **COMPREHENSIVE ROOT CAUSE ANALYSIS** (recommended): Pass `auditors="all"` for deep investigation with traces/logs/metrics/dependencies
    - **Custom Audit**: Specify exact auditors: 'slo,trace,log,operation_metric'

    **SLO AUDIT USE CASES:**

    4. **Audit all SLOs**:
       `slo_targets='[{"Type":"slo","Data":{"Slo":{"SloName":"*"}}}]'`

    22. **Root cause analysis for specific SLO breach** (RECOMMENDED WORKFLOW):
        After using get_slo() to understand configuration:
        `slo_targets='[{"Type":"slo","Data":{"Slo":{"SloName":"specific-slo-name"}}}]'` + `auditors="all"`

    14. **Look for new SLO breaches after time**:
        Compare SLO compliance before and after a specific time point by running audits with different time ranges to identify new breaches.

    **TYPICAL SLO AUDIT WORKFLOWS:**
    1. **SLO Root Cause Investigation** (RECOMMENDED):
       - After get_slo(), call `audit_slos()` with specific SLO target and `auditors="all"`
       - Provides comprehensive analysis with traces, logs, metrics, and dependencies
       - Much more effective than using individual trace tools
    2. **Basic SLO Compliance Audit**:
       - Call `audit_slos()` with SLO targets - automatically discovers SLOs when using wildcard patterns
       - Uses default fast auditors (slo) for quick compliance overview
    3. **Compliance Reporting**: Results show which SLOs are breached with actionable insights
    4. **Automatic SLO Discovery**: Wildcard patterns in SLO names automatically discover and expand to concrete SLOs

    **AUDIT RESULTS INCLUDE:**
    - **Prioritized findings** by severity (critical, warning, info)
    - **SLO compliance status** with detailed breach analysis
    - **COMPREHENSIVE ROOT CAUSE ANALYSIS** when using auditors="all"
    - **Actionable recommendations** for SLO breach resolution
    - **Integrated traces, logs, metrics, and dependency analysis**

    **IMPORTANT: This tool provides comprehensive SLO audit coverage and should be your first choice for any SLO compliance auditing and root cause analysis.**

    **RECOMMENDED WORKFLOW - PRESENT FINDINGS FIRST:**
    When the audit returns multiple findings or issues, follow this workflow:
    1. **Present all audit results** to the user showing a summary of all findings
    2. **Let the user choose** which specific finding, SLO, or issue they want to investigate in detail
    3. **Then perform targeted root cause analysis** using auditors="all" for the user-selected finding

    **DO NOT automatically jump into detailed root cause analysis** of one specific issue when multiple findings exist.
    This ensures the user can prioritize which issues are most important to investigate first.

    **Example workflow:**
    - First call: `audit_slos()` with default auditors for compliance overview
    - Present findings summary to user
    - User selects specific SLO breach to investigate
    - Follow-up call: `audit_slos()` with `auditors="all"` for selected SLO only
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `slo_targets` | string | Yes | REQUIRED. JSON array of SLO targets. Supports wildcard patterns like '*payment*' for automatic SLO discovery. Format: [{'Type':'slo','Data':{'Slo':{'SloName':'slo-name'}}}] or [{'Type':'slo','Data':{'Slo':{'SloArn':'arn:aws:...'}}}]. Large target lists are automatically processed in batches. |
| `start_time` | string | No | Start time (unix seconds or 'YYYY-MM-DD HH:MM:SS'). Defaults to now-24h UTC. |
| `end_time` | string | No | End time (unix seconds or 'YYYY-MM-DD HH:MM:SS'). Defaults to now UTC. |
| `auditors` | string | No | Optional. Comma-separated auditors (e.g., 'slo,trace,log'). Defaults to 'slo' for fast SLO compliance auditing. Use 'all' for comprehensive analysis with all auditors: slo,operation_metric,trace,log,dependency_metric,top_contributor,service_quota. |

## AWS CLI

```bash
aws cloudwatch get-slo-compliance --slo-targets <slo_targets> --start-time <start_time> --end-time <end_time> --auditors <auditors>
```

## boto3

```python
import boto3

client = boto3.client('cloudwatch')
response = client.get_slo_compliance(
    SloTargets=slo_targets,
    StartTime=start_time,
    EndTime=end_time,
    Auditors=auditors,
)
```
