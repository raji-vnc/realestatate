from django.db import models

class Inquiry(models.Model):
    """Simple contact/inquiry model for potential tenants or owners."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} <{self.email}>"
