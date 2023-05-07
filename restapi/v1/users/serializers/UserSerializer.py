from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    This class is serializing User model from Django
    """

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "is_staff")
        read_only_fields = ('is_staff',)


class UserFullSerializer(UserSerializer):
    class Meta:
        model = UserSerializer.Meta.model
        fields = UserSerializer.Meta.fields + ('is_active', 'date_joined',)
        read_only_fields = UserSerializer.Meta.read_only_fields + ('date_joined',)
