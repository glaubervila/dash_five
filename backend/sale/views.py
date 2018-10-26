from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Sum, Avg
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
import pandas 
from .models import *
from .serializers import *



class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_fields = ('id', 'store', 'checkout', 'number', 'date', 'is_canceled',)
    search_fields = ('number', )
    ordering_fields = ('number', 'date','start_time', 'amount')
    ordering = ('-start_time',)   

    def get_summary_by_date(self, year, month, day):
        """
        Retorna informacoes das vendas por data.
        """
        queryset = Ticket.objects.filter(
            date__year=year, 
            date__month=month, 
            date__day=day)

        # Valor Total dos tickets validos
        amount = queryset.filter(is_canceled=False).aggregate(Sum('amount'))['amount__sum'] or 0.00

        # Soma de todos os descontos aplicados em tickets validos.
        discount = queryset.filter(is_canceled=False).aggregate(Sum('discount'))['discount__sum'] or 0.00

        # Soma do valor de todos os tickets cancelados.
        canceled = queryset.filter(is_canceled=True).aggregate(Sum('amount'))['amount__sum'] or 0.00

        # Total liquido de Tickets ( total - cancelados - descontos )
        net_sale = amount - canceled - discount

        # Valor Medio dos Tickets incluindos os cancelados
        average = queryset.aggregate(Avg('amount'))['amount__avg'] or 0.00

        summary = dict({
            'net_sale': net_sale,
            'amount': amount,
            'discounts': discount,
            'canceled': canceled,
            'average': float("%.3f" % average),
            'count': queryset.count(),
            'count_canceled': queryset.filter(is_canceled=True).count(),
        })

        return summary


    @list_route()
    def today_summary(self, request):
        """
        get:
        Retorna informacoes das vendas do dia.
        """
        today = timezone.now()
        today_summary = self.get_summary_by_date(today.year, today.month, today.day)

        # Variacao percentual em relacao ao dia anterior
        yesterday = today + timedelta(days=-1)
        yesterday_summary = self.get_summary_by_date(yesterday.year, yesterday.month, yesterday.day)

        v0 = float(yesterday_summary.get('net_sale'))
        v1 = float(today_summary.get('net_sale'))

        # Calculo de Variacao Percentual (https://pt.wikihow.com/Calcular-a-Varia%C3%A7%C3%A3o-Percentual)
        pct_change = ((v1 - v0) / v0) * 100

        today_summary.update({
            'datetime': today,
            'pct_change': float("%.2f" % pct_change),
            'yesterday_net_sale':  v0
            })


        return Response(today_summary)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_fields = ('id', 'ticket', 'option', 'date_time', 'is_canceled',)
    search_fields = ('ticket', )
    ordering_fields = ('option', 'value', 'date_time',)
    ordering = ('-date_time',)       