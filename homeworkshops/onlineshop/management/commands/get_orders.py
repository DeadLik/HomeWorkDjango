from django.core.management.base import BaseCommand
from onlineshop.models import OrderModel


class Command(BaseCommand):
    help = "Get order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = OrderModel.objects.filter(pk=pk).first()
        self.stdout.write(f'{order}')
