from django.shortcuts import render
from rest_framework import generics
from cities.models.city import City
from .serializers.city import CitySerializer

from cities.models.route import Route
from .serializers import RouteSerializer

class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = City.objects.filter(visible=True)
        return queryset

class RouteMaps(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get_queryset(self):
        queryset = Route.objects.filter(active=True)
        return queryset