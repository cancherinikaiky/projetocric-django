from rest_framework import serializers

from cities.models import AnchorPoint
from api.serializers.category_point import CategoryPointSerializer
from api.serializers.address_point import AddressPointSerializer

class AnchorPointSerializer(serializers.ModelSerializer):
    category = CategoryPointSerializer(many=False)
    address = AddressPointSerializer(many=False)
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = AnchorPoint
        fields = ('id', 'name', 'coordinates', 'category', 'phone', 'address')

    def get_coordinates(self, obj):
        return {'lat': obj.lat, 'lng': obj.lng}
    