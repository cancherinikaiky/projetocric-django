from django.urls import path
from .views import CityList, RouteMaps

urlpatterns = [
    path('cities/', CityList.as_view()),
    path('routes_maps/', RouteMaps.as_view()),
]