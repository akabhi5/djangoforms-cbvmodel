from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Person
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class PersonCreateView(CreateView):
    model = Person
    template_name = 'create.html'
    fields = ['name', 'age']


class HomePageView(ListView):
    model = Person
    template_name = 'home.html'

class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'update.html'
    fields = ['name', 'age']

class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
