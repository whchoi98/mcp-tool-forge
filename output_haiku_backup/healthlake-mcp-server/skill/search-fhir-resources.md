---
name: search-fhir-resources
description: Search for FHIR resources in HealthLake datastore with advanced search capabilities. Returns up to 100 results per call. If pagination.has_next is true, call this tool again with the next_token to get more results.
---

# Search Fhir Resources

Search for FHIR resources in HealthLake datastore with advanced search capabilities. Returns up to 100 results per call. If pagination.has_next is true, call this tool again with the next_token to get more results.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `datastore_id` | string | Yes | HealthLake datastore ID |
| `resource_type` | string | Yes | FHIR resource type (e.g., Patient, Observation, Condition) |
| `search_params` | object | No | Basic FHIR search parameters. Supports modifiers (e.g., 'name:contains'), prefixes (e.g., 'birthdate': 'ge1990-01-01'), and simple chaining (e.g., 'subject:Patient') |
| `chained_params` | object | No | Advanced chained search parameters. Key format: 'param.chain' or 'param:TargetType.chain' (e.g., {'subject.name': 'Smith', 'general-practitioner:Practitioner.name': 'Johnson'}) |
| `include_params` | array | No | Include related resources in the response. Format: 'ResourceType:parameter' or 'ResourceType:parameter:target-type' (e.g., ['Patient:general-practitioner', 'Observation:subject:Patient']) |
| `revinclude_params` | array | No | Include resources that reference the found resources. Format: 'ResourceType:parameter' (e.g., ['Observation:subject', 'Condition:subject']) |
| `count` | integer | No | Maximum number of results to return (1-100, default: 100) |
| `next_token` | string | No | Pagination token for retrieving the next page of results. Use the complete URL from a previous response's pagination.next_token field. When provided, other search parameters are ignored. |

