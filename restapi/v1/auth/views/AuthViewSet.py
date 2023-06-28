import base64

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from restapi.models import UsersRank
from restapi.permissions import get_permission_class
from restapi.utils.session_authentication import CsrfExemptSessionAuthentication
from restapi.v1.auth.serializers.AuthSerializer import (
    LoginSerializer, RegisterSerializer, ResetPasswordSerializer
)
from restapi.v1.users.serializers.UserSerializer import UserSerializer, UserFullSerializer


@ensure_csrf_cookie
def set_csrf_token(request):
    """
    This will be `/api/set-csrf-cookie/` on `urls.py`
    """
    SessionStore().clear_expired()
    return JsonResponse({"details": "CSRF cookie set"})


class Login(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    authentication_classes = [SessionAuthentication]

    def create(self, request, *args, **kwargs):
        """
        Login User
        """

        serializer = self.get_serializer(data=request.data)
        # We keep an if here, because the exception is not a
        # validation exception but an AuthenticationFailed exception

        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = base64.b64decode(serializer.validated_data.get("password"))
            as_standard_user = serializer.validated_data.get("as_standard_user", False)

            user = authenticate(
                request, username=username, password=password,
                as_standard_user=as_standard_user
            )
            if user is not None and user.is_active:
                login(request, user)
                user_serializer = UserFullSerializer(user)
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


class Register(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Register a new User
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_session_token(
                username=serializer.data.get('username'), reason='activate-user'
            )

            # add user automatically in Rank table
            UsersRank.objects.create(user=user)
            # MailUtils.send_user_awaiting_activation(user=user, token=token)

            user_serializer = UserSerializer(user)
            return Response(data=user_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class ResetPassword(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ResetPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(User, username=serializer.data.get("username"))

        if user.email == serializer.data.get("email"):
            new_password = serializer.data.get("new_password")

            user.set_password(new_password)
            user.save()
        else:
            return Response(
                "The email is not in our database",
                status=status.HTTP_401_UNAUTHORIZED
            )

        SessionStore().clear_expired()

        return Response(status=status.HTTP_204_NO_CONTENT)


def get_session_token(username, reason, expiry=172800):
    # Remove all expired sessions
    SessionStore().clear_expired()
    new_session = SessionStore()
    new_session[reason] = username
    new_session.set_expiry(expiry)
    new_session.create()
    return new_session.session_key
