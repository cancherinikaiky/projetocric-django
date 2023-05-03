from rest_framework import serializers

from event.models import Event
from api.serializers import RouteSerializer

class EventSerializer(serializers.ModelSerializer):
    routes = RouteSerializer(many=True)
    class Meta:
        model = Event
        fields = ('id', 'description', 'routes')