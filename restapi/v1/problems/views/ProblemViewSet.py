from django.db import transaction
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response

from restapi.models import Problem
from restapi.v1.problems.serializers.ProblemSerializers import ProblemSerializer, \
    ProblemFullSerializer


class ProblemView(generics.ListCreateAPIView):
    """
    Get a list of problems existing in Database or create a new problem

    get:
    Retrieve all problems from DataBase

    post:
    Create a new Problem object in Database
    """

    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def list(self, request, *args, **kwargs):
        if request.query_params:
            level_filters = []
            topic_filter = []
            filtered_problems = []

            if "level_filter" in request.query_params:
                level_filters = request.query_params.get("level_filter").split(',')

            if "topic_filter" in request.query_params:
                topic_filter = request.query_params.get("topic_filter").split(',')

            if level_filters and topic_filter:
                filtered_problems = Problem.objects.filter(
                    Q(difficulty_level__in=level_filters) & Q(
                        topic_type__topic__in=topic_filter)
                )

            elif level_filters:
                filtered_problems = Problem.objects.filter(
                    Q(difficulty_level__in=level_filters)
                )

            elif topic_filter:
                filtered_problems = Problem.objects.filter(
                    Q(topic_type__topic__in=topic_filter)
                )

            serializer = self.get_serializer(filtered_problems, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            # todo de verificat daca linia de mai jos merge
            if request.user.is_superuser:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            else:
                return Response(
                    data="Request not allowed",
                    status=status.HTTP_401_UNAUTHORIZED
                )
        return Response(
            data="Problem was inserted successfully",
            status=status.HTTP_201_CREATED
        )


class ProblemUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get a specific problem from db, or update/delete a certain problem

    get:
        Get a specific problem by id
    put:
        Update a specific problem by id
    delete:
        Delete a specific problem by id
    """
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def delete(self, request, *args, **kwargs):
        problem = self.get_object()
        problem.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        problem = self.get_object()
        serializer = ProblemSerializer(instance=problem, data=request.data, partial=True,
                                       context={'request': request})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data="Data updates successfully", status=status.HTTP_204_NO_CONTENT)


class ProblemAdminView(generics.ListCreateAPIView):
    """
    Get a list of problems existing in Database or create a new problem

    get:
    Retrieve all problems from DataBase

    post:
    Create a new Problem object in Database
    """

    queryset = Problem.objects.all()
    serializer_class = ProblemFullSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
