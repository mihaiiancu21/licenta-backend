from rest_framework import serializers

from restapi.models import ProblemTopics


class TopicSerializer(serializers.ModelSerializer):
    """
    This class is serializing Topic model
    """

    class Meta:
        model = ProblemTopics
        fields = ("id", "topic")
