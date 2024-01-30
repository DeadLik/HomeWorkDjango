from django.core.management.base import BaseCommand
from onlineshop.models import OrderModel


class Command(BaseCommand):
    help = "Get all orders."

    def handle(self, *args, **kwargs):
        orders = OrderModel.objects.all()
        for i in orders:
            self.stdout.write(f'{i}')
