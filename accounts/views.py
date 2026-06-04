from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# pyrefly: ignore [missing-import]
from .serializers import UserSerializer
from .models import CustomUser


class RegisterView(generics.CreateAPIView):
    """Register a new user (owner or tenant)."""
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Ensure phone is treated as string
        phone = serializer.validated_data.get('phone')
        serializer.validated_data['phone'] = str(phone)
        
        user = serializer.save()
        
        # Create token
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            "user": serializer.data,
            "token": token.key,
            "is_owner": user.is_owner,
            "is_tenant": user.is_tenant
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    """Login user and get token."""
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        password = request.data.get('password')

        if not phone or not password:
            return Response({
                'error': 'Phone and password are required'
            }, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.filter(phone=str(phone)).first()

        if not user or not user.check_password(password):
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key,
            "is_owner": user.is_owner,
            "is_tenant": user.is_tenant
        }, status=status.HTTP_200_OK)
