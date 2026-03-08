---
name: convert-multiple-timestamps
description: Convert multiple Unix epoch timestamps to human-readable format.

    This tool converts multiple timestamps at once, useful for processing
    API responses that contain several timestamp fields.

    Args:
        timestamps: Dictionary of timestamp names and values
        format_string: Python strftime format string for output formatting

    Returns:
        Dictionary containing conversion results for all timestamps

    Example:
        # Convert multiple timestamps
        result = convert_multiple_timestamps({
            "lastTrainedAt": "1761805552",
            "lastTrainedStartTime": "1759276800",
            "lastTrainedEndTime": "1760659200"
        })
    
---

# Convert Multiple Timestamps

Convert multiple Unix epoch timestamps to human-readable format.

    This tool converts multiple timestamps at once, useful for processing
    API responses that contain several timestamp fields.

    Args:
        timestamps: Dictionary of timestamp names and values
        format_string: Python strftime format string for output formatting

    Returns:
        Dictionary containing conversion results for all timestamps

    Example:
        # Convert multiple timestamps
        result = convert_multiple_timestamps({
            "lastTrainedAt": "1761805552",
            "lastTrainedStartTime": "1759276800",
            "lastTrainedEndTime": "1760659200"
        })
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `timestamps` | object | Yes |  |
| `format_string` | string | No |  |

