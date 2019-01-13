from django.core.management.base import BaseCommand, CommandError
from stock.models import Produto
import humanize
from datetime import datetime
from django.db.models import Max
from django.conf import settings
import os
import pandas as pd 

class Command(BaseCommand):
    help = 'Importa Produtos a partir de um csv.'

    def add_arguments(self, parser):

        # Arquivo csv
        parser.add_argument('filename', type=str, help='Caminho para o arquivo csv com os produtos')

        # Apaga todos os produtos antes de inserir
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Remove todos os produtos antes de inserir',
        )


    def delete(self):

        self.stdout.write("Removido %s produtos " % Produto.objects.count())    
        
        for x in Produto.objects.all().iterator():
            x.delete()

    def load_produtos(self, filepath):


        data = pd.read_csv(filepath, delimiter=';') 

        data.sort_values('CODIGO')

        # List Headers
        # data.head():

        for row in data.itertuples():
            try:
                prod, created = Produto.objects.update_or_create(
                    codigo=row.CODIGO, 
                    defaults={
                        'descricao': row.PRODUTO,
                        'unidade': row.UNIDADE
                    }
                )

                self.stdout.write("Created: [ %s ]  - %s - %s" % (created, row.CODIGO, row.PRODUTO) )    
            except:
                self.stdout.write("Failed: %s - %s" % (row.CODIGO, row.PRODUTO) )    

    def handle(self, *args, **options):

        if options['delete']:
            self.stdout.write("Removendo todos os produtos")    
            self.delete()

        filename = options['filename']

        filepath = os.path.join(settings.MEDIA_TMP_DIR, filename)

        t0 = datetime.now()

        if os.path.exists(filepath):
            self.load_produtos(filepath)    
        else:
            self.stdout.write("Arquivo nao encontrado:  %s " % filepath)       

        

        t1 = datetime.now()
        tdelta = t1 - t0

        self.stdout.write("Duracao %s " % humanize.naturaldelta(tdelta))    

        self.stdout.write("Produtos:  %s " % Produto.objects.count())    




