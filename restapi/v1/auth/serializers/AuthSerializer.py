from django.contrib.auth.models import User
from rest_framework import serializers

from rest_framework.validators import UniqueValidator


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True, help_text="User's username"
    )
    password = serializers.CharField(
        required=True, min_length=8, help_text="User's password"
    )

    as_standard_user = serializers.BooleanField(
        required=False, help_text="Login as a standard instead of an admin user"
    )


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=255, validators=[UniqueValidator(queryset=User.objects.all())], help_text="User's email"
    )
    password = serializers.CharField(required=True, min_length=8, help_text="User's password")
    first_name = serializers.CharField(required=True, max_length=30, allow_blank=True)
    last_name = serializers.CharField(required=True, max_length=150, allow_blank=True)

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            email=validated_data['email'],
            is_active=True
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
