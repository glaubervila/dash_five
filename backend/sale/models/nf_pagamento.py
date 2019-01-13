from django.db import models

from sale.models import Nfe

class NfPagamento(models.Model):

    nf = models.ForeignKey   (
        Nfe, 
        on_delete=models.CASCADE,
        verbose_name='Nota Fiscal'
    )

    f_pagamento = models.CharField(
        verbose_name='Forma de pagamento',
        max_length=2,
        choices=(
            ('01', '01 - Dinheiro'), 
            ('02', '02 - Cheque'),
            ('03', '03 - Cartão de Crédito'),
            ('04', '04 - Cartão de Débito'),
            ('05', '05 - Crédito Loja'),
            ('10', '10 - Vale Alimentação'),
            ('11', '11 - Vale Refeição'),
            ('12', '12 - Vale Presente'),
            ('13', '13 - Vale Combustível'),
            ('99', '99 - Outros'),
        )
    )

    valor = models.FloatField(
        verbose_name='Valor do Pagamento',
        default=0
    )    