from rest_framework import serializers
from .models import Restaurant
from diet.serializers import DietaryOptionSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    dietary_options = DietaryOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = [
            'id', 'name', 'location', 'address', 'images', 'description',
            'phone_number', 'website', 'dietary_options'
        ]
