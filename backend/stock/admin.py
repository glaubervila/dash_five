from django.contrib import admin

from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'unidade',)
    search_fields = ('descricao',)