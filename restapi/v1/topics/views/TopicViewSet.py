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