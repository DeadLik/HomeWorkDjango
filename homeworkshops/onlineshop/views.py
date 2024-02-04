import logging

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from onlineshop.models import Customer, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'{request} request received')
    return render(request, 'onlineshop/onlineshop.html')


def customers(request):
    logger.info(f'{request} request received')
    customers = Customer.objects.all()
    context = {'title': 'Customers',
               'name': 'customer_orders',
               'items': customers}
    return render(request, 'onlineshop/items.html', context)


def products(request):
    logger.info(f'{request} request received')
    products = Product.objects.all()
    context = {'title': 'Products',
               'name': 'product_by_id',
               'items': products}
    return render(request, 'onlineshop/items.html', context)


def orders(request):
    logger.info(f'{request} request received')
    orders = Order.objects.all()
    context = {'title': 'Orders',
               'name': 'order_products',
               'items': orders}
    return render(request, 'onlineshop/items.html', context)


def order_products(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    products = Product.objects.filter(order=order).all()
    context = {'title': order.id,
               'list': 'Order',
               'items': products,
               'name': 'product_by_id'}
    return render(request, 'onlineshop/item_by_id.html', context)


def customer_orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).all()
    context = {'title': customer.id,
               'list': 'Customer',
               'items': orders,
               'name': 'order_products'}
    return render(request, 'onlineshop/item_by_id.html', context)


def product_by_id(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'title': product.id,
               'list': 'Product',
               'product': product}
    return render(request, 'onlineshop/product_by_id.html', context)


def customer_products(request, customer_id, period):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer,
                                  date_ordered__gt=(timezone.now() - timezone.timedelta(days=period))).all()
    products = [product for order in orders for product in order.products.all()]
    context = {'title': customer.id,
               'list': 'Customer',
               'items': products,
               'name': 'order_products',
               'period': period}
    return render(request, 'onlineshop/item_by_id.html', context)
