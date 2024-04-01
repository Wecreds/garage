from rest_framework.viewsets import ModelViewSet

from garage.models import Accessory, Category, Color
from garage.serializers import AccessorySerializer, CategorySerializer, ColorSerializer

class AccessoryViewSet(ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer