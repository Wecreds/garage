from rest_framework.viewsets import ModelViewSet

from garage.models import Accessory
from garage.serializers import AccessorySerializer

class AccessoryViewSet(ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer