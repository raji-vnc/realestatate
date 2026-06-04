from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist
from .serializers import WishlistSerializer

class WishlistListCreateView(generics.ListCreateAPIView):
    """List and create wishlist items for the authenticated user."""
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WishlistDetailView(generics.RetrieveDestroyAPIView):
    """Retrieve or delete a single wishlist item (owner only)."""
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    queryset = Wishlist.objects.all()

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            self.permission_denied(self.request, message="Not your wishlist item")
        return obj
