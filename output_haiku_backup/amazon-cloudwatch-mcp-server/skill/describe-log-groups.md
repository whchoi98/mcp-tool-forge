---
name: describe-log-groups
description: Lists AWS CloudWatch log groups and saved queries associated with them, optionally filtering by a name prefix.

        This tool retrieves information about log groups in the account, or log groups in accounts linked to this account as a monitoring account.
        If a prefix is provided, only log groups with names starting with the specified prefix are returned.

        Additionally returns any user saved queries that are associated with any of the returned log groups.

        Usage: Use this tool to discover log groups that you'd retrieve or query logs from and queries that have been saved by the user.

        Returns:
        --------
        List of log group metadata dictionaries and saved queries associated with them
           Each log group metadata contains details such as:
                - logGroupName: The name of the log group.
                - creationTime: Timestamp when the log group was created
                - retentionInDays: Retention period, if set
                - storedBytes: The number of bytes stored.
                - kmsKeyId: KMS Key Id used for data encryption, if set
                - dataProtectionStatus: Displays whether this log group has a protection policy, or whether it had one in the past, if set
                - logGroupClass: Type of log group class
                - logGroupArn: The Amazon Resource Name (ARN) of the log group. This version of the ARN doesn't include a trailing :* after the log group name.
            Any saved queries that are applicable to the returned log groups are also included.
        
---

# Describe Log Groups

Lists AWS CloudWatch log groups and saved queries associated with them, optionally filtering by a name prefix.

        This tool retrieves information about log groups in the account, or log groups in accounts linked to this account as a monitoring account.
        If a prefix is provided, only log groups with names starting with the specified prefix are returned.

        Additionally returns any user saved queries that are associated with any of the returned log groups.

        Usage: Use this tool to discover log groups that you'd retrieve or query logs from and queries that have been saved by the user.

        Returns:
        --------
        List of log group metadata dictionaries and saved queries associated with them
           Each log group metadata contains details such as:
                - logGroupName: The name of the log group.
                - creationTime: Timestamp when the log group was created
                - retentionInDays: Retention period, if set
                - storedBytes: The number of bytes stored.
                - kmsKeyId: KMS Key Id used for data encryption, if set
                - dataProtectionStatus: Displays whether this log group has a protection policy, or whether it had one in the past, if set
                - logGroupClass: Type of log group class
                - logGroupArn: The Amazon Resource Name (ARN) of the log group. This version of the ARN doesn't include a trailing :* after the log group name.
            Any saved queries that are applicable to the returned log groups are also included.
        

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_identifiers` | string | No | When include_linked_accounts is set to True, use this parameter to specify the list of accounts to search. IMPORTANT: Only has affect if include_linked_accounts is True |
| `include_linked_accounts` | string | No | If the AWS account is a monitoring account, set this to True to have the tool return log groups in the accounts listed in account_identifiers.
                If this parameter is set to true and account_identifiers contains a null value, the tool returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account. |
| `log_group_class` | string | No | If specified, filters for only log groups of the specified class. |
| `log_group_name_prefix` | string | No | An exact prefix to filter log groups by name. IMPORTANT: Only log groups with names starting with this prefix will be returned. |
| `max_items` | string | No | The maximum number of log groups to return. |
| `region` | string | No | AWS region to query. Defaults to AWS_REGION environment variable or us-east-1 if not set. |
| `profile_name` | string | No | AWS CLI Profile Name to use for AWS access. Falls back to AWS_PROFILE environment variable if not specified, or uses default AWS credential chain. |

## AWS CLI

```bash
aws logs describe-log-groups --log-group-name-prefix <log_group_name_prefix> --max-items <max_items> --log-group-class <log_group_class>
```

## boto3

```python
import boto3

client = boto3.client('logs')
response = client.describe_log_groups(
    LogGroupNamePrefix=log_group_name_prefix,
    Limit=max_items,
    LogGroupClass=log_group_class,
)
```
