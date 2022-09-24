from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


from .serializers import JokeSerializer
from .models import Joke


class JokeViewSet(generics.ListCreateAPIView):
    serializer_class = JokeSerializer

    def get_queryset(self):
        return Joke.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Creates a new Joke.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
