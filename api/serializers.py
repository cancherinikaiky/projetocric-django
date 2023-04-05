from rest_framework import serializers
from cities.models.route import Route
from cities.models.city import City

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'id_route', 'polilyne')

class CitySerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    class Meta:
        model =  City
        fields = ('id', 'name', 'routes')
