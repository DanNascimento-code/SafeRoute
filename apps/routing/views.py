
from django.http import JsonResponse
from services.routing_service import get_safe_route


def safe_route_view(request):
  
    origin = request.GET.get("origin")
    destination = request.GET.get("destination")

    if not origin or not destination:
        return JsonResponse(
            {
                "error": "Missing required parameters",
                "details": "Both 'origin' and 'destination' are required."
            },
            status=400
        )

    try:
        
        result = get_safe_route(origin, destination)

       
        return JsonResponse(
            {
                "status": "success",
                "data": result
            },
            status=200
        )

    except Exception as e:
        
        return JsonResponse(
            {
                "status": "error",
                "message": "Internal server error",
                "details": str(e)
            },
            status=500
        )