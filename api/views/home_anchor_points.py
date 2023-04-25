from rest_framework import generics

from api.serializers import HomeSerializer
from home.models import Home
from cities.models import City

class HomeAnchorPoints(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

    def get_queryset(self):
        homes = super().get_queryset()
        query_cities = City.objects.filter(visible=True)

        for home in homes:
            points = []

            for city in query_cities:

                city_points = city.points.all()

                for point in city_points:
                    point_data = {
                    'id': point.id,
                    'name': point.name,
                    'phone': point.phone,
                    }

                    if point_data not in points:
                        points.append(point_data)

            home.points = points
        return homes