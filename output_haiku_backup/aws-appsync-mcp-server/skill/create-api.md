---
name: create-api
description: Creates a new AppSync API.

        This operation creates a new AppSync API with the specified configuration.
        The API will be created with default settings and can be further configured
        using additional AppSync operations.
        
---

# Create Api

Creates a new AppSync API.

        This operation creates a new AppSync API with the specified configuration.
        The API will be created with default settings and can be further configured
        using additional AppSync operations.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | string | Yes | The name of the API |
| `owner_contact` | string | No | The owner contact information for the API |
| `tags` | string | No | A map of tags to assign to the resource |
| `event_config` | string | No | The event configuration for the API |

