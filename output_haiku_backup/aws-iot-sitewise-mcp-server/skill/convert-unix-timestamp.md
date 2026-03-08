---
name: convert-unix-timestamp
description: Convert Unix epoch timestamp to human-readable format.

    This tool provides accurate timestamp conversion to prevent AI agents from
    making conversion errors when interpreting Unix timestamps from API responses.

    Args:
        timestamp: Unix epoch timestamp (seconds since 1970-01-01)
        format_string: Python strftime format string for output formatting
        timezone: Timezone for conversion (currently only supports UTC)

    Returns:
        Dictionary containing conversion results and metadata

    Example:
        # Convert a single timestamp
        result = convert_unix_timestamp(1727740800)
        # Returns: {
        #   "success": True,
        #   "timestamp": 1727740800,
        #   "formatted": "October 01, 2024 at 00:00:00 UTC",
        #   "iso_format": "2024-10-01T00:00:00+00:00",
        #   "year": 2024,
        #   "month": 10,
        #   "day": 1
        # }
    
---

# Convert Unix Timestamp

Convert Unix epoch timestamp to human-readable format.

    This tool provides accurate timestamp conversion to prevent AI agents from
    making conversion errors when interpreting Unix timestamps from API responses.

    Args:
        timestamp: Unix epoch timestamp (seconds since 1970-01-01)
        format_string: Python strftime format string for output formatting
        timezone: Timezone for conversion (currently only supports UTC)

    Returns:
        Dictionary containing conversion results and metadata

    Example:
        # Convert a single timestamp
        result = convert_unix_timestamp(1727740800)
        # Returns: {
        #   "success": True,
        #   "timestamp": 1727740800,
        #   "formatted": "October 01, 2024 at 00:00:00 UTC",
        #   "iso_format": "2024-10-01T00:00:00+00:00",
        #   "year": 2024,
        #   "month": 10,
        #   "day": 1
        # }
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timestamp` | string | Yes |  |
| `format_string` | string | No |  |
| `timezone` | string | No |  |

