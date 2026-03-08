---
name: load-to-storage
description: Load data to one or more storage targets.

    This tool uses the UnifiedDataLoader to load data to configured storage targets.
    Currently supports:
    - S3: Load data as CSV, JSON, or Parquet files with optional partitioning

    Example targets configuration:
    ```python
    targets = [
        {
            'type': 's3',
            'config': {
                'bucket': 'my-bucket',
                'prefix': 'data/users/',
                'format': 'parquet',
                'partitioning': {'enabled': True, 'columns': ['region']},
                'storage': {'class': 'INTELLIGENT_TIERING', 'encryption': 'AES256'},
            },
        }
    ]
    ```

    Parameters:
        data: Dictionary mapping table names to lists of records
        targets: List of target configurations

    Returns:
        Dictionary containing results for each target
    
---

# Load To Storage

Load data to one or more storage targets.

    This tool uses the UnifiedDataLoader to load data to configured storage targets.
    Currently supports:
    - S3: Load data as CSV, JSON, or Parquet files with optional partitioning

    Example targets configuration:
    ```python
    targets = [
        {
            'type': 's3',
            'config': {
                'bucket': 'my-bucket',
                'prefix': 'data/users/',
                'format': 'parquet',
                'partitioning': {'enabled': True, 'columns': ['region']},
                'storage': {'class': 'INTELLIGENT_TIERING', 'encryption': 'AES256'},
            },
        }
    ]
    ```

    Parameters:
        data: Dictionary mapping table names to lists of records
        targets: List of target configurations

    Returns:
        Dictionary containing results for each target
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input_data` | string | Yes |  |

