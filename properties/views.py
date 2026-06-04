from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Property
from .serializers import PropertySerializer


class PropertyListCreateView(generics.ListCreateAPIView):
    """GET  /properties/  – list all properties (public).
    POST /properties/  – create a new property (owner must be authenticated).
    """
    queryset = Property.objects.all().order_by('-created_at')
    serializer_class = PropertySerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]

    def perform_create(self, serializer):
        # Set the owner to the requesting user
        serializer.save(owner=self.request.user)


class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    """GET /properties/<int:pk>/ – retrieve a property.
    PUT/PATCH – update (owner only).
    DELETE – delete (owner only).
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        # Ensure only the owner can modify; read is allowed for any authenticated user
        if self.request.method in ["PUT", "PATCH", "DELETE"] and obj.owner != self.request.user:
            self.permission_denied(self.request, message="Not the owner of this property")
        return obj
