from django.urls import path
from .views import ModelsAPIVIEW

urlpatterns = [
    path('routes/', ModelsAPIVIEW.as_view()),
]