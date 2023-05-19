from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from restapi.models import UsersRank
from restapi.permissions import get_permission_class
from restapi.v1.rank.serializers.RankSerializer import UserRankFullSerializer
from restapi.v1.users.serializers.UserSerializer import UserSerializer


class UserListView(generics.ListAPIView):
    """
    Get full list of the users
    """

    queryset = UsersRank.objects.all()
    serializer_class = UserRankFullSerializer

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


class UserUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get a specific user from db, or update/delete a certain user

    get:
        Get a specific user by id
    put:
        Update a specific user by id
    delete:
        Delete a specific user by id
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        user_object = self.get_object()
        user_object.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        user_object = self.get_object()
        serializer = UserSerializer(
            instance=user_object,
            data=request.data,
            partial=True, context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data="Data updates successfully", status=status.HTTP_204_NO_CONTENT
        )
