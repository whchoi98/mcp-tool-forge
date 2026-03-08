---
name: validate-and-save-data
description: Validate JSON Lines data and save it as CSV files.

    This tool validates the structure of JSON Lines data and saves it as CSV files
    using pandas.

    Parameters:
        data: Dictionary mapping table names to lists of records
        workspace_dir: CRITICAL - The current workspace directory
        output_dir: Optional subdirectory within workspace_dir to save CSV files to

    Returns:
        A dictionary containing validation results and paths to saved CSV files
    
---

# Validate And Save Data

Validate JSON Lines data and save it as CSV files.

    This tool validates the structure of JSON Lines data and saves it as CSV files
    using pandas.

    Parameters:
        data: Dictionary mapping table names to lists of records
        workspace_dir: CRITICAL - The current workspace directory
        output_dir: Optional subdirectory within workspace_dir to save CSV files to

    Returns:
        A dictionary containing validation results and paths to saved CSV files
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input_data` | string | Yes |  |

