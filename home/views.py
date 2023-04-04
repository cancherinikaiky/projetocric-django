from django.shortcuts import render
from django.views.generic.list import ListView
from cities.models.route import Route
from cities.models.city import City

class PostHome(ListView):
    template_name = 'home/index.html'
    model = City
    context_object_name = 'cities'

# def index(request):
#     return render(request, 'home/index.html')