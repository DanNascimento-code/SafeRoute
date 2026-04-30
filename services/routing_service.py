
from integrations.mapbox import get_routes
from services.risk_service import calculate_route_risk


def get_safe_route(origin: str, destination: str) -> dict:
   
    routes = get_routes(origin, destination)

    enriched_routes = []

    for route in routes:
        risk_data = calculate_route_risk(route)

        enriched_route = {
            **route,
            "risk": risk_data["score"],
            "risk_breakdown": risk_data["breakdown"],
        }

        enriched_routes.append(enriched_route)

    sorted_routes = sorted(enriched_routes, key=lambda r: r["risk"])

    safest_route = sorted_routes[0]

    return {
        "origin": origin,
        "destination": destination,
        "recommended_route": safest_route,
        "alternative_routes": sorted_routes[1:],
        "total_routes_analyzed": len(sorted_routes),
    }