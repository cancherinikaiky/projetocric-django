from rest_framework import serializers

from cities.models import City
from api.serializers import RouteSerializer

class CityDetailSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ('id', 'name', 'coordinates', 'routes')

    def get_coordinates(self, obj):
        return {'lat': obj.lat, 'lng': obj.lng}