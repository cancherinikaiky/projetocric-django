from django.shortcuts import render
from rest_framework import generics

from api.serializers import HomeSerializer
from home.models import Home
from cities.models import City

class HomeRoutes(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

    def get_queryset(self):
        homes = super().get_queryset()
        query_cities = City.objects.filter(visible=True)

        for home in homes:
            routes = []

            for city in query_cities:

                city_routes = city.routes.all()

                for route in city_routes:
                    route_data = {
                    'id': route.id,
                    'name': route.name,
                    'id_route': route.id_route,
                    'polilyne': route.polilyne,
                    }

                    if route_data not in routes:
                        routes.append(route_data)

            home.routes = routes
        return homes