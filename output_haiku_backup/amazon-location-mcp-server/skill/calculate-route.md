---
name: calculate-route
description: Calculate a route and return summary info and turn-by-turn directions.

    Parameters:
        departure_position: [lon, lat]
        destination_position: [lon, lat]
        travel_mode: 'Car', 'Truck', 'Walking', or 'Bicycle' (default: 'Car')
        optimize_for: 'FastestRoute' or 'ShortestRoute' (default: 'FastestRoute')

    Returns:
        dict with distance, duration, and turn_by_turn directions (list of step summaries).
    
---

# Calculate Route

Calculate a route and return summary info and turn-by-turn directions.

    Parameters:
        departure_position: [lon, lat]
        destination_position: [lon, lat]
        travel_mode: 'Car', 'Truck', 'Walking', or 'Bicycle' (default: 'Car')
        optimize_for: 'FastestRoute' or 'ShortestRoute' (default: 'FastestRoute')

    Returns:
        dict with distance, duration, and turn_by_turn directions (list of step summaries).
    

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `departure_position` | array | Yes | Departure position as [longitude, latitude] |
| `destination_position` | array | Yes | Destination position as [longitude, latitude] |
| `travel_mode` | string | No | Travel mode: 'Car', 'Truck', 'Walking', or 'Bicycle' (default: 'Car') |
| `optimize_for` | string | No | Optimize route for 'FastestRoute' or 'ShortestRoute' (default: 'FastestRoute') |

## AWS CLI

```bash
aws location calculate-route --departure-position <departure_position> --destination-position <destination_position> --travel-mode <travel_mode> --optimize-for <optimize_for>
```

## boto3

```python
import boto3

client = boto3.client('location')
response = client.calculate_route(
    DeparturePosition=departure_position,
    DestinationPosition=destination_position,
    TravelMode=travel_mode,
    OptimizeFor=optimize_for,
)
```
