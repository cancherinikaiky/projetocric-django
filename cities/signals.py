from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models.route import Route, Api
from .models.city import City
from unidecode import unidecode

@receiver(pre_save, sender=Route)
def insert_polilyne(sender, instance, **kwargs):
    api = Api()
    try:
        polilyne = api.getRoute(instance.id_route)
        instance.polilyne = polilyne
    except KeyError:
        instance.polilyne = None

@receiver(pre_save, sender=City)
def insert_id_map(sender, instance, **kwargs):
    instance.id_map = replace(instance.name)
    instance.banner_photo.name = replace(instance.banner_photo.name)

def replace(name):
    return unidecode(name).strip().lower().replace(' ', '_').replace('-', '_')
