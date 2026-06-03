from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['phone', 'email', 'is_owner', 'is_tenant', 'is_staff', 'is_active']
    list_filter = ['is_owner', 'is_tenant', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Custom Roles', {'fields': ('is_owner', 'is_tenant')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'email', 'password', 'is_owner', 'is_tenant'),
        }),
    )
    search_fields = ['phone', 'email']
    ordering = ['phone']

admin.site.register(CustomUser, CustomUserAdmin)

