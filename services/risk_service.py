
import random


def distance_score(route: dict) -> float:
    
    max_distance = 10000  
    return min(route["distance"] / max_distance, 1)


def duration_score(route: dict) -> float:
  
    max_duration = 3600  
    return min(route["duration"] / max_duration, 1)


def lighting_score(route: dict) -> float:
   
    return random.uniform(0, 1)


def crime_score(route: dict) -> float:
   
    return random.uniform(0, 1)



WEIGHTS = {
    "distance": 0.2,
    "duration": 0.2,
    "lighting": 0.3,
    "crime": 0.3,
}


def calculate_route_risk(route: dict) -> dict:
   
    d_score = distance_score(route)
    t_score = duration_score(route)
    l_score = lighting_score(route)
    c_score = crime_score(route)

    total_risk = (
        WEIGHTS["distance"] * d_score +
        WEIGHTS["duration"] * t_score +
        WEIGHTS["lighting"] * l_score +
        WEIGHTS["crime"] * c_score
    )

    return {
        "score": round(total_risk * 100, 2),  # escala 0–100
        "breakdown": {
            "distance": round(d_score, 3),
            "duration": round(t_score, 3),
            "lighting": round(l_score, 3),
            "crime": round(c_score, 3),
        }
    }