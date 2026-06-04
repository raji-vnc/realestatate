from django.db import models
from django.conf import settings
from properties.models import Property

class Wishlist(models.Model):
    """A user's saved property (wishlist)."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='wishlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'property')
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.user.phone} - {self.property.title}"
