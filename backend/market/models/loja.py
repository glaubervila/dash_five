from django.db import models
from common.models import Country, State, City

class Loja(models.Model):

    cnpj = models.CharField(
        max_length=14, 
        verbose_name='CNPJ',
    )

    inscricao_estatual = models.CharField(
        max_length=14, 
        verbose_name='Inscricao Estadual',
    )

    nome = models.CharField(
        max_length=60,
        verbose_name='Razao Social ou Nome'
    )

    nome_fantasia = models.CharField(
        max_length=60,
        verbose_name='Nome fantasia',
        null=True, blank=True
    )

    pais = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE, 
        verbose_name='Pais'
    )

    estado = models.ForeignKey(
        State, 
        on_delete=models.CASCADE, 
        verbose_name='Estado'
    )

    cidade = models.ForeignKey(
        City, 
        on_delete=models.CASCADE, 
        verbose_name='Cidade'
    )

    # TODO: municipio
    bairro = models.CharField(
        max_length=60,
        verbose_name='Bairro',
    )

    logradouro = models.CharField(
        max_length=60,
        verbose_name='Logradouro'
    )

    numero = models.CharField(
        max_length=60,
        verbose_name='Numero'
    )

    complemento = models.CharField(
        max_length=60, 
        verbose_name='Complemento',
        null=True, blank=True
    )

    cep = models.CharField(
        max_length=8, 
        verbose_name='CEP',
    )

    telefone = models.CharField(
        max_length=16, 
        verbose_name='Telefone',
        null=True, blank=True
    )

    crt = models.CharField(
        max_length=1, 
        verbose_name='Código de Regime Tributário',
        choices=(('1', 'Simples Nacional'), ('2', 'Simples Nacional, excesso sublimite de receita bruta'), ('3', 'Regime Normal') )
    )

    def __str__(self):
        return self.nome

# class Checkout(models.Model):

#     store = models.ForeignKey(
#         Store, 
#         on_delete=models.CASCADE, 
#         verbose_name='Store'
#     )

#     number = models.PositiveIntegerField(
#         verbose_name='Number'
#     )


#     def __str__(self):
#         return "%s - Checkout %s" % (self.store.name, str(self.number))