---
name: list-icons
description: List available icons from the diagrams package, with optional filtering.

    This tool dynamically inspects the diagrams package to find available
    providers, services, and icons that can be used in diagrams.

    USAGE INSTRUCTIONS:
    1. Call without filters to get a list of available providers
    2. Call with provider_filter to get all services and icons for that provider
    3. Call with both provider_filter and service_filter to get icons for a specific service

    Example workflow:
    - First call: list_icons() → Returns all available providers
    - Second call: list_icons(provider_filter="aws") → Returns all AWS services and icons
    - Third call: list_icons(provider_filter="aws", service_filter="compute") → Returns AWS compute icons

    This approach is more efficient than loading all icons at once, especially when you only need
    icons from specific providers or services.

    Returns:
        Dictionary with available providers, services, and icons organized hierarchically
    
---

# List Icons

List available icons from the diagrams package, with optional filtering.

    This tool dynamically inspects the diagrams package to find available
    providers, services, and icons that can be used in diagrams.

    USAGE INSTRUCTIONS:
    1. Call without filters to get a list of available providers
    2. Call with provider_filter to get all services and icons for that provider
    3. Call with both provider_filter and service_filter to get icons for a specific service

    Example workflow:
    - First call: list_icons() → Returns all available providers
    - Second call: list_icons(provider_filter="aws") → Returns all AWS services and icons
    - Third call: list_icons(provider_filter="aws", service_filter="compute") → Returns AWS compute icons

    This approach is more efficient than loading all icons at once, especially when you only need
    icons from specific providers or services.

    Returns:
        Dictionary with available providers, services, and icons organized hierarchically
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `provider_filter` | string | No | Filter icons by provider name (e.g., "aws", "gcp", "k8s") |
| `service_filter` | string | No | Filter icons by service name (e.g., "compute", "database", "network") |

