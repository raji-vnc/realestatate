from django.urls import path
from .views import PropertyListCreateView, PropertyDetailView

urlpatterns = [
    # List all properties (public) / create property (authenticated owner)
    path('properties/', PropertyListCreateView.as_view(), name='property-list-create'),
    # Retrieve / update / delete a specific property by id
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
]
