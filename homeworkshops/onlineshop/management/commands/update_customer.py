from django.core.management.base import BaseCommand
from onlineshop.models import CustomerModel


class Command(BaseCommand):
    help = "Update customer by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer ID')
        parser.add_argument('name', type=str, help='Customer name')
        parser.add_argument('email', type=str, help='Customer email')
        parser.add_argument('phone', type=int, help='Customer phone')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        customer = CustomerModel.objects.filter(pk=pk).first()
        customer.name = name
        customer.email = email
        customer.phone = phone
        customer.save()
        self.stdout.write(f'{customer}')