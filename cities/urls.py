from django.urls import path
from . import views


urlpatterns = [
    path('cidade/<int:pk>/', views.CityDetail.as_view(), name='city_detail'),
]