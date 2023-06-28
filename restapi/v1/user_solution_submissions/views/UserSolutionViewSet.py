from django.db.models import OuterRef, Subquery
from rest_framework import generics, status
from rest_framework.response import Response

from restapi.models import Problem, UserSolutionSubmitted
from restapi.v1.user_solution_submissions.serializers.UserSolutionSerializers import (
    UserSolutionSerializer, UserSolutionFullSerializer,
)


class UserSolutionView(generics.ListAPIView):
    """
    Get all solutions submitted by user by a given problem id
    """
    queryset = Problem.objects.all()
    serializer_class = UserSolutionSerializer

    def list(self, request, *args, **kwargs):
        problem = self.get_object()
        user = request.user

        all_submissions = UserSolutionSubmitted.objects.filter(
            user=user, problem=problem
        )

        serializer = self.get_serializer(all_submissions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserAllMaxSolutionsView(generics.ListAPIView):
    """
    Get a list of submissions with max points per problem
    """

    serializer_class = UserSolutionSerializer

    def list(self, request, *args, **kwargs):
        user = request.user

        # filter all problems by max points and group by problem id
        sq = UserSolutionSubmitted.objects.filter(
            problem=OuterRef('problem'),
            user=user
        ).order_by('-points')  # deferred execution

        all_submissions = UserSolutionSubmitted.objects.filter(
            pk=Subquery(sq.values('pk')[:1])
        )

        serializer = self.get_serializer(all_submissions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserAllSolutionsView(generics.ListAPIView):
    """
    Get a list of all users submissions
    """
    serializer_class = UserSolutionFullSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = UserSolutionSubmitted.objects.filter(user=user)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
