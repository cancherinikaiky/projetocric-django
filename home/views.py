from django.shortcuts import render
from django.views.generic.list import ListView
from cities.models.city import City


class PostHome(ListView):
    template_name = 'home/index.html'
    model = City
