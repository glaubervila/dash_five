from rest_framework import serializers
from .models import *

from market.models import Store, Checkout

class TicketSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(
        queryset=Store.objects.all(), many=False)

    checkout = serializers.PrimaryKeyRelatedField(
        queryset=Checkout.objects.all(), many=False)

    class Meta:
        model = Ticket
        fields = (
            'id',
            'store',
            'checkout',
            'number',
            'date',
            'start_time',
            'amount',
            'discount',
            'is_canceled',
        )

class PaymentSerializer(serializers.ModelSerializer):
    ticket = serializers.PrimaryKeyRelatedField(
        queryset=Ticket.objects.all(), many=False)


    class Meta:
        model = Payment
        fields = (
            'id',
            'ticket',
            'option',
            'value',
            'date_time',
            'is_canceled',
        )
