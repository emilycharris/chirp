from django.contrib import admin
from django.db import models
from main.models import Chirp, StopWord

# Register your models here.

class ChirpAdmin(admin.ModelAdmin):
    list_display = ['body', 'bird']
    search_fields = ['body']

admin.site.register(Chirp, ChirpAdmin)

class StopWordAdmin(admin.ModelAdmin):
    list_display = ['word'] # <-- allows us to not do __str__
    search_fields = ['word']

admin.site.register(StopWord, StopWordAdmin)
