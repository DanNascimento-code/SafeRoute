
import requests
import uuid
from config import settings


BASE_URL = "https://api.openrouteservice.org/v2/directions/foot-walking"


def get_routes(origin: str, destination: str):
   
    url = BASE_URL

    headers = {
        "Authorization": settings.OPENROUTE_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [
            [float(origin.split(",")[0]), float(origin.split(",")[1])],
            [float(destination.split(",")[0]), float(destination.split(",")[1])]
        ],
        
    }

    response = requests.post(url, json=body, headers=headers)

    if response.status_code != 200:
        raise Exception(f"OpenRouteService error: {response.text}")

    data = response.json()

    print(response.json())

    return _parse_routes(data)


def _parse_routes(data: dict):
    routes = []

    features = data.get("features", [])

    for feature in features:
        properties = feature.get("properties", {})
        summary = properties.get("summary", {})
        geometry = feature.get("geometry", {}).get("coordinates", [])

        if not summary or not geometry:
            continue

        parsed_route = {
            "id": str(uuid.uuid4()),
            "distance": summary.get("distance", 0),
            "duration": summary.get("duration", 0),
            "geometry": geometry,
            "risk": None
        }

        routes.append(parsed_route)

    return routes

