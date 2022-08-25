from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField()
    is_author = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email

    
class Joke(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    joke = models.CharField(unique=True, blank=True, max_length=255)
    answer = models.CharField(unique=True, blank=True, max_length=255)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    vote_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.joke, self.answer