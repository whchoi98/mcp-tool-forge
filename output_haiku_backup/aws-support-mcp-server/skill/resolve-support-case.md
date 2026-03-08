---
name: resolve-support-case
description: Resolve a support case.

## Usage
- You must provide a valid case ID
- The case must be in an open state to be resolved

## Example
```
resolve_support_case(case_id='case-12345678910-2013-c4c1d2bf33c5cf47')
```
---

# Resolve Support Case

Resolve a support case.

## Usage
- You must provide a valid case ID
- The case must be in an open state to be resolved

## Example
```
resolve_support_case(case_id='case-12345678910-2013-c4c1d2bf33c5cf47')
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `case_id` | string | Yes | The ID of the support case |

## AWS CLI

```bash
aws support resolve-case --case-id <case_id>
```

## boto3

```python
import boto3

client = boto3.client('support')
response = client.resolve_case(
    CaseId=case_id,
)
```
