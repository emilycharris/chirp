from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from main.models import Chirp

# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    model = Chirp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #you have to have this line
        context['amount'] = Chirp.objects.all().count()
        return context

class ChirpDetailView(DetailView):
    model = Chirp

    #use for detail transactions in homework
    def get_queryset(self):
        return Chirp.objects.filter(bird=self.request.user) #do this for security

class ChirpCreateView(CreateView):
    model = Chirp
    fields = ['body']
    success_url = '/'

    #to add authenticated user to chirp automatically
    #creates instance of chirp without actually updating database

    def form_valid(self, form):

        chirp = form.save(commit=False)
        chirp.bird = self.request.user
        return super().form_valid(form)
