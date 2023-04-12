from django.shortcuts import render
from django.views.generic.list import ListView
from home.models import Home

class PostHome(ListView):
    template_name = 'home/index.html'
    queryset = Home.objects.all()
    context_object_name = 'homes'