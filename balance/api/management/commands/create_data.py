from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from ...models import Transaction, create_transfer


class Command(BaseCommand):
    """
    Setup example data for the API
    """

    help = 'Generate example data for the API.'

    def handle(self, *args, **options):
        self.stdout.write('Creating example data...')
        self._create_transactions()

    def _create_transactions(self):
        """
        Create example transactions.
        """
        foo, bar = self._create_users()
        Transaction.create_deposit(user=foo, amount=10000, currency='EUR')
        Transaction.create_deposit(user=bar, amount=15000, currency='EUR')
        create_transfer(user_from=foo, user_to=bar, amount=5000, currency='EUR')
        Transaction.create_withdrawal(user=bar, amount=10000, currency='EUR')
        self.stdout.write('Created example transactions')

    def _create_users(self):
        """
        Create example users
        """
        foo, created = User.objects.get_or_create(username='foo', first_name='Foo', last_name='Balance',
                                                  email='foo@test.com')
        if created:
            self.stdout.write(f'Created new user: {foo}')
        bar, created = User.objects.get_or_create(username='bar', first_name='Bar', last_name='Balance',
                                                  email='bar@test.com')
        if created:
            self.stdout.write(f'Created new user: {bar}')
        return foo, bar
