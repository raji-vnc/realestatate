from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)

    # Make phone number the primary identifier - set as required
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.phone

