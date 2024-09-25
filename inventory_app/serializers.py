from rest_framework import serializers
from .models import Inventory_model

class Inventory_serializers(serializers.ModelSerializer):
    class Meta:
        model = Inventory_model
        fields='__all__'