from rest_framework import generics
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.response import Response
from rest_framework import status

from serializers.joke import JokeSerializer


class JokeList(LoggingMixin, generics.ListAPIView):
    """List all jokes."""

    serializer_class = JokeSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new Report.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)