from rest_framework import generics, status
from rest_framework.response import Response

from restapi.models import ProblemExamples
from restapi.v1.problems_examples.serializers.ProblemExampleSerializers \
    import ProblemExampleSerializer


class ProblemExampleView(generics.ListAPIView):
    """
    Get full list of topics
    """

    queryset = ProblemExamples.objects.all()
    serializer_class = ProblemExampleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
