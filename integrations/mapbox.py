
import random
import uuid

def _generate_fake_geometry():

    return [
        {"lat": -23.55 + random.uniform(-0.01, 0.01),
         "lng": -46.63 + random.uniform(-0.01, 0.01)}
         for _ in range(10)
    ]

def _generate_route(base_distance: int, variability: int):

    distance = base_distance + random.randint(-variability, variability)
    duration = int(distance / 2) + random.randint(-50, 50)

    return {
        "id": str(uuid.uuid4()),
        "distance": max(distance, 100),
        "duration": max(duration, 60),
        "geometry": _generate_fake_geometry(),
    }    

def get_routes(origin: str, destination: str):

    base_distance = random.randint(1000, 5000)

    routes = [
        _generate_route(base_distance, 300),
        _generate_route(base_distance, 600),
        _generate_route(base_distance, 900),
    ]    

    return routes