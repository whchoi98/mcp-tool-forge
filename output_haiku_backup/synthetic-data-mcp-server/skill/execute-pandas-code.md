---
name: execute-pandas-code
description: Execute pandas code to generate synthetic data and save it as CSV files.

    This tool runs pandas code in a restricted environment to generate synthetic data.
    It then saves any generated DataFrames as CSV files.

    ## Features

    1. **Multiple DataFrame Detection**: The tool automatically finds all pandas DataFrames defined in your code and saves them as separate CSV files.

    2. **Referential Integrity Checking**: For multi-table data models, the tool checks for foreign key relationships and validates that references are valid.

    3. **Third Normal Form Validation**: The tool identifies potential 3NF violations like functional dependencies between non-key attributes.

    ## Code Requirements

    - Your code should define one or more pandas DataFrames
    - No need to include imports - pandas is already available as 'pd'
    - No need to include save logic - all DataFrames will be automatically saved

    ## Example Usage

    ```python
    # Simple table
    customers_df = pd.DataFrame(
        {
            'customer_id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'city': ['New York', 'San Francisco', 'Chicago'],
        }
    )

    # Related table with foreign key
    orders_df = pd.DataFrame(
        {'order_id': [101, 102, 103], 'customer_id': [1, 2, 3], 'amount': [99.99, 149.99, 199.99]}
    )
    ```

    Parameters:
        code: Python code using pandas to generate synthetic data
        workspace_dir: CRITICAL - The current workspace directory
        output_dir: Optional subdirectory within workspace_dir to save CSV files to

    Returns:
        A dictionary containing execution results and paths to saved CSV files
    
---

# Execute Pandas Code

Execute pandas code to generate synthetic data and save it as CSV files.

    This tool runs pandas code in a restricted environment to generate synthetic data.
    It then saves any generated DataFrames as CSV files.

    ## Features

    1. **Multiple DataFrame Detection**: The tool automatically finds all pandas DataFrames defined in your code and saves them as separate CSV files.

    2. **Referential Integrity Checking**: For multi-table data models, the tool checks for foreign key relationships and validates that references are valid.

    3. **Third Normal Form Validation**: The tool identifies potential 3NF violations like functional dependencies between non-key attributes.

    ## Code Requirements

    - Your code should define one or more pandas DataFrames
    - No need to include imports - pandas is already available as 'pd'
    - No need to include save logic - all DataFrames will be automatically saved

    ## Example Usage

    ```python
    # Simple table
    customers_df = pd.DataFrame(
        {
            'customer_id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'city': ['New York', 'San Francisco', 'Chicago'],
        }
    )

    # Related table with foreign key
    orders_df = pd.DataFrame(
        {'order_id': [101, 102, 103], 'customer_id': [1, 2, 3], 'amount': [99.99, 149.99, 199.99]}
    )
    ```

    Parameters:
        code: Python code using pandas to generate synthetic data
        workspace_dir: CRITICAL - The current workspace directory
        output_dir: Optional subdirectory within workspace_dir to save CSV files to

    Returns:
        A dictionary containing execution results and paths to saved CSV files
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input_data` | string | Yes |  |

