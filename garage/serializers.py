from rest_framework.serializers import ModelSerializer

from garage.models import Accessory, Category

class AccessorySerializer(ModelSerializer):
    class Meta:
        model = Accessory
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"