from django.contrib import admin
from django.db import models
from main.models import Chirp

# Register your models here.

class ChirpAdmin(admin.ModelAdmin):
    list_display = ['body', 'bird']
    search_fields = ['body']

admin.site.register(Chirp, ChirpAdmin)
