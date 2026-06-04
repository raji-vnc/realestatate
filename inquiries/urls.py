from django.urls import path
from .views import InquiryListCreateView

urlpatterns = [
    # POST /inquiries/ – public creation
    # GET  /inquiries/ – list inquiries (authenticated)
    path('inquiries/', InquiryListCreateView.as_view(), name='inquiry-list-create'),
]
