from django.db import models

from cities.models import Route

class RoutePath(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nome do caminho')
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    time = models.CharField(max_length=10, verbose_name='Horário de Sáida')

    def __str__(self):
        return self.name