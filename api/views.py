from django.shortcuts import render
from rest_framework import viewsets
from cities.models.route import Route
from .serializers import RouteSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
