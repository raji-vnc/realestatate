from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from properties.models import Property
# If you have an Inquiry model, import it similarly:
# from ..inquiries.models import Inquiry

class DashboardView(generics.GenericAPIView):
    """Simple dashboard API endpoint.
    Returns summary statistics for the authenticated user:
    - Total number of properties owned
    - Total number of properties in the system
    - Recent properties (last 5 created)
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        # Total properties owned by the user
        owned_count = Property.objects.filter(owner=user).count()
        # Total properties in the system
        total_count = Property.objects.all().count()
        # Recent properties (last 5)
        recent_props = Property.objects.order_by('-created_at')[:5]
        recent_data = [
            {
                "id": prop.id,
                "title": prop.title,
                "city": prop.city,
                "price": str(prop.price),
                "created_at": prop.created_at,
            }
            for prop in recent_props
        ]

        data = {
            "owned_properties": owned_count,
            "total_properties": total_count,
            "recent_properties": recent_data,
        }
        return Response(data, status=status.HTTP_200_OK)
