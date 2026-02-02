from rest_framework import serializers # type: ignore

from .models import InventoryItem, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ['id', 'username', 'email', 'is_staff']

        class InventoryItemSerializer(serializers.ModelSerializer):

            class Meta:
                model = InventoryItem

                fields = '__all__'