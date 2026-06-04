from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    """Manager for CustomUser where phone is the unique identifier."""

    def create_user(self, phone, email=None, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone must be set')
        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone, email, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)

    # Make phone number the primary identifier - set as required
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.phone

