import base64

from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from permissions import get_permission_class
from restapi.utils.session_authentication import CsrfExemptSessionAuthentication
from restapi.v1.auth.serializers.AuthSerializer import LoginSerializer
from restapi.v1.users.serializers.UserSerializer import UserSerializer


class Login(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        """
        Login User
        """

        serializer = self.get_serializer(data=request.data)
        # We keep an if here, because the exception is not a validation exception but an AuthenticationFailed exception

        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = base64.b64decode(serializer.validated_data.get("password"))
            as_standard_user = serializer.validated_data.get("as_standard_user", False)

            user = authenticate(request, username=username, password=password, as_standard_user=as_standard_user)
            if user is not None and user.is_active:
                login(request, user)
                user_serializer = UserSerializer(user)
                return Response(data=user_serializer.data, status=status.HTTP_200_OK)
        raise AuthenticationFailed()


class Logout(generics.RetrieveAPIView):
    """
    Logout endpoint
    """
    permission_classes = get_permission_class(default=AllowAny)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
