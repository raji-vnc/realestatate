from django.db import models
from django.conf import settings
from properties.models import Property

class TenantApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='applications')
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tenant.phone} for {self.property.title}"

class RentalAgreement(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='agreements')
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='agreements')
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='active') # active, completed, terminated
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Agreement for {self.property.title} with {self.tenant.phone}"
