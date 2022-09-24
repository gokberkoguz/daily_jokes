from rest_framework import serializers

from .models import Joke, User


class UserSerializer(serializers.ModelSerializer):
    """
    User
    """

    class Meta:
        model = User
        fields = ["email"]

class JokeSerializer(serializers.ModelSerializer):
    """
    Serializes the Joke model
    """

    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Joke

        fields = ["user", "joke", "answer", "rate"]
        read_only_fields = ["user", "rate"]
        ref_name = "daily_jokes_joke"

    def create(self, validated_data):
        return Joke.objects.create(**validated_data)
