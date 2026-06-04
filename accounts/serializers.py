from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the custom user model.

    Handles creation with password hashing and representation of user fields.
    """

    class Meta:
        model = User
        fields = ["id", "phone", "email", "username", "password", "is_owner", "is_tenant"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
