from rest_framework import serializers
from .models import DietaryOption

class DietaryOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryOption
        fields = ['id', 'name', 'icon', 'color_light', 'color_dark']
