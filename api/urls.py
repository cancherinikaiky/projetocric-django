from django.urls import path
from .views import CityList

urlpatterns = [
    path('cities/', CityList.as_view()),
]