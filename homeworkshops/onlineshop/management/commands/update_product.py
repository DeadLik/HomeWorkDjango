from django.core.management.base import BaseCommand
from onlineshop.models import ProductModel


class Command(BaseCommand):
    help = "Update product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('title', type=str, help='Product title')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('amount', type=int, help='Product amount')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        title = kwargs.get('title')
        price = kwargs.get('price')
        amount = kwargs.get('amount')
        product = ProductModel.objects.filter(pk=pk).first()
        product.title = title
        product.price = price
        product.amount = amount
        product.save()
        self.stdout.write(f'{product}')
