---
name: analyzeSchema
description: Analyze the schema of a collection by sampling documents.

    This tool samples documents from a collection and provides information about
    the document structure and field coverage across the sampled documents.

    Returns:
        Dict[str, Any]: Schema analysis results including field coverage
    
---

# Analyzeschema

Analyze the schema of a collection by sampling documents.

    This tool samples documents from a collection and provides information about
    the document structure and field coverage across the sampled documents.

    Returns:
        Dict[str, Any]: Schema analysis results including field coverage
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_id` | string | Yes | The connection ID returned by the connect tool |
| `database` | string | Yes | Name of the database |
| `collection` | string | Yes | Name of the collection to analyze |
| `sample_size` | integer | No | Number of documents to sample (default: 100) |

## AWS CLI

```bash
aws docdb describe-db-cluster-snapshot-attributes --db-cluster-snapshot-identifier <connection_id> --database-name <database> --collection-name <collection> --max-records <sample_size>
```

## boto3

```python
import boto3

client = boto3.client('docdb')
response = client.describe_db_cluster_snapshot_attributes(
    DBClusterSnapshotIdentifier=connection_id,
    DatabaseName=database,
    CollectionName=collection,
    MaxRecords=sample_size,
)
```
