---
name: AnalyzeAHORunPerformance
description: Analyze AWS HealthOmics workflow run performance and provide optimization recommendations.

    This tool analyzes HealthOmics workflow runs to help users optimize:
    - Resource utilization patterns (CPU, memory)
    - Cost optimization opportunities
    - Performance bottlenecks
    - Resource allocation efficiency
    - Runtime optimization suggestions

    Use this tool when users ask about:
    - "How can I optimize my HealthOmics runs?"
    - "Why is my workflow using too many resources?"
    - "How can I reduce costs for my genomic workflows?"
    - "What resources are being wasted in my runs?"
    - "How can I improve workflow performance?"

    The tool summarizes run manifest logs containing task-level metrics
    and provides a structured report with recommendations for optimization.

    Args:
        ctx: MCP request context for error reporting
        run_ids: List of run IDs to analyze for optimization
        headroom: Headroom percentage for instance recommendations (default 0.20 = 20%)
        detailed: Include detailed task metrics JSON section (default False)

    Returns:
        Formatted analysis string with structured manifest data and optimization recommendations
    
---

# Analyzeahorunperformance

Analyze AWS HealthOmics workflow run performance and provide optimization recommendations.

    This tool analyzes HealthOmics workflow runs to help users optimize:
    - Resource utilization patterns (CPU, memory)
    - Cost optimization opportunities
    - Performance bottlenecks
    - Resource allocation efficiency
    - Runtime optimization suggestions

    Use this tool when users ask about:
    - "How can I optimize my HealthOmics runs?"
    - "Why is my workflow using too many resources?"
    - "How can I reduce costs for my genomic workflows?"
    - "What resources are being wasted in my runs?"
    - "How can I improve workflow performance?"

    The tool summarizes run manifest logs containing task-level metrics
    and provides a structured report with recommendations for optimization.

    Args:
        ctx: MCP request context for error reporting
        run_ids: List of run IDs to analyze for optimization
        headroom: Headroom percentage for instance recommendations (default 0.20 = 20%)
        detailed: Include detailed task metrics JSON section (default False)

    Returns:
        Formatted analysis string with structured manifest data and optimization recommendations
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_ids` | string | Yes | List of run IDs to analyze for resource optimization. Can be provided as a JSON array string like ["run1", "run2"] or as a comma-separated string like "run1,run2" |
| `headroom` | number | No | Headroom percentage for instance recommendations (0.0 to 1.0). Default is 0.20 (20%). This adds a buffer to recommended instance sizes to prevent over-optimization. Set this value to 0 for aggressive optimization |
| `detailed` | boolean | No | Include very detailed task metrics in the report. Typically this is only required for granular analysis and can consume a large number of tokens in the agents context window. Default is False. |

