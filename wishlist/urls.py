from django.urls import path
from .views import WishlistListCreateView, WishlistDetailView

urlpatterns = [
    # List/create wishlist items for the authenticated user
    path('wishlist/', WishlistListCreateView.as_view(), name='wishlist-list-create'),
    # Retrieve/delete a specific wishlist item
    path('wishlist/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
]
