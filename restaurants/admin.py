from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from restaurants.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location', 'address', 'phone_number', 'website')
    search_fields = ('name', 'address')