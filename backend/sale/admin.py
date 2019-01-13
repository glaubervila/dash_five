from django.contrib import admin

from .models import Nfe, NfProduto, NfPagamento

@admin.register(Nfe)
class NfeAdmin(admin.ModelAdmin):
    list_display = ('id', 'emitente', 'mod', 'serie', 'numero', 'data', 'q_item', 'v_total')
    search_fields = ('numero',)

@admin.register(NfProduto)
class NfProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nf', 'produto', 'descricao', 'quantidade', 'v_unitario', 'v_bruto_total', 'v_total_tributo', 'flag_total')


@admin.register(NfPagamento)
class NfPagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nf', 'f_pagamento', 'valor',)
