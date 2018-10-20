from django.core.management.base import BaseCommand, CommandError
from market.models import Store, Checkout
from common.models import Country
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Creates fakes stores and checkouts.'

    def add_arguments(self, parser):
        # Quantidade de Lojas
        parser.add_argument('stores', type=int, help='Number of stores to be created')

        # Apaga todas as lojas antes de inserir as novas
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Delete all stores before creating new ones',
        )


    def delete(self):
        for x in Store.objects.all().iterator():
            x.delete()

    def create_store(self, limit):       

        contry = Country.objects.get(initials='BR')

        states = contry.state_set.all()



        # https://faker.readthedocs.io/en/latest/locales/pt_BR.html        
        fake = Faker('pt_BR')

        id = Store.objects.count() + 1

        min_checkout = 3
        max_checkout = 20

        for index in range(int(limit)):

            state = random.choice(states)
            city = random.choice(state.city_set.all())

            store = Store()
            store.name = "Loja %s" % id 
            store.social_name  = fake.company()
            store.number = id
            store.country = contry
            store.state = state
            store.city = city
            store.adress = fake.street_address()

            store.save()

            # Create Checkouts 
            qtd_checkout = random.randrange(min_checkout, max_checkout)


            self.create_checkouts(store, qtd_checkout)

            self.stdout.write("Created %s shop with %s checkouts" % (store.name, qtd_checkout)) 

            id += 1


    def create_checkouts(self, store, limit):
        id = 1
        for index in range(int(limit)):

            checkout = Checkout()
            checkout.store = store
            checkout.number = id

            checkout.save()

            id += 1


    def handle(self, *args, **options):

        if options['delete']:
            self.stdout.write("Deleting All Stores")    
            self.delete()

        self.create_store(options['stores'])
