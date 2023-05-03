from django.shortcuts import render
from django.views.generic.detail import DetailView

from event.models import Event

class EventView(DetailView):
    model = Event
    template_name = 'events/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Event.objects.get(pk=self.kwargs['pk'])
        return context
