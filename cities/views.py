from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from cities.models import City

def charqueadas(resquest):
    return render(resquest, 'cities/charqueadas.html')

def vale_verde(request):
    return render(request, 'cities/vale_verde.html')

# def cidade(request, post_name):
#     name_filtered = post_name.lower().replace(" ", "_")
#     return render(request, 'cities/' + name_filtered + '.html')

class CityDetail(DetailView):
    model = City
    template_name = 'cities/city_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = City.objects.get(pk=self.kwargs['pk'])
        return context