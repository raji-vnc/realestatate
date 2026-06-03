from django.db import models
from django.conf import settings

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    year_built = models.IntegerField()
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')
    available_from = models.DateField(null=True, blank=True)
    is_rented = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} in {self.city}"

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    properties = models.ManyToManyField(Property, related_name='amenities', blank=True)

    def __str__(self):
        return self.name

