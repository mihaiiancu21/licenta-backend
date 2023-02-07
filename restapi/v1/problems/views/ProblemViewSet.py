from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response

from restapi.models import Problem
from restapi.v1.problems.serializers.ProblemSerializers import ProblemSerializer


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
                return Response(data="Request not allowed", status=status.HTTP_401_UNAUTHORIZED)
        return Response(data="Problem was inserted successfully", status=status.HTTP_201_CREATED)


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
        serializer = ProblemSerializer(instance=problem, data=request.data, partial=True, context={'request': request})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data="Data updates successfully", status=status.HTTP_204_NO_CONTENT)
