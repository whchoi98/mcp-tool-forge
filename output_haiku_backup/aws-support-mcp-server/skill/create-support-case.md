---
name: create-support-case
description: Create a new AWS Support case.

## Usage Requirements
- You must provide a clear subject and detailed communication body

## Example
```
create_support_case(
    subject='EC2 instance not starting',
    service_code='amazon-elastic-compute-cloud-linux',
    category_code='using-aws',
    severity_code='urgent',
    communication_body='My EC2 instance i-1234567890abcdef0 is not starting.',
)
```

## Severity Level Guidelines
- low (General guidance): You have a general development question or want to request a feature.
- normal (System impaired): Non-critical functions are behaving abnormally or you have a time-sensitive development question.
- high (Production system impaired): Important functions are impaired but a workaround exists.
- urgent (Production system down): Your business is significantly impacted and no workaround exists.
- critical (Business-critical system down): Your business is at risk and critical functions are unavailable.
---

# Create Support Case

Create a new AWS Support case.

## Usage Requirements
- You must provide a clear subject and detailed communication body

## Example
```
create_support_case(
    subject='EC2 instance not starting',
    service_code='amazon-elastic-compute-cloud-linux',
    category_code='using-aws',
    severity_code='urgent',
    communication_body='My EC2 instance i-1234567890abcdef0 is not starting.',
)
```

## Severity Level Guidelines
- low (General guidance): You have a general development question or want to request a feature.
- normal (System impaired): Non-critical functions are behaving abnormally or you have a time-sensitive development question.
- high (Production system impaired): Important functions are impaired but a workaround exists.
- urgent (Production system down): Your business is significantly impacted and no workaround exists.
- critical (Business-critical system down): Your business is at risk and critical functions are unavailable.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `subject` | string | Yes | The subject of the support case |
| `service_code` | string | Yes | The code for the AWS service. Use describe_services get valid codes. |
| `category_code` | string | Yes | The category code for the issue. Use describe_services to get valid codes. |
| `severity_code` | string | Yes | The severity code for the issue. Use describe_severity_levels to get valid codes. |
| `communication_body` | string | Yes | The initial communication for the case |
| `cc_email_addresses` | string | No | Email addresses to CC on the case |
| `language` | string | No | The language of the case (ISO 639-1 code) |
| `issue_type` | string | No | The type of issue: technical, account-and-billing, or service-limit |
| `attachment_set_id` | string | No | The ID of the attachment set |

## AWS CLI

```bash
aws support create-case --subject <subject> --service-code <service_code> --category-code <category_code> --severity-code <severity_code> --communication-body <communication_body> --cc-email-addresses <cc_email_addresses> --language <language> --issue-type <issue_type> --attachment-set-id <attachment_set_id>
```

## boto3

```python
import boto3

client = boto3.client('support')
response = client.create_case(
    Subject=subject,
    ServiceCode=service_code,
    CategoryCode=category_code,
    SeverityCode=severity_code,
    CommunicationBody=communication_body,
    CcEmailAddresses=cc_email_addresses,
    Language=language,
    IssueType=issue_type,
    AttachmentSetId=attachment_set_id,
)
```
