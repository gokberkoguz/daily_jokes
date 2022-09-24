from django.urls import include, path
from rest_framework import routers

from .views.joke import JokeList


app_name = "jokes"

router = routers.DefaultRouter()
router.register(r"joke_list", JokeList, basename="joke_list")
