from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from main.models import Chirp

# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    model = Chirp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #you have to have this line
        context['amount'] = Chirp.objects.all().count()
        return context
