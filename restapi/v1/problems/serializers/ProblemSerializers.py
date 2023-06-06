from rest_framework import serializers

from restapi.models import Problem, ProblemTopics, ProblemExamples
from restapi.v1.problems_examples.serializers.ProblemExampleSerializers import (
    ProblemExampleSerializer,
)
from restapi.v1.topics.serializers.TopicSerializers import TopicSerializer


class ProblemSerializer(serializers.ModelSerializer):
    """
    This class is serializing Problem model
    """

    class Meta:
        model = Problem
        fields = (
            "id", "topic_type", "title", "description",
            "restrictions", "difficulty_level",
            "task_description", "points", "code_snapshot"
        )


class ProblemFullSerializer(serializers.ModelSerializer):
    topic_type = TopicSerializer()
    problem_example = ProblemExampleSerializer()

    class Meta:
        model = Problem
        fields = (
            "id", "topic_type", "problem_example",
            "title", "description", "restrictions",
            "difficulty_level", "task_description",
            "points", "code_snapshot"
        )

    def create(self, validated_data):
        # get topic type from serialization
        topic_type = validated_data.pop("topic_type")

        # get the object from DB. It will be used later in Problem model creation
        topic_type_obj = ProblemTopics.objects.get(topic=topic_type["topic"])

        # get problem_sample data from serialization
        problem_example = validated_data.pop("problem_example")

        # save the problem example
        problem_example_obj = ProblemExamples.objects.create(
            example_description=problem_example["example_description"]
        )

        problem_example_obj.save()

        problem = Problem.objects.create(
            topic_type=topic_type_obj,
            problem_example=problem_example_obj,
            title=validated_data["title"],
            description=validated_data["description"],
            restrictions=validated_data["restrictions"],
            difficulty_level=validated_data["difficulty_level"],
            task_description=validated_data["task_description"],
            points=validated_data["points"],
            code_snapshot=validated_data["code_snapshot"]
        )

        problem.save()

        return problem

    def update(self, instance, validated_data):

        if validated_data.get("topic_type"):
            # get topic type from serialization
            topic_type = validated_data.pop("topic_type")

            # get the object from DB. It will be used later in Problem model creation
            topic_type_obj = ProblemTopics.objects.get(topic=topic_type["topic"])
            instance.topic_type = topic_type_obj

        if validated_data.get("problem_example"):
            # get problem_sample data from serialization
            problem_example = validated_data.pop("problem_example")
            instance.problem_example.example_description = problem_example[
                "example_description"]
            instance.problem_example.save()

        instance.title = validated_data["title"]
        instance.description = validated_data["description"]
        instance.restrictions = validated_data["restrictions"]
        instance.difficulty_level = validated_data["difficulty_level"]
        instance.task_description = validated_data["task_description"]
        instance.points = validated_data["points"]
        instance.code_snapshot = validated_data["code_snapshot"]
        instance.save()

        return instance
