from rest_framework import serializers

from api.serializers import RouteSerializer
from home.models import Home

class HomeSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Home
        fields = ('id', 'name', 'coordinates', 'routes')

    def get_coordinates(self, obj):
        return {'lat': obj.lat, 'lng': obj.lng}