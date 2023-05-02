from django.db import models

from cities.models import Route

class Event(models.Model):
    description = models.CharField(max_length=500, verbose_name="Descrição do evento", null=True)
    routes = models.ManyToManyField(Route, blank=True, null=True, verbose_name="Rotas do Evento")

    def __str__(self) -> str:
        return self.description