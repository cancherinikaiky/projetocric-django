from .models import Home
from cities.models import City

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=City)
def update_home(sender, instance, **kwargs):
    if not instance.visible:
        home = Home.objects.filter(city=instance).first()
        if home:
            home.delete()
            return

    home, created = Home.objects.get_or_create(city=instance)
    home.save()
