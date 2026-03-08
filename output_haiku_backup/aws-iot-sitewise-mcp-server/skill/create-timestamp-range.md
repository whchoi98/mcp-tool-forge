---
name: create-timestamp-range
description: Create a formatted timestamp range from start and end timestamps.

    This tool formats a range of timestamps for display, useful for showing
    training periods, evaluation periods, or other time ranges.

    Args:
        start_timestamp: Start Unix epoch timestamp
        end_timestamp: End Unix epoch timestamp
        format_string: Python strftime format string for output formatting

    Returns:
        Dictionary containing formatted range and individual conversions

    Example:
        # Create a training period range
        result = create_timestamp_range(1727740800, 1729123200)
        # Returns formatted range like "October 01, 2024 - October 17, 2024"
    
---

# Create Timestamp Range

Create a formatted timestamp range from start and end timestamps.

    This tool formats a range of timestamps for display, useful for showing
    training periods, evaluation periods, or other time ranges.

    Args:
        start_timestamp: Start Unix epoch timestamp
        end_timestamp: End Unix epoch timestamp
        format_string: Python strftime format string for output formatting

    Returns:
        Dictionary containing formatted range and individual conversions

    Example:
        # Create a training period range
        result = create_timestamp_range(1727740800, 1729123200)
        # Returns formatted range like "October 01, 2024 - October 17, 2024"
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `start_timestamp` | string | Yes |  |
| `end_timestamp` | string | Yes |  |
| `format_string` | string | No |  |

