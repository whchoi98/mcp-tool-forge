---
name: connect
description: Connect to an AWS DocumentDB cluster.

    This tool establishes and validates a connection to DocumentDB.
    The returned connection_id can be used with other tools instead of providing
    the full connection string each time.

    Returns:
        Dict[str, Any]: Connection details including connection_id and available databases
    
---

# Connect

Connect to an AWS DocumentDB cluster.

    This tool establishes and validates a connection to DocumentDB.
    The returned connection_id can be used with other tools instead of providing
    the full connection string each time.

    Returns:
        Dict[str, Any]: Connection details including connection_id and available databases
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `connection_string` | string | Yes | DocumentDB connection string. Example: "mongodb://user:pass@docdb-cluster.cluster-xyz.us-west-2.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem" |

