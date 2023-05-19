from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from restapi.models import UsersRank
from restapi.permissions import get_permission_class
from restapi.v1.rank.serializers.RankSerializer import RankSerializer


class RankListView(generics.ListAPIView):
    """
    Get full list of user from rank table
    """

    queryset = UsersRank.objects.all()
    serializer_class = RankSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RankRetrieveView(generics.RetrieveAPIView):
    """
    Get rank by username
    """

    serializer_class = RankSerializer
    permission_classes = get_permission_class(default=IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        try:
            user_found = UsersRank.objects.get(
                user__username=kwargs.get('search_value', None)
            )
            serializer = self.get_serializer(user_found)
            return Response(serializer.data)

        except ObjectDoesNotExist:
            raise NotFound(detail="The User is not registered.", code="user_not_found")
