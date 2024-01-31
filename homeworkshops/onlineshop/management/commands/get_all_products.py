from django.core.management.base import BaseCommand
from onlineshop.models import ProductModel


class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **kwargs):
        products = ProductModel.objects.all()
        for i in products:
            self.stdout.write(f'{i}')
