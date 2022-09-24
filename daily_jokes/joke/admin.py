from django.contrib import admin
from .models import Joke
from .models import User

LIST_PER_PAGE = 25


class UserAdmin(admin.ModelAdmin):
    """
    Inherits GuardedModelAdmin in order to manage
    Object Permission via Django Admin interface
    """

    list_display = ("email", "is_author")
    # list_filter = [('created_at', DateTimeRangeFilter)]
    search_fields = ["email"]
    list_display_links = ["email"]
    list_per_page = LIST_PER_PAGE
    exclude = ('password',)

class JokeAdmin(admin.ModelAdmin):
    """
    Inherits GuardedModelAdmin in order to manage
    Object Permission via Django Admin interface
    """

    list_display = ("user", "joke", "answer", "rate", "vote_count", "created_at")
    # list_filter = [('created_at', DateTimeRangeFilter)]
    search_fields = ["user"]
    list_display_links = ["user", "joke", "answer"]
    list_per_page = LIST_PER_PAGE


admin.site.register(User, UserAdmin)
admin.site.register(Joke, JokeAdmin)
