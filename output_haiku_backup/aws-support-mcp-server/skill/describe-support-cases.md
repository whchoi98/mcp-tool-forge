---
name: describe-support-cases
description: Retrieve information about support cases.

## Usage
- You can retrieve cases by ID, display ID, or date range
- You can include or exclude resolved cases and communications
- You can paginate through results using the next_token parameter

## Example
```
describe_support_cases(
    case_id_list=['case-12345678910-2013-c4c1d2bf33c5cf47'], include_communications=True
)
```

## Date Format
Dates should be provided in ISO 8601 format (e.g., "2023-01-01T00:00:00Z")

## Response Format
You can request the response in either JSON or Markdown format using the format parameter.
---

# Describe Support Cases

Retrieve information about support cases.

## Usage
- You can retrieve cases by ID, display ID, or date range
- You can include or exclude resolved cases and communications
- You can paginate through results using the next_token parameter

## Example
```
describe_support_cases(
    case_id_list=['case-12345678910-2013-c4c1d2bf33c5cf47'], include_communications=True
)
```

## Date Format
Dates should be provided in ISO 8601 format (e.g., "2023-01-01T00:00:00Z")

## Response Format
You can request the response in either JSON or Markdown format using the format parameter.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `case_id_list` | string | No | List of case IDs to retrieve |
| `display_id` | string | No | The display ID of the case |
| `after_time` | string | No | The start date for a filtered date search (ISO 8601 format) |
| `before_time` | string | No | The end date for a filtered date search (ISO 8601 format) |
| `include_resolved_cases` | boolean | No | Include resolved cases in the results |
| `include_communications` | boolean | No | Include communications in the results |
| `language` | string | No | The language of the case (ISO 639-1 code) |
| `max_results` | string | No | The maximum number of results to return |
| `next_token` | string | No | A resumption point for pagination |
| `format` | string | No | The format of the response (json or markdown) |

## AWS CLI

```bash
aws support describe-cases --case-id-list <case_id_list> --display-id <display_id> --after-time <after_time> --before-time <before_time> --include-resolved-cases <include_resolved_cases> --include-communications <include_communications> --language <language> --max-results <max_results> --next-token <next_token>
```

## boto3

```python
import boto3

client = boto3.client('support')
response = client.describe_cases(
    CaseIdList=case_id_list,
    DisplayId=display_id,
    AfterTime=after_time,
    BeforeTime=before_time,
    IncludeResolvedCases=include_resolved_cases,
    IncludeCommunications=include_communications,
    Language=language,
    MaxResults=max_results,
    NextToken=next_token,
)
```
