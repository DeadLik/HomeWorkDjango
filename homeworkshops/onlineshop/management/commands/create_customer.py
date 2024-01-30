from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from onlineshop.models import CustomerModel
from random import randint


class Command(BaseCommand):
    help = 'Creates 5 user records.'

    def handle(self, *args, **kwargs):
        for i in range(0, 10):
            customer = CustomerModel(name=f'Пользователь{i}',
                                     email=f'costumer{i}@nam.ru',
                                     phone=randint(1000_0000_000, 9999_9999_999),
                                     address=lorem_ipsum.paragraph(),
                                     )
            customer.save()
            self.stdout.write(f'Пользователь {i} успешно добавлен')
