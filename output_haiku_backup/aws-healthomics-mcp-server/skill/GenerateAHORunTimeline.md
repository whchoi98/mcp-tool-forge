---
name: GenerateAHORunTimeline
description: Generate a Gantt-style timeline visualization for an AWS HealthOmics workflow run.

    This tool creates an SVG Gantt chart showing task execution phases (pending and running)
    with status-based coloring. The chart helps visualize task parallelism and identify
    bottlenecks in workflow execution.

    Use this tool when users ask about:
    - "Show me a timeline of my workflow run"
    - "Visualize the execution of my HealthOmics workflow"
    - "Create a Gantt chart for my run"
    - "How did my tasks execute over time?"
    - "What was the parallelism in my workflow?"

    The chart displays:
    - Pending/starting phase (light grey bars)
    - Running phase (colored by status: blue=COMPLETED, red=FAILED, orange=CANCELLED)
    - Interactive tooltips with task details (name, CPUs, memory, instance type, cost)
    - Time axis with configurable units (seconds, minutes, hours, days)

    Args:
        ctx: MCP request context for error reporting
        run_id: The run ID to generate timeline for
        time_unit: Time unit for the timeline axis (sec, min, hr, day)
        region: AWS region for pricing lookups
        output_format: Output format (svg or base64)

    Returns:
        SVG string or base64-encoded SVG representing the Gantt chart timeline
    
---

# Generateahoruntimeline

Generate a Gantt-style timeline visualization for an AWS HealthOmics workflow run.

    This tool creates an SVG Gantt chart showing task execution phases (pending and running)
    with status-based coloring. The chart helps visualize task parallelism and identify
    bottlenecks in workflow execution.

    Use this tool when users ask about:
    - "Show me a timeline of my workflow run"
    - "Visualize the execution of my HealthOmics workflow"
    - "Create a Gantt chart for my run"
    - "How did my tasks execute over time?"
    - "What was the parallelism in my workflow?"

    The chart displays:
    - Pending/starting phase (light grey bars)
    - Running phase (colored by status: blue=COMPLETED, red=FAILED, orange=CANCELLED)
    - Interactive tooltips with task details (name, CPUs, memory, instance type, cost)
    - Time axis with configurable units (seconds, minutes, hours, days)

    Args:
        ctx: MCP request context for error reporting
        run_id: The run ID to generate timeline for
        time_unit: Time unit for the timeline axis (sec, min, hr, day)
        region: AWS region for pricing lookups
        output_format: Output format (svg or base64)

    Returns:
        SVG string or base64-encoded SVG representing the Gantt chart timeline
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run_id` | string | Yes | The run ID to generate timeline for. |
| `time_unit` | string | No | Time unit for the timeline axis. Valid values: sec, min, hr, day. Defaults to hr. |
| `region` | string | No | AWS region for pricing lookups. Defaults to us-east-1. |
| `output_format` | string | No | Output format for the SVG. Valid values: svg (raw SVG string), base64 (base64-encoded SVG for easier extraction). Defaults to base64. |

