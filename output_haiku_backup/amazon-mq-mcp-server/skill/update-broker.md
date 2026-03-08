---
name: update-broker
description: Execute the AWS AmazonMQ `update_broker` operation.
---

# Update Broker

Execute the AWS AmazonMQ `update_broker` operation.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `region` | string | Yes | AWS region on which the broker is in |
| `BrokerId` | string | Yes |  |
| `AuthenticationStrategy` | string | No | <p>Optional. The authentication strategy used to secure the broker. The default is SIMPLE.</p> |
| `AutoMinorVersionUpgrade` | boolean | No | <p>Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot.</p> <note><p>Must be set to true for ActiveMQ brokers version 5.18 and above and for RabbitMQ brokers version 3.13 and above.</p></note> |
| `Configuration` | string | No | <p>A list of information about the configuration.</p> |
| `EngineVersion` | string | No | <p>The broker engine version. For more information, see the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html">ActiveMQ version management</a> and the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p> <note><p>When upgrading to ActiveMQ version 5.18 and above or RabbitMQ version 3.13 and above, you must have autoMinorVersionUpgrade set to true for the broker.</p></note> |
| `HostInstanceType` | string | No | <p>The broker's host instance type to upgrade to. For a list of supported instance types, see <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/broker.html#broker-instance-types">Broker instance types</a>.</p> |
| `LdapServerMetadata` | string | No | <p>Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.</p> |
| `Logs` | string | No | <p>Enables Amazon CloudWatch logging for brokers.</p> |
| `MaintenanceWindowStartTime` | string | No | <p>The parameters that determine the WeeklyStartTime.</p> |
| `SecurityGroups` | string | No | <p>The list of security groups (1 minimum, 5 maximum) that authorizes connections to brokers.</p> |
| `DataReplicationMode` | string | No | <p>Defines whether this broker is a part of a data replication pair.</p> |

## AWS CLI

```bash
aws mq update-broker --broker-id <BrokerId> --authentication-strategy <AuthenticationStrategy> --auto-minor-version-upgrade <AutoMinorVersionUpgrade> --configuration <Configuration> --engine-version <EngineVersion> --host-instance-type <HostInstanceType> --ldap-server-metadata <LdapServerMetadata> --logs <Logs> --maintenance-window-start-time <MaintenanceWindowStartTime> --security-groups <SecurityGroups> --data-replication-mode <DataReplicationMode>
```

## boto3

```python
import boto3

client = boto3.client('mq')
response = client.update_broker(
    BrokerId=BrokerId,
    AuthenticationStrategy=AuthenticationStrategy,
    AutoMinorVersionUpgrade=AutoMinorVersionUpgrade,
    Configuration=Configuration,
    EngineVersion=EngineVersion,
    HostInstanceType=HostInstanceType,
    LdapServerMetadata=LdapServerMetadata,
    Logs=Logs,
    MaintenanceWindowStartTime=MaintenanceWindowStartTime,
    SecurityGroups=SecurityGroups,
    DataReplicationMode=DataReplicationMode,
)
```
