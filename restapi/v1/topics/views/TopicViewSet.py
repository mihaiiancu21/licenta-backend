from rest_framework import generics, status
from rest_framework.response import Response

from restapi.models import ProblemTopics
from restapi.v1.topics.serializers.TopicSerializers import TopicSerializer


class TopicsListView(generics.ListAPIView):
    """
    Get full list of topics
    """

    queryset = ProblemTopics.objects.all()
    serializer_class = TopicSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TopicUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get a specific problem topic from db, or update/delete a certain problem topic

    get:
        Get a specific topic by id
    put:
        Update a specific topic by id
    delete:
        Delete a specific topic by id
    """
    queryset = ProblemTopics.objects.all()
    serializer_class = TopicSerializer

    def delete(self, request, *args, **kwargs):
        problem_topic = self.get_object()
        problem_topic.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        problem_topic = self.get_object()
        serializer = TopicSerializer(
            instance=problem_topic,
            data=request.data,
            partial=True, context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data="Data updates successfully", status=status.HTTP_204_NO_CONTENT)
