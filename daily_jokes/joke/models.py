from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)
    is_author = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Joke(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    joke = models.CharField(unique=True, blank=True, max_length=255)
    answer = models.CharField(unique=False, blank=True, max_length=255)
    rate = models.FloatField(
        default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    vote_count = models.IntegerField(default=0)
    is_used = models.BooleanField(
        default=False
    )  # If used, we can prevent repeated jokes by updating it to True.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.joke + "  " + self.answer
