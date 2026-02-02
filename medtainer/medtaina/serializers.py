from rest_framework import serializers
from .models import InventoryItem, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

        class InventoryItemSerializer(serializers.ModelSerializer):
            class Meta:
                model = InventoryItem
                fields = ['id', 'name', 'description', 'quantity', 'price', 'last_updated'] 