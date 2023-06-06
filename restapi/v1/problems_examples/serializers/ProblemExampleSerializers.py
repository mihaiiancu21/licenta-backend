from rest_framework import serializers

from restapi.models import ProblemExamples


class ProblemExampleSerializer(serializers.ModelSerializer):
    """
    This class is serializing Problem Example model
    """

    class Meta:
        model = ProblemExamples
        fields = ("id", "example_description")
