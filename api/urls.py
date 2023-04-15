from django.urls import path
from .views import CityList, CityDetail, HomeRoutes

urlpatterns = [
    path('cities/', CityList.as_view()),
    path('cities/<int:pk>/', CityDetail.as_view()),
    path('home_routes/', HomeRoutes.as_view()),
]