from rest_framework import serializers
from cities.models.city import City
from api.serializers import RouteSerializer

class CityDetailSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'routes')