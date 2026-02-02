from rest_framework import viewsets # type: ignore

from .models import InventoryItem, User

from .serializers import InventoryItemSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = UserSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):

    queryset = InventoryItem.objects.all()

    serializer_class = InventoryItemSerializer