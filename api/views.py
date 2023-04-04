from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from cities.models.route import Route
from cities.models.city import City
from .serializers import RouteSerializer
from .serializers import CitySerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from itertools import chain

# class RouteViewSet(viewsets.ModelViewSet):
#     queryset = Route.objects.all()
#     serializer_class = RouteSerializer

# class RouteViewSet(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         routes = Route.objects.all()
#         # cities = City.objects.all()
#         serializer1 = RouteSerializer(routes, many=True)
#         # serializer2 = CitySerializer(cities, many=True)
#         return Response({'routes': serializer1.data})

class ModelsAPIVIEW(generics.ListAPIView):
    def get_queryset(self):
        model1 = Route.objects.all()    
        model2 = City.objects.all()
        queryset = list(chain(model1, model2))
        return queryset

    # queryset = Route.objects.all()
    # serializer_class = RouteSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     model2 = City.objects.all()
    #     queryset = queryset | model2
    #     return queryset