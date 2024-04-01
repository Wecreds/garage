from rest_framework.viewsets import ModelViewSet

from garage.models import Accessory, Category
from garage.serializers import AccessorySerializer, CategorySerializer

class AccessoryViewSet(ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer