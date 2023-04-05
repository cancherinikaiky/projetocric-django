from django.urls import path
from .views import CityList

urlpatterns = [
    path('routes/', CityList.as_view()),
]