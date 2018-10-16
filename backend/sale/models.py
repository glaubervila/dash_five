from django.db import models

from market.models import Store, Checkout


class Ticket(models.Model):

    store = models.ForeignKey(
        Store, 
        on_delete=models.CASCADE,
        verbose_name='Store'
    )

    checkout = models.ForeignKey(
        Checkout, 
        on_delete=models.CASCADE,
        verbose_name='Checkout'
    )

    number = models.PositiveIntegerField(
        verbose_name='Number',
    )

    date = models.DateField(
        verbose_name='Date',
        auto_now=False
    )

    start_time = models.DateTimeField(
        verbose_name='Start Time',
        auto_now=False
    )

    amount = models.DecimalField(
        verbose_name='Amount',
        max_digits=15,
        decimal_places=3
    )

    discount = models.DecimalField(
        verbose_name='Discount',
        max_digits=15,
        decimal_places=3,
        null=True, blank=True
    )

    is_canceled = models.BooleanField(
        verbose_name='Canceled',
        default=False
    )


class Payment(models.Model):

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        verbose_name='Ticket'
    )

    option = models.CharField(
        verbose_name='Option',
        max_length=128,
    )

    value = models.DecimalField(
        verbose_name='Value',
        max_digits=15,
        decimal_places=3
    )

    date_time = models.DateTimeField(
        verbose_name='Date Time',
        auto_now=False
    )

    is_canceled = models.BooleanField(
        verbose_name='Canceled',
        default=False
    )
