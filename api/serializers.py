from rest_framework import serializers
from cities.models.route import Route

from cities.models.route import Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'id_route', 'polilyne')