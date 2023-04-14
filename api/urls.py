from django.urls import path
from .views import CityList, CityDetail, RoutesMaps

urlpatterns = [
    path('cities/', CityList.as_view()),
    path('cities/<int:pk>/', CityDetail.as_view()),
    path('routes_maps/', RoutesMaps.as_view()),
]