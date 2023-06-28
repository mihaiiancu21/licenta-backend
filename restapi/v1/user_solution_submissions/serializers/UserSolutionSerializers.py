from rest_framework import serializers

from restapi.models import UserSolutionSubmitted
from restapi.v1.problems.serializers.ProblemSerializers import ProblemSerializer


class UserSolutionSerializer(serializers.ModelSerializer):
    """
    This class is serializing UserSolutionSubmitted model
    """

    class Meta:
        model = UserSolutionSubmitted
        fields = "__all__"


class UserSolutionFullSerializer(serializers.ModelSerializer):
    """
    This class is serializing UserSolutionSubmitted model
    """

    problem = ProblemSerializer()

    class Meta:
        model = UserSolutionSubmitted
        fields = "__all__"
