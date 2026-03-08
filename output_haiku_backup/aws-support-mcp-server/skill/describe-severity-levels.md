---
name: describe-severity-levels
description: Retrieve information about AWS Support severity levels. This tool provides details about the available severity levels for AWS Support cases, including their codes and descriptions.

## Usage
- You can request the response in either JSON or Markdown format.
- Use this information to determine the appropriate severity level for creating support cases.
- Use this information when crafting queries for Describe Cases.

## Example
```
# Get severity levels in JSON format
describe_severity_levels()

# Get severity levels in Markdown format
describe_severity_levels(format='markdown')
```
## Severity Level Guidelines
- low (General guidance): You have a general development question or want to request a feature
- normal (System impaired): Non-critical functions are behaving abnormally
- high (Production system impaired): Important functions are impaired but a workaround exists
- urgent (Production system down): Your business is significantly impacted; no workaround exists
- critical (Business-critical system down): Your business is at risk; critical functions unavailable
---

# Describe Severity Levels

Retrieve information about AWS Support severity levels. This tool provides details about the available severity levels for AWS Support cases, including their codes and descriptions.

## Usage
- You can request the response in either JSON or Markdown format.
- Use this information to determine the appropriate severity level for creating support cases.
- Use this information when crafting queries for Describe Cases.

## Example
```
# Get severity levels in JSON format
describe_severity_levels()

# Get severity levels in Markdown format
describe_severity_levels(format='markdown')
```
## Severity Level Guidelines
- low (General guidance): You have a general development question or want to request a feature
- normal (System impaired): Non-critical functions are behaving abnormally
- high (Production system impaired): Important functions are impaired but a workaround exists
- urgent (Production system down): Your business is significantly impacted; no workaround exists
- critical (Business-critical system down): Your business is at risk; critical functions unavailable

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `format` | string | No | The format of the response in markdown or json |

