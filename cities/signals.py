from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models.route import Route, Api


@receiver(pre_save, sender=Route)
def my_function(sender, instance, **kwargs):
    api = Api()
    try:
        polilyne = api.getRoute(instance.id_route)
        instance.polilyne = polilyne
    except KeyError:
        instance.polilyne = None