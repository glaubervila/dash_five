from django.core.management.base import BaseCommand, CommandError
from market.models import Store, Checkout
from sale.models import Ticket, Payment
from faker import Faker
import random
from datetime import datetime
import pytz
import pandas as pd
import humanize
from django.db.models import Max
class Command(BaseCommand):
    help = 'Creates fakes Sales and Payments.'

    def add_arguments(self, parser):
        # Intervalo par gerar as vendas
        parser.add_argument('start', type=str, help='Initial sales date in this format YYYY-MM-DD')
        parser.add_argument('end', type=str, help='Final sales date in this format YYYY-MM-DD')

        # Apaga todas as vendas antes de inserir as novas
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Delete all tickets before creating new ones',
        )

        # Quantidade maxima de Vendas por dia
        parser.add_argument(
            '--max_ticket', action='store_true', dest='max_ticket',  default=100, help='Maximum number of tickets per day. default value is 100',)
        
        # Valor Minimo de Venda
        parser.add_argument(
            '--min_amount', action='store_true', dest='min_amount',  default=1, help='Minimum amount of sales. default value is 1',)

        # Valor Maximo de Venda
        parser.add_argument(
            '--max_amount', action='store_true', dest='max_amount',  default=2000, help='Maximum amount of sales. default value is 2000',)

        # Percentual de um cupom ter sido cancelado
        parser.add_argument(
            '--cancel', action='store_true', dest='cancel',  default=8, help='Chance of a ticket being canceled, value must be integer between 0 and 100, the default value is 8.',)

        # Percentual de um cupom receber desconto
        parser.add_argument(
            '--discount', action='store_true', dest='discount',  default=30, help='Percentage chance of applying discount. must be an integer between 0 and 100 the default is 30.',)

        # Percentual Minimo de Desconto
        parser.add_argument(
            '--discount_min', action='store_true', dest='discount_min',  default=3, help='Minimum discount percentage, must be integer between 0 and 100, default 3.',)

        # Percentual Maximo de Desconto
        parser.add_argument(
            '--discount_max', action='store_true', dest='discount_max',  default=10, help='Maximun discount percentage, must be integer between 0 and 100, default 10',)



    def delete(self):

        self.stdout.write("Removing %s sales" % Ticket.objects.count())    
        
        for x in Ticket.objects.all().iterator():
            x.delete()


    def create_tickets(self, start, end, options):

        # lista com todas as Lojas
        stores = Store.objects.all()

        # Intervalo de datas
        daterange = pd.date_range(start, end)

        # numero do ultimo ticket
        number = Ticket.objects.all().aggregate(Max('number'))['number__max'] 
        if not number:
            number = 1
        else:
            number +=1

        print("Max Ticket: %s" % number)

        # Para cada data cria uma serie ramdomica de vendas
        for dt in daterange:

            # Para cada dia escolher um limit aleatoria de tickets até o limit passado por parametro. 
            qtd_tickets = random.randint(0, options['max_ticket'])
            # Criacao do ticket
            for i in range(qtd_tickets):
                
                # Convert dates do UTC to prevent Django warning
                date = datetime(dt.year, dt.month, dt.day, tzinfo=pytz.UTC)
                st = self.random_time(dt, 8, 23)
                start_time = datetime(st.year, st.month, st.day, st.hour, st.minute, st.second, tzinfo=pytz.UTC)

                # Loja
                store = random.choice(stores)
                # Escolhe um checkout aleatorio da loja.
                checkout = random.choice(store.checkout_set.all())

                # Amount, gera um valor aletorio baseado no valor minimo e maximo passado por parametro.
                amount = self.random_amount(options['min_amount'], options['max_amount'])

                # canceled, Calcula um percentual de chance do ticket ter sido cancelado.
                is_canceled = self.percentage_chance(options['cancel'])

                # Discount, se o ticket nao for cancelado tem a chance de aplicar um desconto.
                discount = 0
                discout_percentage = None
                if not is_canceled:
                    discount, discout_percentage = self.generate_discount(amount, options)

                # Cria a Instancia do Ticket.
                ticket = Ticket()
                ticket.store = store
                ticket.checkout = checkout
                ticket.number = number
                ticket.date = date
                ticket.start_time = start_time
                ticket.amount = amount
                ticket.discount = discount
                ticket.discount_percentage = discout_percentage
                ticket.is_canceled = is_canceled

                ticket.save()

                self.create_payments(ticket, options)

                number += 1



    def random_time(self, date, min_hour, max_hour):
        """
            Generate a Random time for a date between a min and max hours
        """       
        return datetime(
            date.year, 
            date.month, 
            date.day, 
            random.randint(min_hour, max_hour), 
            random.randint(0,59), 
            random.randint(0, 59))

    def random_amount(self, min_amount, max_amount):
        """
            Gera um valor entre o minimo e o maximo, com 3 casas decimais
        """
        return float(random.randint(int(min_amount), int(max_amount)) + float("{:.3f}".format(random.random())))


    def generate_discount(self, amount, options):

        # Calcula uma chance de aplicar desconto.
        if self.percentage_chance(options['discount']):
            # Percentual de desconto randomico baseado em um percentual minimo e maximo.
            percentage = random.randint(int(options['discount_min']), int(options['discount_max']))

            discount = (amount * percentage / 100)

            return discount, percentage
        else:
            return 0, None

    def create_payments(self, ticket, options):
        """
            Cria registros da forma de pagamento usada em cada ticket.
        """
        payment_options = list([
            'Dinheiro', 'cartão débito', 'cartão acredito', 'ter pos débito', 'ter pos crédito'
        ])

        # TODO: deve permitir que um ticket possa ser pago em mais de uma forma de pagamento.
        payment_option = random.choice(payment_options)

        # Subtrair o amount do discount
        value = ticket.amount - ticket.discount

        payment = Payment()
        payment.ticket = ticket
        payment.option = payment_option
        payment.value = value
        payment.date_time = ticket.start_time
        payment.is_canceled = ticket.is_canceled

        payment.save()


    def percentage_chance(self, percentage_chance):
        """
            Calcula um percentual de chance de ser True.
            @param: float percentade_chance exemplo: 12
            tem 12% de chance de retornar True.
        """
        # TODO Rever essa formula nao parece estar retornando 
        # a porcentagem correta.
        if random.randint(0,100) < percentage_chance:
            return True
        else:
            return False


    def handle(self, *args, **options):

        if options['delete']:
            self.stdout.write("Deleting All Sales")    
            self.delete()

        start = datetime.strptime(options['start'], '%Y-%m-%d')
        end = datetime.strptime(options['end'] , '%Y-%m-%d')
        tdelta = end - start

        t0 = datetime.now()

        self.create_tickets(start, end, options)

        t1 = datetime.now()
        tdelta = t1 - t0

        self.stdout.write("Duration %s " % humanize.naturaldelta(tdelta))    

        self.stdout.write("Tickets:  %s " % Ticket.objects.count())    




