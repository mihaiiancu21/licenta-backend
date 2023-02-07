from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    This class is serializing User model from Django
    """

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
