from rest_framework import serializers

from restapi.models import Problem


class ProblemSerializer(serializers.ModelSerializer):
    """
    This class is serializing Problem model
    """

    class Meta:
        model = Problem
        fields = (
            "id", "topic_type", "title", "description", "restrictions", "difficulty_level",
            "status", "task_description", "points"
        )
