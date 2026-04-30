from django.urls import path
from .views import safe_route_view

urlpatterns = [
    path('safe-route/', safe_route_view),
]

