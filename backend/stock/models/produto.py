from django.db import models


class Produto(models.Model):

    descricao = models.CharField(
        verbose_name='Descricao',
        help_text='Descricao do produto ou servico',
        max_length=120,
    )

    unidade = models.CharField(
        verbose_name='Unidade',
        help_text='Unidade Comercial',
        max_length=6,
        null=True, blank=True
    )