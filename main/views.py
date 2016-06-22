from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from main.models import Chirp, StopWord, Profile

# Create your views here.

class IndexView(CreateView):
      template_name = "index.html"
      model = Chirp
      fields = ["body"]
      success_url = reverse_lazy("index_view")

      def form_valid(self, form):
          stop_words = StopWord.objects.all()
          # if trump/clinton/or sanders in body, add error
          chirp_body = form.cleaned_data["body"].lower()
          for stop_word in stop_words:
              if stop_word.word in chirp_body:
                  form.add_error("body", "You've said a bad word. I'm going to tell on you.")
                  return self.form_invalid(form)
          chirp = form.save(commit=False)
          chirp.bird = self.request.user
          return super().form_valid(form)


      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context["object_list"] = Chirp.objects.all()
          context["amount"] = Chirp.objects.all().count()
          return context

class ChirpDetailView(DetailView):
    model = Chirp

    #use for detail transactions in homework
    def get_queryset(self):
        return Chirp.objects.filter(bird=self.request.user) #do this for security




class ProfileUpdateView(UpdateView):

    fields = ['favorite_bird']
    success_url = reverse_lazy("profile_update_view")

    def get_object(self, queryset=None):
        return self.request.user.profile
        #override the requirement to have slug or pk


class ChirpDeleteView(DeleteView):
    success_url = reverse_lazy("index_view")


    def get_queryset(self):   # <-- for security
        return Chirp.objects.filter(bird=self.request.user)
