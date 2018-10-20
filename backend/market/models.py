from django.db import models
from common.models import Country, State, City

class Store(models.Model):

    name = models.CharField(
        max_length=1024,
        verbose_name='Name'
    )

    social_name = models.CharField(
        max_length=1024,
        verbose_name='Social Name'
    )

    number = models.PositiveIntegerField(
        verbose_name='Number',
        default=None,
        null=True, blank=True
    )

    country = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE, 
        verbose_name='Country'
    )

    state = models.ForeignKey(
        State, 
        on_delete=models.CASCADE, 
        verbose_name='State'
    )

    city = models.ForeignKey(
        City, 
        on_delete=models.CASCADE, 
        verbose_name='City'
    )

    adress = models.CharField(
        max_length=1024,
        verbose_name='Adress'
    )

    def __str__(self):
        return self.name

class Checkout(models.Model):

    store = models.ForeignKey(
        Store, 
        on_delete=models.CASCADE, 
        verbose_name='Store'
    )

    number = models.PositiveIntegerField(
        verbose_name='Number'
    )


    def __str__(self):
        return "%s - Checkout %s" % (self.store.name, str(self.number))