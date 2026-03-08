---
name: get-diagram-examples
description: Get example code for different types of diagrams.

    This tool provides ready-to-use example code for various diagram types.
    Use these examples to understand the syntax and capabilities of the diagrams package
    before creating your own custom diagrams.

    USAGE INSTRUCTIONS:
    1. Select the diagram type you're interested in (or 'all' to see all examples)
    2. Study the returned examples to understand the structure and syntax
    3. Use these examples as templates for your own diagrams
    4. When ready, modify an example or write your own code and use generate_diagram

    EXAMPLE CATEGORIES:
    - aws: AWS cloud architecture diagrams (basic services, grouped workers, clustered web services, Bedrock)
    - sequence: Process and interaction flow diagrams
    - flow: Decision trees and workflow diagrams
    - class: Object relationship and inheritance diagrams
    - k8s: Kubernetes architecture diagrams
    - onprem: On-premises infrastructure diagrams
    - custom: Custom diagrams with custom icons
    - all: All available examples across categories

    Each example demonstrates different features of the diagrams package:
    - Basic connections between components
    - Grouping with Clusters
    - Advanced styling with Edge attributes
    - Different layout directions
    - Multiple component instances
    - Custom icons and nodes

    Parameters:
        diagram_type (str): Type of diagram example to return. Options: aws, sequence, flow, class, k8s, onprem, custom, all

    Returns:
        Dictionary with example code for the requested diagram type(s), organized by example name
    
---

# Get Diagram Examples

Get example code for different types of diagrams.

    This tool provides ready-to-use example code for various diagram types.
    Use these examples to understand the syntax and capabilities of the diagrams package
    before creating your own custom diagrams.

    USAGE INSTRUCTIONS:
    1. Select the diagram type you're interested in (or 'all' to see all examples)
    2. Study the returned examples to understand the structure and syntax
    3. Use these examples as templates for your own diagrams
    4. When ready, modify an example or write your own code and use generate_diagram

    EXAMPLE CATEGORIES:
    - aws: AWS cloud architecture diagrams (basic services, grouped workers, clustered web services, Bedrock)
    - sequence: Process and interaction flow diagrams
    - flow: Decision trees and workflow diagrams
    - class: Object relationship and inheritance diagrams
    - k8s: Kubernetes architecture diagrams
    - onprem: On-premises infrastructure diagrams
    - custom: Custom diagrams with custom icons
    - all: All available examples across categories

    Each example demonstrates different features of the diagrams package:
    - Basic connections between components
    - Grouping with Clusters
    - Advanced styling with Edge attributes
    - Different layout directions
    - Multiple component instances
    - Custom icons and nodes

    Parameters:
        diagram_type (str): Type of diagram example to return. Options: aws, sequence, flow, class, k8s, onprem, custom, all

    Returns:
        Dictionary with example code for the requested diagram type(s), organized by example name
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `diagram_type` | string | No | Type of diagram example to return. Options: aws, sequence, flow, class, k8s, onprem, custom, all |

