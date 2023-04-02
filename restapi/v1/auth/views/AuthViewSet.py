import base64
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from permissions import get_permission_class
from restapi.utils.session_authentication import CsrfExemptSessionAuthentication
from restapi.v1.auth.serializers.AuthSerializer import LoginSerializer, RegisterSerializer
from restapi.v1.users.serializers.UserSerializer import UserSerializer


@ensure_csrf_cookie
def set_csrf_token(request):
    """
    This will be `/api/set-csrf-cookie/` on `urls.py`
    """
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
            token = get_session_token(cuid=serializer.data.get('cuid'), reason='activate-user')
            # MailUtils.send_user_awaiting_activation(user=user, token=token)

            user_serializer = UserSerializer(user)
            return Response(data=user_serializer.data, status=status.HTTP_200_OK)
            # return Response(
            #     data='Signup successful, you will receive a validation email.', status=status.HTTP_201_CREATED
            # )
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


def get_session_token(cuid, reason, expiry=172800):
    # Remove all expired sessions
    SessionStore().clear_expired()
    new_session = SessionStore()
    new_session[reason] = cuid
    new_session.set_expiry(expiry)  # with "timedelta(days=2)" won't work... :(
    new_session.create()
    return new_session.session_key
