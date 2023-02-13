from rest_framework import serializers


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
