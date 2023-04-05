from django.shortcuts import render
from rest_framework import generics
from cities.models.city import City
from .serializers.city import CitySerializer

class CityList(generics.ListAPIView):
    # queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = City.objects.filter(visible=True)
        return queryset