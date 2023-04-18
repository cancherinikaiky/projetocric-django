from rest_framework import serializers
from api.serializers import CitySerializer
from home.models import Home

class HomeSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)

    class Meta:
        model = Home
        fields = ('id', 'name', 'lat', 'lng', 'cities')