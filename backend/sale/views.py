from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_fields = ('id', 'store', 'checkout', 'number', 'date', 'is_canceled',)
    search_fields = ('number', )
    ordering_fields = ('number', 'date','start_time', 'amount')
    ordering = ('-start_time',)   

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_fields = ('id', 'ticket', 'option', 'date_time', 'is_canceled',)
    search_fields = ('ticket', )
    ordering_fields = ('option', 'value', 'date_time',)
    ordering = ('-date_time',)       