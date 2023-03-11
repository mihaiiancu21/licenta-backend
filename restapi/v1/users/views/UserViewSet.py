from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from restapi.permissions import get_permission_class
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


class UserDetailsView(generics.RetrieveUpdateAPIView):
    """
    Get details by current user
    """
    permission_classes = get_permission_class(default=IsAuthenticated, )
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        current_user = request.user

        serializer = self.get_serializer(current_user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
