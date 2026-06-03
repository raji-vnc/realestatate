from django.contrib import admin
from .models import Property, Amenity

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'city', 'state', 'price', 'bedrooms', 'bathrooms', 'owner', 'is_rented']
    list_filter = ['city', 'state', 'is_rented']
    search_fields = ['title', 'description', 'address', 'city']
    raw_id_fields = ['owner']

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

