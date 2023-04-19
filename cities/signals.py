from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models.api_strava import Api
from unidecode import unidecode

from .models import Route

@receiver(pre_save, sender=Route)
def insert_polyline(sender, instance, **kwargs):
    api = Api()
    try:
        polyline = api.get_route(instance.id_route)
        instance.polyline = polyline
    except KeyError:
        instance.polyline = None

def replace(name):
    return unidecode(name).strip().lower().replace(' ', '_').replace('-', '_')
