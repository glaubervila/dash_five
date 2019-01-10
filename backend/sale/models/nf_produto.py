from django.db import models

from sale.models import Nfe
from stock.models import Produto

class NfProduto(models.Model):

    nf = models.ForeignKey   (
        Nfe, 
        on_delete=models.CASCADE,
        verbose_name='Nota Fiscal'
    )

    produto = models.ForeignKey   (
        Produto, 
        on_delete=models.CASCADE,
        verbose_name='Produto'
    )

    ean = models.CharField(
        verbose_name='EAN',
        help_text='GTIN (Global Trade Item Number) do produto',
        max_length=14,
        null=True, blank=True
    )

    descricao = models.CharField(
        verbose_name='Descrição',
        help_text='Descrição do produto',
        max_length=120,
    )

    ncm = models.CharField(
        verbose_name='NCM',
        help_text='Código NCM',
        max_length=8,
        default='00',
    )

    cfop = models.CharField(
        verbose_name='CFOP',
        help_text='Código Fiscal de Operações e Prestações',
        max_length=4,
    )

    unidade = models.CharField(
        verbose_name='Unidade',
        help_text='Unidade Comercial',
        max_length=6,
    )

    quantidade = models.FloatField(
        verbose_name='Quantidade',
        help_text='Quantidade Comercial',
        default=0
    )

    v_unitario = models.FloatField(
        verbose_name='Valor Unitário',
        help_text='Valor Unitário de Comercialização',
        default=0
    )

    v_bruto_total = models.FloatField(
        verbose_name='Total Bruto',
        help_text='Valor Total Bruto dos Produtos',
        default=0
    )

    u_tributavel = models.CharField(
        verbose_name='Unidade Tributável',
        # help_text='Unidade Tributável',
        max_length=6,
        null=True, blank=True
    )
    
    q_tributavel = models.FloatField(
        verbose_name='Quantidade Tributável',
        default=0
    )

    v_unit_tributacao = models.FloatField(
        verbose_name='Tributação',
        help_text='Valor Unitário de tributação',
        default=0
    )

    flag_total = models.CharField(
        verbose_name='Modelo',
        help_text='Indica se valor do Item entra no valor total da NF-e',
        max_length=1,
        choices=(
            ('0', '0 - Valor do item não compõe o valor total da NF-e'), 
            ('1', '1 - Valor do item compõe o valor total da NF-e')
        )
    )

    