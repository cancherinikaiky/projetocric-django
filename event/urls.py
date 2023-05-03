from django.urls import path
from .import views

urlpatterns = [
    path('<int:pk>/', views.EventView.as_view(), name='event'),
]