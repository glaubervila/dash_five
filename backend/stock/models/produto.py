from django.db import models


class Produto(models.Model):

    codigo = models.CharField(
        verbose_name='Código Interno',
        max_length=60,
        default=0
    )

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

    def __str__(self):
        return self.codigo