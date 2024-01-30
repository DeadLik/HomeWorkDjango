from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from onlineshop.models import OrderModel, CustomerModel
from random import choice


class Command(BaseCommand):
    help = 'Creates 5 order records.'

    def handle(self, *args, **kwargs):
        customer = CustomerModel.objects.all()
        for i in range(0, 10):
            order = OrderModel(customer=choice(customer),
                               total_price=0)
            order.save()
            self.stdout.write(f'Заказ {i} успешно добавлен')
