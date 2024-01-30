from django.core.management.base import BaseCommand
from onlineshop.models import CustomerModel


class Command(BaseCommand):
    help = "Delete customer by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = CustomerModel.objects.filter(pk=pk).first()
        if customer is not None:
            customer.delete()
            self.stdout.write(f'Пользователь "{customer}" успешно удалён.')
        else:
            self.stdout.write('Данного пользователя нет в БД')
