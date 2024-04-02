from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from garage.models import Accessory, Category, Color

class AccessorySerializer(ModelSerializer):
    class Meta:
        model = Accessory
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ColorSerializer(ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Color
        fields = ['id', 'name']
        
    def get_name(self, obj):
        return obj.name.upper()