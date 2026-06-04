from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Inquiry
from .serializers import InquirySerializer


class InquiryListCreateView(generics.ListCreateAPIView):
    """GET  /inquiries/  – list all inquiries (admin/authenticated only)
    POST /inquiries/  – create a new inquiry (public endpoint).
    """
    queryset = Inquiry.objects.all().order_by('-created_at')
    serializer_class = InquirySerializer

    def get_permissions(self):
        # Allow anyone to create (POST), but require authentication for listing (GET)
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inquiry = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"inquiry": InquirySerializer(inquiry).data},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
