from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from restapi.utils.session_authentication import CsrfExemptSessionAuthentication
from restapi.v1.users.serializers.UserSerializer import UserSerializer


class UserListView(generics.ListAPIView):
    """
    Get full list of the users
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
