from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from onlineshop.models import ProductModel
from random import randint
from math import pi


class Command(BaseCommand):
    help = 'Creates 5 product records.'

    def handle(self, *args, **kwargs):
        for i in range(0, 10):
            product = ProductModel(title=f'Товар{i}',
                                   description=lorem_ipsum.paragraph(),
                                   price=randint(100, 100_000) / pi,
                                   amount=randint(1, 200))
            product.save()
            self.stdout.write(f'Товар {i} успешно добавлен')
