# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
#from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import User, Joke

LIST_PER_PAGE = 25

class UserAdmin(admin.ModelAdmin):
    """
    Inherits GuardedModelAdmin in order to manage
    Object Permission via Django Admin interface
    """
    readonly_fields = ['name']
    list_display = ('name',  'email', 'is_author')
    #list_filter = [('created_at', DateTimeRangeFilter)]
    search_fields = ['email']
    list_display_links = ['name', 'email']
    list_per_page = LIST_PER_PAGE


class JokeAdmin(admin.ModelAdmin):
    """
    Inherits GuardedModelAdmin in order to manage
    Object Permission via Django Admin interface
    """
    readonly_fields = ['author']
    list_display = ('author',  'joke',
                    'answer', 'rate', 
                    'vote_count', 'created_at')
    #list_filter = [('created_at', DateTimeRangeFilter)]
    search_fields = ['author']
    list_display_links = ['author', 'joke', 'answer']
    list_per_page = LIST_PER_PAGE

admin.site.register(User, UserAdmin)
admin.site.register(Joke, JokeAdmin)
