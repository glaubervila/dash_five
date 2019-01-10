from django.contrib import admin

from .models import Loja

@admin.register(Loja)
class LojaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cnpj', 'nome', 'nome_fantasia', 'pais', 'estado', 'cidade')
    search_fields = ('cnpj', 'nome', 'nome_fantasia')


# @admin.register(Checkout)
# class CheckoutAdmin(admin.ModelAdmin):
#     list_display = ('id','store', 'number',)
#     search_fields = ('number',)