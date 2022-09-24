from django.urls import include, path
from rest_framework import routers

from .views import JokeViewSet

app_name = "jokes"

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('joke/', JokeViewSet.as_view(), name='joke')
]