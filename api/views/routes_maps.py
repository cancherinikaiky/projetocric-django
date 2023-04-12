from django.shortcuts import render
from rest_framework import generics

from cities.models import Route
from api.serializers import RouteSerializer

class RoutesMaps(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get_queryset(self):
        queryset = Route.objects.filter(active=True)
        return queryset