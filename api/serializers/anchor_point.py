from rest_framework import serializers

from cities.models import AnchorPoint
from api.serializers.category_point import CategoryPointSerializer

class AnchorPointSerializer(serializers.ModelSerializer):
    # category = CategoryPointSerializer(many=False)
    # coordinates = serializers.SerializerMethodField()

    class Meta:
        model = AnchorPoint
        fields = ('id', 'name','phone',)

    # def get_coordinates(self, obj):
    #     return {'lat': obj.lat, 'lng': obj.lng}