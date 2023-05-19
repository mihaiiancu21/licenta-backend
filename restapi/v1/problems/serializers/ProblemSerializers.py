from rest_framework import serializers

from restapi.models import Problem
from restapi.v1.topics.serializers.TopicSerializers import TopicSerializer


class ProblemSerializer(serializers.ModelSerializer):
    """
    This class is serializing Problem model
    """

    class Meta:
        model = Problem
        fields = (
            "id", "topic_type", "title", "description", "restrictions", "difficulty_level",
            "task_description", "points"
        )


class ProblemFullSerializer(serializers.ModelSerializer):
    topic_type = TopicSerializer()

    class Meta:
        model = Problem
        fields = (
            "id", "topic_type", "title", "description", "restrictions", "difficulty_level",
            "task_description", "points"
        )
