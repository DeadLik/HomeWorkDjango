from django.core.management.base import BaseCommand
from onlineshop.models import CustomerModel


class Command(BaseCommand):
    help = "Get all customers."

    def handle(self, *args, **kwargs):
        customers = CustomerModel.objects.all()
        for i in customers:
            self.stdout.write(f'{i}')
