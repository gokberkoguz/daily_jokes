from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .user import User


class Joke(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    joke = models.CharField(unique=True, blank=True, max_length=255)
    answer = models.CharField(unique=True, blank=True, max_length=255)
    rate = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    vote_count = models.IntegerField()
    is_user = models.BooleanField() #If used, we can prevent repeated jokes by updating it to True.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.joke, self.answer
