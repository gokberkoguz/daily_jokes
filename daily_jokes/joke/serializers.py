from rest_framework import serializers

from models.joke import Joke


class JokeSerializer(serializers.ModelSerializer):
    """
    Serializes the Joke model
    """

    class Meta:
        model = Joke

        fields = ["author", "joke", "answer", "rate"]
        read_only_fields = fields
        ref_name = "daily_jokes_joke"