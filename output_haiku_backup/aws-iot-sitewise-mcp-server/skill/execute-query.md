---
name: execute-query
description: Execute comprehensive SQL queries against AWS IoT SiteWise data using the executeQuery API.

    The AWS IoT SiteWise query language supports SQL capabilities including:
    - Views: asset, asset_property, raw_time_series,         latest_value_time_series, precomputed_aggregates
    - SQL clauses: SELECT, FROM, WHERE, GROUP BY, ORDER BY, HAVING, LIMIT
    - Functions: Aggregation, date/time, string, mathematical, conditional
    - Operators: Comparison, logical, arithmetic, pattern matching (LIKE)
    - JOIN operations: JOIN, LEFT JOIN,
        UNION (prefer implicit joins for performance)

    Available Views and Schema (From Official AWS Documentation):

    ASSET VIEW: Contains information about the asset and model derivation
    - asset_id (string), asset_name (string), asset_description (string)
    - asset_model_id (string), parent_asset_id (string),
        asset_external_id (string)
    - asset_external_model_id (string), hierarchy_id (string)

    ASSET_PROPERTY VIEW: Contains information about the asset property's structure
    - asset_id (string), property_id (string), property_name (string),
        property_alias (string)
    - property_external_id (string), asset_composite_model_id (string),
        property_type (string)
    - property_data_type (string), int_attribute_value (integer),
        double_attribute_value (double)
    - boolean_attribute_value (boolean), string_attribute_value (string)

    RAW_TIME_SERIES VIEW: Contains the historical data of the time series
    - asset_id (string), property_id (string), property_alias (string),
        event_timestamp (timestamp)
    - quality (string), boolean_value (boolean), int_value (integer),
        double_value (double), string_value (string)

    LATEST_VALUE_TIME_SERIES VIEW: Contains the latest value of the time series
    - asset_id (string), property_id (string), property_alias (string),
        event_timestamp (timestamp)
    - quality (string), boolean_value (boolean), int_value (integer),
        double_value (double), string_value (string)

    PRECOMPUTED_AGGREGATES VIEW: Contains automatically computed         aggregated asset property values
    - asset_id (string), property_id (string), property_alias (string),
        event_timestamp (timestamp)
    - quality (string), resolution (string), sum_value (double),
        count_value (integer)
    - average_value (double), maximum_value (double),
        minimum_value (double), stdev_value (double)

    Complete SQL Function Reference (From AWS IoT SiteWise User Guide):

    DATE/TIME FUNCTIONS:
    - DATE_ADD(
        unit,
        value,
        date): Add time to date (e.g.,
        DATE_ADD(DAY, 7, event_timestamp))    - DATE_SUB(
        unit,
        value,
        date): Subtract time from date (e.g.,
        DATE_SUB(
            YEAR,
            2,
            event_timestamp))    - TIMESTAMP_ADD(
                unit,
                value,
                timestamp): Add time to timestamp
    - TIMESTAMP_SUB(unit, value, timestamp): Subtract time from timestamp
    - NOW(
        ): Current timestamp (supported,
        but use TIMESTAMP_ADD/SUB for math operations)    -             TIMESTAMP literals: Use TIMESTAMP '2023-01-01 00:00:00' for specific dates
    - CAST(expression AS TIMESTAMP): Convert string to timestamp

    Note: NOW() IS supported. When doing math on NOW() or         any timestamp, use TIMESTAMP_ADD/TIMESTAMP_SUB functions rather than             +/- operators.

    TYPE CONVERSION FUNCTIONS:
    - TO_DATE(integer): Convert epoch milliseconds to date
    - TO_DATE(expression, format): Convert string to date with format
    - TO_TIMESTAMP(double): Convert epoch seconds to timestamp
    - TO_TIMESTAMP(string, format): Convert string to timestamp with format
    - TO_TIME(int): Convert epoch milliseconds to time
    - TO_TIME(string, format): Convert string to time with format
    - CAST(expression AS data_type): Convert between BOOLEAN, INTEGER,
        TIMESTAMP, DATE, STRING, etc.

    AGGREGATE FUNCTIONS:
    - AVG(expression): Average value
    - COUNT(expression): Count rows (COUNT(*) is supported)
    - MAX(expression): Maximum value
    - MIN(expression): Minimum value
    - SUM(expression): Sum values
    - STDDEV(expression): Standard deviation
    - GROUP BY expression: Group results
    - HAVING boolean-expression: Filter grouped results

    IMPORTANT LIMITATIONS:
    - Window functions, CTEs (WITH clauses), DISTINCT, SELECT *, and         ILIKE are NOT supported

    SUPPORTED FEATURES:
    - CASE statements (CASE WHEN...THEN...ELSE...END pattern) ARE supported
    - COUNT(*) IS supported (only SELECT * is blocked)
    - Use implicit JOINs for better performance when possible

    Args:
        query_statement: The SQL query statement to execute (max 64KB)
        region: AWS region (default: us-east-1)
        next_token: Token for paginated results
        max_results: Maximum results to return (1-4000, default: 100)

    Returns:
        Dictionary containing:
        - success: Boolean indicating query success
        - columns: List of column definitions
        - rows: List of result rows
        - next_token: Token for next page (if applicable)
        - query_statistics: Execution statistics
        - query_status: Query execution status

    Example Queries (Using Correct View and Column Names):

    Basic Asset Discovery:
        "SELECT asset_id, asset_name, asset_model_id FROM asset"

    Metadata Filtering:
        "SELECT a.asset_name, p.property_name FROM asset a, asset_property p             WHERE a.asset_id = p.asset_id AND a.asset_name LIKE 'Windmill%'"

    Value Filtering with Time Range:
        "SELECT a.asset_name, r.int_value FROM asset a, raw_time_series r
         WHERE a.asset_id = r.asset_id
         AND r.int_value > 30
         AND r.event_timestamp > TIMESTAMP '2022-01-05 12:15:00'
         AND r.event_timestamp < TIMESTAMP '2022-01-05 12:20:00'"

    Aggregation with Grouping:
        "SELECT MAX(d.int_value) AS max_int_value, d.asset_id
         FROM raw_time_series AS d
         GROUP BY d.asset_id
         HAVING MAX(d.int_value) > 5"

    Date/Time Manipulation:
        "SELECT r.asset_id, r.int_value,
         DATE_ADD(DAY, 7, r.event_timestamp) AS date_in_future,
         DATE_SUB(YEAR, 2, r.event_timestamp) AS date_in_past,
         TIMESTAMP_ADD(DAY, 2, r.event_timestamp) AS timestamp_in_future,
         TIMESTAMP_SUB(DAY, 2, r.event_timestamp) AS timestamp_in_past
         FROM raw_time_series AS r"

    Type Conversion Examples:
        "SELECT r.asset_id, TO_DATE(r.event_timestamp) AS date_value,
         TO_TIME(r.event_timestamp) AS time_value
         FROM raw_time_series AS r"

    Attribute Property Filtering (For Attribute Properties Only -         Note: Only one attribute value type can be non-null per property):
        "SELECT p.property_name,
         CASE
             WHEN p.string_attribute_value IS NOT NULL THEN p.string_attribute_value
             WHEN p.double_attribute_value IS NOT NULL THEN                  CAST(p.double_attribute_value AS STRING)
             ELSE 'NULL'
         END as attribute_value
         FROM asset_property p
         WHERE p.property_type = 'attribute'
         AND (p.string_attribute_value LIKE 'my-property-%' OR              p.double_attribute_value > 100.0)"

    Precomputed Aggregates (Include quality and resolution filters):
        "SELECT asset_id, property_id, average_value, event_timestamp
         FROM precomputed_aggregates
         WHERE quality = 'GOOD'
         AND resolution = '1h'
         AND event_timestamp BETWEEN TIMESTAMP '2023-01-01 00:00:00' AND              TIMESTAMP '2023-01-02 00:00:00'"

    Implicit JOIN for Better Performance:
        "SELECT a.asset_name, p.property_name, r.double_value
         FROM asset a, asset_property p, raw_time_series r
         WHERE a.asset_id = p.asset_id
         AND p.property_id = r.property_id
         AND r.quality = 'GOOD'"

    Data Quality Analysis:
        "SELECT asset_id, property_alias,
         SUM(CASE WHEN quality = 'GOOD' THEN 1 ELSE 0 END) as good_readings,
         SUM(CASE WHEN quality = 'BAD' THEN 1 ELSE 0 END) as bad_readings,
         ROUND(
             SUM(CASE WHEN quality = 'GOOD' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),

             2) as quality_percent         FROM raw_time_series WHERE                  event_timestamp >= TIMESTAMP '2023-01-01 00:00:00'
         GROUP BY asset_id, property_alias HAVING COUNT(*) > 10"

    CASE Statement and COUNT(*) Examples:
        "SELECT asset_id, COUNT(*) as total_records,
         CASE WHEN COUNT(*) = 0 THEN 'No Data' ELSE 'Has Data' END as data_status
         FROM raw_time_series GROUP BY asset_id"

    Query Optimization Guidelines (From AWS Documentation):

    1. METADATA FILTERS -         Use WHERE clause with these operators for metadata fields:
       - Equals (=), Not equals (!=), LIKE, IN, AND, OR
       - Use literals on right side of operators for better performance

    2. RAW DATA FILTERS - Always filter on event_timestamp using:
       - Equals (
           =), Greater than (>), Less than (<), Greater/Less than or                equals (>=,
           <=)       - BETWEEN, AND operators
       - Avoid != and OR operators as they don't limit data scan effectively

    3. PRECOMPUTED AGGREGATES - Always specify:
       - Quality filter (quality = 'GOOD') to reduce data scanned
       - Resolution filter (1m, 15m, 1h, 1d) to avoid full table scan

    4. JOIN OPTIMIZATION:
       - Use implicit JOINs instead of explicit JOIN keyword when possible
       - Push metadata filters into subqueries for better performance
       - Apply filters on individual JOINed tables to minimize data scanned

    5. PERFORMANCE TIPS:
       - Use LIMIT clause to reduce data scanned for some queries
       - Set page size to maximum 20000 for large queries
       - Use attribute value columns (
           double_attribute_value,
           etc.) for better performance than latest_value_time_series       -                Filter on asset_id, property_id for indexed access
       - Always include quality = 'GOOD' filters for reliable data

    
---

# Execute Query

Execute comprehensive SQL queries against AWS IoT SiteWise data using the executeQuery API.

    The AWS IoT SiteWise query language supports SQL capabilities including:
    - Views: asset, asset_property, raw_time_series,         latest_value_time_series, precomputed_aggregates
    - SQL clauses: SELECT, FROM, WHERE, GROUP BY, ORDER BY, HAVING, LIMIT
    - Functions: Aggregation, date/time, string, mathematical, conditional
    - Operators: Comparison, logical, arithmetic, pattern matching (LIKE)
    - JOIN operations: JOIN, LEFT JOIN,
        UNION (prefer implicit joins for performance)

    Available Views and Schema (From Official AWS Documentation):

    ASSET VIEW: Contains information about the asset and model derivation
    - asset_id (string), asset_name (string), asset_description (string)
    - asset_model_id (string), parent_asset_id (string),
        asset_external_id (string)
    - asset_external_model_id (string), hierarchy_id (string)

    ASSET_PROPERTY VIEW: Contains information about the asset property's structure
    - asset_id (string), property_id (string), property_name (string),
        property_alias (string)
    - property_external_id (string), asset_composite_model_id (string),
        property_type (string)
    - property_data_type (string), int_attribute_value (integer),
        double_attribute_value (double)
    - boolean_attribute_value (boolean), string_attribute_value (string)

    RAW_TIME_SERIES VIEW: Contains the historical data of the time series
    - asset_id (string), property_id (string), property_alias (string),
        event_timestamp (timestamp)
    - quality (string), boolean_value (boolean), int_value (integer),
        double_value (double), string_value (string)

    LATEST_VALUE_TIME_SERIES VIEW: Contains the latest value of the time series
    - asset_id (string), property_id (string), property_alias (string),
        event_timestamp (timestamp)
    - quality (string), boolean_value (boolean), int_value (integer),
        double_value (double), string_value (string)

    PRECOMPUTED_AGGREGATES VIEW: Contains automatically computed         aggregated asset property values
    - asset_id (string), property_id (string), property_alias (string),
        event_timestamp (timestamp)
    - quality (string), resolution (string), sum_value (double),
        count_value (integer)
    - average_value (double), maximum_value (double),
        minimum_value (double), stdev_value (double)

    Complete SQL Function Reference (From AWS IoT SiteWise User Guide):

    DATE/TIME FUNCTIONS:
    - DATE_ADD(
        unit,
        value,
        date): Add time to date (e.g.,
        DATE_ADD(DAY, 7, event_timestamp))    - DATE_SUB(
        unit,
        value,
        date): Subtract time from date (e.g.,
        DATE_SUB(
            YEAR,
            2,
            event_timestamp))    - TIMESTAMP_ADD(
                unit,
                value,
                timestamp): Add time to timestamp
    - TIMESTAMP_SUB(unit, value, timestamp): Subtract time from timestamp
    - NOW(
        ): Current timestamp (supported,
        but use TIMESTAMP_ADD/SUB for math operations)    -             TIMESTAMP literals: Use TIMESTAMP '2023-01-01 00:00:00' for specific dates
    - CAST(expression AS TIMESTAMP): Convert string to timestamp

    Note: NOW() IS supported. When doing math on NOW() or         any timestamp, use TIMESTAMP_ADD/TIMESTAMP_SUB functions rather than             +/- operators.

    TYPE CONVERSION FUNCTIONS:
    - TO_DATE(integer): Convert epoch milliseconds to date
    - TO_DATE(expression, format): Convert string to date with format
    - TO_TIMESTAMP(double): Convert epoch seconds to timestamp
    - TO_TIMESTAMP(string, format): Convert string to timestamp with format
    - TO_TIME(int): Convert epoch milliseconds to time
    - TO_TIME(string, format): Convert string to time with format
    - CAST(expression AS data_type): Convert between BOOLEAN, INTEGER,
        TIMESTAMP, DATE, STRING, etc.

    AGGREGATE FUNCTIONS:
    - AVG(expression): Average value
    - COUNT(expression): Count rows (COUNT(*) is supported)
    - MAX(expression): Maximum value
    - MIN(expression): Minimum value
    - SUM(expression): Sum values
    - STDDEV(expression): Standard deviation
    - GROUP BY expression: Group results
    - HAVING boolean-expression: Filter grouped results

    IMPORTANT LIMITATIONS:
    - Window functions, CTEs (WITH clauses), DISTINCT, SELECT *, and         ILIKE are NOT supported

    SUPPORTED FEATURES:
    - CASE statements (CASE WHEN...THEN...ELSE...END pattern) ARE supported
    - COUNT(*) IS supported (only SELECT * is blocked)
    - Use implicit JOINs for better performance when possible

    Args:
        query_statement: The SQL query statement to execute (max 64KB)
        region: AWS region (default: us-east-1)
        next_token: Token for paginated results
        max_results: Maximum results to return (1-4000, default: 100)

    Returns:
        Dictionary containing:
        - success: Boolean indicating query success
        - columns: List of column definitions
        - rows: List of result rows
        - next_token: Token for next page (if applicable)
        - query_statistics: Execution statistics
        - query_status: Query execution status

    Example Queries (Using Correct View and Column Names):

    Basic Asset Discovery:
        "SELECT asset_id, asset_name, asset_model_id FROM asset"

    Metadata Filtering:
        "SELECT a.asset_name, p.property_name FROM asset a, asset_property p             WHERE a.asset_id = p.asset_id AND a.asset_name LIKE 'Windmill%'"

    Value Filtering with Time Range:
        "SELECT a.asset_name, r.int_value FROM asset a, raw_time_series r
         WHERE a.asset_id = r.asset_id
         AND r.int_value > 30
         AND r.event_timestamp > TIMESTAMP '2022-01-05 12:15:00'
         AND r.event_timestamp < TIMESTAMP '2022-01-05 12:20:00'"

    Aggregation with Grouping:
        "SELECT MAX(d.int_value) AS max_int_value, d.asset_id
         FROM raw_time_series AS d
         GROUP BY d.asset_id
         HAVING MAX(d.int_value) > 5"

    Date/Time Manipulation:
        "SELECT r.asset_id, r.int_value,
         DATE_ADD(DAY, 7, r.event_timestamp) AS date_in_future,
         DATE_SUB(YEAR, 2, r.event_timestamp) AS date_in_past,
         TIMESTAMP_ADD(DAY, 2, r.event_timestamp) AS timestamp_in_future,
         TIMESTAMP_SUB(DAY, 2, r.event_timestamp) AS timestamp_in_past
         FROM raw_time_series AS r"

    Type Conversion Examples:
        "SELECT r.asset_id, TO_DATE(r.event_timestamp) AS date_value,
         TO_TIME(r.event_timestamp) AS time_value
         FROM raw_time_series AS r"

    Attribute Property Filtering (For Attribute Properties Only -         Note: Only one attribute value type can be non-null per property):
        "SELECT p.property_name,
         CASE
             WHEN p.string_attribute_value IS NOT NULL THEN p.string_attribute_value
             WHEN p.double_attribute_value IS NOT NULL THEN                  CAST(p.double_attribute_value AS STRING)
             ELSE 'NULL'
         END as attribute_value
         FROM asset_property p
         WHERE p.property_type = 'attribute'
         AND (p.string_attribute_value LIKE 'my-property-%' OR              p.double_attribute_value > 100.0)"

    Precomputed Aggregates (Include quality and resolution filters):
        "SELECT asset_id, property_id, average_value, event_timestamp
         FROM precomputed_aggregates
         WHERE quality = 'GOOD'
         AND resolution = '1h'
         AND event_timestamp BETWEEN TIMESTAMP '2023-01-01 00:00:00' AND              TIMESTAMP '2023-01-02 00:00:00'"

    Implicit JOIN for Better Performance:
        "SELECT a.asset_name, p.property_name, r.double_value
         FROM asset a, asset_property p, raw_time_series r
         WHERE a.asset_id = p.asset_id
         AND p.property_id = r.property_id
         AND r.quality = 'GOOD'"

    Data Quality Analysis:
        "SELECT asset_id, property_alias,
         SUM(CASE WHEN quality = 'GOOD' THEN 1 ELSE 0 END) as good_readings,
         SUM(CASE WHEN quality = 'BAD' THEN 1 ELSE 0 END) as bad_readings,
         ROUND(
             SUM(CASE WHEN quality = 'GOOD' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),

             2) as quality_percent         FROM raw_time_series WHERE                  event_timestamp >= TIMESTAMP '2023-01-01 00:00:00'
         GROUP BY asset_id, property_alias HAVING COUNT(*) > 10"

    CASE Statement and COUNT(*) Examples:
        "SELECT asset_id, COUNT(*) as total_records,
         CASE WHEN COUNT(*) = 0 THEN 'No Data' ELSE 'Has Data' END as data_status
         FROM raw_time_series GROUP BY asset_id"

    Query Optimization Guidelines (From AWS Documentation):

    1. METADATA FILTERS -         Use WHERE clause with these operators for metadata fields:
       - Equals (=), Not equals (!=), LIKE, IN, AND, OR
       - Use literals on right side of operators for better performance

    2. RAW DATA FILTERS - Always filter on event_timestamp using:
       - Equals (
           =), Greater than (>), Less than (<), Greater/Less than or                equals (>=,
           <=)       - BETWEEN, AND operators
       - Avoid != and OR operators as they don't limit data scan effectively

    3. PRECOMPUTED AGGREGATES - Always specify:
       - Quality filter (quality = 'GOOD') to reduce data scanned
       - Resolution filter (1m, 15m, 1h, 1d) to avoid full table scan

    4. JOIN OPTIMIZATION:
       - Use implicit JOINs instead of explicit JOIN keyword when possible
       - Push metadata filters into subqueries for better performance
       - Apply filters on individual JOINed tables to minimize data scanned

    5. PERFORMANCE TIPS:
       - Use LIMIT clause to reduce data scanned for some queries
       - Set page size to maximum 20000 for large queries
       - Use attribute value columns (
           double_attribute_value,
           etc.) for better performance than latest_value_time_series       -                Filter on asset_id, property_id for indexed access
       - Always include quality = 'GOOD' filters for reliable data

    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query_statement` | string | Yes | SQL query statement to execute against AWS IoT SiteWise data |
| `region` | string | No | AWS region |
| `next_token` | string | No | The token to be used for the next set of paginated results |
| `max_results` | integer | No | The maximum number of results to return (1-10000) |

## AWS CLI

```bash
aws iotsitewise execute-query --query-statement <query_statement> --next-token <next_token> --max-results <max_results>
```

## boto3

```python
import boto3

client = boto3.client('iotsitewise')
response = client.execute_query(
    QueryStatement=query_statement,
    NextToken=next_token,
    MaxResults=max_results,
)
```
