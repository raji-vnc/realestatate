from django.contrib import admin
from .models import TenantApplication, RentalAgreement

@admin.register(TenantApplication)
class TenantApplicationAdmin(admin.ModelAdmin):
    list_display = ['tenant', 'property', 'status', 'applied_at', 'approved_at']
    list_filter = ['status']
    search_fields = ['tenant__phone', 'property__title']
    raw_id_fields = ['tenant', 'property']

@admin.register(RentalAgreement)
class RentalAgreementAdmin(admin.ModelAdmin):
    list_display = ['tenant', 'property', 'start_date', 'end_date', 'status']
    list_filter = ['status']
    search_fields = ['tenant__phone', 'property__title']
    raw_id_fields = ['tenant', 'property']

