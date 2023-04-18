from django.shortcuts import render
from rest_framework import generics

from cities.models import Route
from api.serializers import HomeSerializer
from home.models import Home
from home.models import CityManager

from cities.models import City

class HomeRoutes(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

    def get_queryset(self):
        homes = super().get_queryset()
        query_cities = City.objects.filter(visible=True)
        for home in homes:
            cities = []
            for city in query_cities:
                routes = city.routes.all()
                city_data = {
                    'name': city.name,
                        'lat': city.lat,
                        'lng': city.lng,
                        'banner_photo': city.banner_photo,
                        'routes': [{'name': r.name, 'id_route': r.id_route, 'polilyne': r.polilyne} for r in routes],
                }
                cities.append(city_data)
            home.cities = cities
        return homes
        