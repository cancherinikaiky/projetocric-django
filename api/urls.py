from django.urls import path
from .views import CityList, RoutesMaps

urlpatterns = [
    path('cities/', CityList.as_view()),
    path('routes_maps/', RoutesMaps.as_view()),
]