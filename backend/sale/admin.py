from django.contrib import admin

from .models import Nfe, NfProduto

@admin.register(Nfe)
class NfeAdmin(admin.ModelAdmin):
    list_display = ('id', 'emitente', 'mod', 'serie', 'numero', 'data', 'n_item', 'v_total')
    search_fields = ('numero',)

@admin.register(NfProduto)
class NfeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nf', 'produto', 'descricao', 'quantidade', 'v_unitario', 'v_bruto_total', 'flag_total')
    # search_fields = ('descricao',)

# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'ticket', 'option', 'value', 'date_time', 'is_canceled')
#     search_fields = ('ticket',)    