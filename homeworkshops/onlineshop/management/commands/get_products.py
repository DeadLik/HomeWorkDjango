from django.core.management.base import BaseCommand
from onlineshop.models import ProductModel


class Command(BaseCommand):
    help = "Get product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = ProductModel.objects.filter(pk=pk).first()
        self.stdout.write(f'{product}')
