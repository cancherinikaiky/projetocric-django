from django.db import models

from event.models.how_knew import HowKnew
from event.models import Event


class Bond(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Nome Completo')
    date_of_birth = models.DateField(verbose_name='Data de Nascimento')
    bond_choice = models.ForeignKey(Bond, on_delete=models.CASCADE, verbose_name='Categoria')
    how_knew = models.ForeignKey(HowKnew, on_delete=models.CASCADE, verbose_name='Como soube do evento?')
    rg = models.CharField(max_length=10, verbose_name='RG')
    route = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Trajeto desejado')

    def __str__(self):
        return self.full_name
    
    def get_bond_choice_display(self):
        if isinstance(self.bond_choice, str):
            return self.bond_choice.upper()
        else:
            return "-"
    