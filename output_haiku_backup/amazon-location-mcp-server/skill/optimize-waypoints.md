---
name: optimize-waypoints
description: Optimize the order of waypoints using Amazon Location Service geo-routes optimize_waypoints API (V2).

    Returns summary (optimized order, total distance, duration, etc.) or full response if mode='raw'.
    
---

# Optimize Waypoints

Optimize the order of waypoints using Amazon Location Service geo-routes optimize_waypoints API (V2).

    Returns summary (optimized order, total distance, duration, etc.) or full response if mode='raw'.
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `origin_position` | array | Yes | Origin position as [longitude, latitude] |
| `destination_position` | array | Yes | Destination position as [longitude, latitude] |
| `waypoints` | array | Yes | List of intermediate waypoints, each as a dict with at least Position [longitude, latitude], optionally Id |
| `travel_mode` | string | No | Travel mode: 'Car', 'Truck', 'Walking', or 'Bicycle' (default: 'Car') |
| `mode` | string | No | Output mode: 'summary' (default) or 'raw' for all AWS fields |

## AWS CLI

```bash
aws location calculate-route --calculator-name <ctx.config.calculator_name> --departure-position <origin_position> --destination-position <destination_position> --waypoints <waypoints> --travel-mode <travel_mode>
```

## boto3

```python
import boto3

client = boto3.client('location')
response = client.calculate_route(
    CalculatorName=ctx.config.calculator_name,
    DeparturePosition=origin_position,
    DestinationPosition=destination_position,
    Waypoints=waypoints,
    TravelMode=travel_mode,
)
```
