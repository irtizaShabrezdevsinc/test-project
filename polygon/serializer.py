from rest_framework import serializers
from .models import Polygon


class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygon
        depth = 1
        fields = '__all__'
    

class PolygonLatLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygon
        fields = ['longitude', 'latitude']
