from django.core.management.base import BaseCommand
from onlineshop.models import ProductModel


class Command(BaseCommand):
    help = "Delete product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = ProductModel.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
            self.stdout.write(f'Товар "{product}" успешно удалён.')
        else:
            self.stdout.write('Данного товара нет в БД')
