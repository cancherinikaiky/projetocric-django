from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=250)
    id_route = models.CharField(max_length=50, unique=True)
    polyline = models.CharField(max_length=5000,blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    def get_routes(self):
        data = Route.objects.all()
        return data
    
    def get_route(self, idRoute):
        return Route.objects.get(id_route=idRoute)