---
name: add-communication-to-case
description: Add communication to a support case.

## Usage
- You must provide a valid case ID
- You must provide a communication body
- You can optionally CC email addresses on the communication
- You can optionally attach files using an attachment set ID

## Example
```
add_communication_to_case(
    case_id='case-12345678910-2013-c4c1d2bf33c5cf47',
    communication_body='Here is an update on my issue...',
)
```
---

# Add Communication To Case

Add communication to a support case.

## Usage
- You must provide a valid case ID
- You must provide a communication body
- You can optionally CC email addresses on the communication
- You can optionally attach files using an attachment set ID

## Example
```
add_communication_to_case(
    case_id='case-12345678910-2013-c4c1d2bf33c5cf47',
    communication_body='Here is an update on my issue...',
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `case_id` | string | Yes | The ID of the support case |
| `communication_body` | string | Yes | The text of the communication |
| `cc_email_addresses` | string | No | Email addresses to CC on the communication |
| `attachment_set_id` | string | No | The ID of the attachment set |

## AWS CLI

```bash
aws support add-communication-to-case --case-id <case_id> --communication-body <communication_body> --cc-email-addresses <cc_email_addresses> --attachment-set-id <attachment_set_id>
```

## boto3

```python
import boto3

client = boto3.client('support')
response = client.add_communication_to_case(
    CaseId=case_id,
    CommunicationBody=communication_body,
    CcEmailAddresses=cc_email_addresses,
    AttachmentSetId=attachment_set_id,
)
```
