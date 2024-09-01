from django.contrib import admin

from diet.models import DietaryOption


@admin.register(DietaryOption)
class DietaryOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'color_light', 'color_dark')
    search_fields = ('name',)

