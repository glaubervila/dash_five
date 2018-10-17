from django.shortcuts import render

from rest_framework import viewsets

from .models import *
from .serializers import *

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_fields = ('id', 'name', 'initials',)
    search_fields = ('name', 'initials')

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_fields = ('id','country', 'name', 'uf',)
    search_fields = ('name', 'uf')

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_fields = ('id','state', 'name', )
    search_fields = ('name',)    
    ordering = ('name',)