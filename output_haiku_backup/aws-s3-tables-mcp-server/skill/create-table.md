---
name: create-table
description: Create a new S3 table in an S3 table bucket.

    Creates a new S3 table associated with the given S3 namespace in an S3 table bucket.
    The S3 table can be configured with specific format and metadata settings. Metadata contains the schema of the table.
    Do not use the metadata parameter if the schema is unclear.

    Supported Iceberg Primitive Types:
    - boolean: True or false
    - int: 32-bit signed integers (can promote to long)
    - long: 64-bit signed integers
    - float: 32-bit IEEE 754 floating point (can promote to double)
    - double: 64-bit IEEE 754 floating point
    - decimal(P,S): Fixed-point decimal with precision P and scale S (precision must be 38 or less)
    - date: Calendar date without timezone or time
    - time: Time of day, microsecond precision, without date or timezone
    - timestamp: Timestamp, microsecond precision, without timezone (represents date and time regardless of zone)
    - timestamptz: Timestamp, microsecond precision, with timezone (stored as UTC)
    - string: Arbitrary-length character sequences (UTF-8 encoded)

    Note: Binary field types (binary, fixed, uuid) are not supported.

    Example of S3 table metadata:
    {
        "metadata": {
            "iceberg": {
                "schema": {
                    "type": "struct",
                    "fields": [
                        {
                            "id": 1,
                            "name": "id",
                            "type": "long",
                            "required": true
                        },
                        {
                            "id": 2,
                            "name": "bool_field",
                            "type": "boolean",
                            "required": false
                        },
                        {
                            "id": 3,
                            "name": "int_field",
                            "type": "int",
                            "required": false
                        },
                        {
                            "id": 4,
                            "name": "long_field",
                            "type": "long",
                            "required": false
                        },
                        {
                            "id": 5,
                            "name": "float_field",
                            "type": "float",
                            "required": false
                        },
                        {
                            "id": 6,
                            "name": "double_field",
                            "type": "double",
                            "required": false
                        },
                        {
                            "id": 7,
                            "name": "decimal_field",
                            "type": "decimal(10,2)",
                            "required": false
                        },
                        {
                            "id": 8,
                            "name": "date_field",
                            "type": "date",
                            "required": false
                        },
                        {
                            "id": 9,
                            "name": "time_field",
                            "type": "time",
                            "required": false
                        },
                        {
                            "id": 10,
                            "name": "timestamp_field",
                            "type": "timestamp",
                            "required": false
                        },
                        {
                            "id": 11,
                            "name": "timestamptz_field",
                            "type": "timestamptz",
                            "required": false
                        },
                        {
                            "id": 12,
                            "name": "string_field",
                            "type": "string",
                            "required": false
                        }
                    ]
                },
                "partition-spec": [
                    {
                        "source-id": 8,
                        "field-id": 1000,
                        "transform": "month",
                        "name": "date_field_month"
                    }
                ],
                "table-properties": {
                    "description": "Example table demonstrating supported Iceberg primitive types"
                }
            }
        }
    }

    Permissions:
    You must have the s3tables:CreateTable permission to use this operation.
    
---

# Create Table

Create a new S3 table in an S3 table bucket.

    Creates a new S3 table associated with the given S3 namespace in an S3 table bucket.
    The S3 table can be configured with specific format and metadata settings. Metadata contains the schema of the table.
    Do not use the metadata parameter if the schema is unclear.

    Supported Iceberg Primitive Types:
    - boolean: True or false
    - int: 32-bit signed integers (can promote to long)
    - long: 64-bit signed integers
    - float: 32-bit IEEE 754 floating point (can promote to double)
    - double: 64-bit IEEE 754 floating point
    - decimal(P,S): Fixed-point decimal with precision P and scale S (precision must be 38 or less)
    - date: Calendar date without timezone or time
    - time: Time of day, microsecond precision, without date or timezone
    - timestamp: Timestamp, microsecond precision, without timezone (represents date and time regardless of zone)
    - timestamptz: Timestamp, microsecond precision, with timezone (stored as UTC)
    - string: Arbitrary-length character sequences (UTF-8 encoded)

    Note: Binary field types (binary, fixed, uuid) are not supported.

    Example of S3 table metadata:
    {
        "metadata": {
            "iceberg": {
                "schema": {
                    "type": "struct",
                    "fields": [
                        {
                            "id": 1,
                            "name": "id",
                            "type": "long",
                            "required": true
                        },
                        {
                            "id": 2,
                            "name": "bool_field",
                            "type": "boolean",
                            "required": false
                        },
                        {
                            "id": 3,
                            "name": "int_field",
                            "type": "int",
                            "required": false
                        },
                        {
                            "id": 4,
                            "name": "long_field",
                            "type": "long",
                            "required": false
                        },
                        {
                            "id": 5,
                            "name": "float_field",
                            "type": "float",
                            "required": false
                        },
                        {
                            "id": 6,
                            "name": "double_field",
                            "type": "double",
                            "required": false
                        },
                        {
                            "id": 7,
                            "name": "decimal_field",
                            "type": "decimal(10,2)",
                            "required": false
                        },
                        {
                            "id": 8,
                            "name": "date_field",
                            "type": "date",
                            "required": false
                        },
                        {
                            "id": 9,
                            "name": "time_field",
                            "type": "time",
                            "required": false
                        },
                        {
                            "id": 10,
                            "name": "timestamp_field",
                            "type": "timestamp",
                            "required": false
                        },
                        {
                            "id": 11,
                            "name": "timestamptz_field",
                            "type": "timestamptz",
                            "required": false
                        },
                        {
                            "id": 12,
                            "name": "string_field",
                            "type": "string",
                            "required": false
                        }
                    ]
                },
                "partition-spec": [
                    {
                        "source-id": 8,
                        "field-id": 1000,
                        "transform": "month",
                        "name": "date_field_month"
                    }
                ],
                "table-properties": {
                    "description": "Example table demonstrating supported Iceberg primitive types"
                }
            }
        }
    }

    Permissions:
    You must have the s3tables:CreateTable permission to use this operation.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `table_bucket_arn` | string | Yes | Table bucket ARN |
| `namespace` | string | Yes | The name of the namespace. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `name` | string | Yes | The name of the table. Must be 1-255 characters long and contain only alphanumeric characters, underscores, and hyphens. |
| `format` | string | No | The format for the S3 table. |
| `metadata` | string | No | The metadata for the S3 table. |
| `region_name` | string | No | The AWS region name where the operation should be performed. |

