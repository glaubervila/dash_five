from django.shortcuts import render

from rest_framework import viewsets

from .models import *
from .serializers import *

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_fields = ('id', 'name', 'social_name', 'state', 'city',)
    search_fields = ('name', 'social_name',)
    ordering = ('name',)

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = StoreSerializer
    filter_fields = ('id', 'store', 'number',)
    search_fields = ('number', )
    ordering = ('number',)    