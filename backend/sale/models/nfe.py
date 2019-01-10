from django.db import models

from market.models import Loja

class Nfe(models.Model):

    emitente = models.ForeignKey   (
        Loja, 
        on_delete=models.CASCADE,
        verbose_name='Emitente'
    )

    mod = models.CharField(
        verbose_name='Modelo',
        help_text='Código do Modelo',
        max_length=2,
        choices=(('55', '55 - NF-e'), ('65', '65 - NFC-e'))
    )

    serie = models.CharField(
        verbose_name='Série',
        help_text='Série do Documento Fiscal',
        max_length=3,
    )

    numero = models.CharField(
        verbose_name='Número',
        help_text='Número do Documento Fiscal',
        max_length=9,
    )

    data = models.DateTimeField(
        verbose_name='Data Emissão',
        help_text='Data e hora de emissão do Documento Fiscal',
        auto_now=False
    )

    tp_operacao = models.CharField(
        verbose_name='Operação',
        help_text='Tipo de Operação',
        max_length=1,
        choices=(
            ('0', '0 - Entrada'), 
            ('1', '1 - Saída')
        )
    )

    id_destino = models.CharField(
        verbose_name='Destino',
        help_text='Identificador de local de destino da operação',
        max_length=1,
        choices=(
            ('1', '1 - Operação interna'),
            ('2', '2 - Operação interestadual'),
            ('3', '3 - Operação com exterior')
        )
    )

    tp_emissao = models.CharField(
        verbose_name='Tipo de Emissão',
        help_text='Tipo de Emissão da NF-e',
        max_length=1,
        choices=(
            ('1', '1 - Emissão normal'),
            ('2', '2 - Contingência FS-IA'),
            ('3', '3 - Contingência SCAN'),
            ('4', '4 - Contingência DPEC'),
            ('5', '5 - Contingência FS-DA'),
            ('6', '6 - Contingência SVC-AN'),
            ('7', '7 - Contingência SVC-RS'),
            ('9', '7 - Contingência off-line da NFC-e'),
        )
    )

    chave_acesso = models.CharField(
        verbose_name='Chave de Acesso',
        help_text='Código Numérico que compõe a Chave de Acesso',
        max_length=8
    )

    chave_acesso_dv = models.CharField(
        verbose_name='DV Chave de Acesso',
        help_text='Dígito Verificador da Chave de Acesso da NF-e',
        max_length=1
    )

    n_item = models.PositiveIntegerField(
        verbose_name = "Items",
        help_text='Quantidade de Items',
        default=0
    )

    v_total = models.DecimalField(
        verbose_name='Valor Total',
        help_text='Valor Total da NF-e',
        max_digits=15,
        decimal_places=3,
        default=0
    )

    v_total_tributo = models.FloatField(
        verbose_name='Total de Tributos',
        help_text='Valor aproximado total de tributos federais, estaduais e municipais.',
        # max_digits=15,
        # decimal_places=3,
        default=0
    )

    v_total_desconto = models.FloatField(
        verbose_name='Total de Descontos',
        help_text='Valor Total do Desconto',
        # max_digits=15,
        # decimal_places=3,
        default=0
    )



# class Payment(models.Model):

#     ticket = models.ForeignKey(
#         Ticket,
#         on_delete=models.CASCADE,
#         verbose_name='Ticket'
#     )

#     option = models.CharField(
#         verbose_name='Option',
#         max_length=128,
#     )

#     value = models.DecimalField(
#         verbose_name='Value',
#         max_digits=15,
#         decimal_places=3
#     )

#     date_time = models.DateTimeField(
#         verbose_name='Date Time',
#         auto_now=False
#     )

#     is_canceled = models.BooleanField(
#         verbose_name='Canceled',
#         default=False
#     )
