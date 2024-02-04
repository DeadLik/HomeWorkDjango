from django.urls import path

from onlineshop.views import customers, products, orders, \
    order_products, customer_orders, product_by_id, customer_products, index

urlpatterns = [
    path('', index, name='index'),
    path('customers/', customers, name='customers'),
    path('products/', products, name='products'),
    path('orders/', orders, name='orders'),
    path('customers/<int:customer_id>', customer_orders, name='customer_orders'),
    path('customers/<int:customer_id>/<int:period>/', customer_products, name='customer_products'),
    path('products/<int:product_id>', product_by_id, name='product_by_id'),
    path('orders/<int:order_id>', order_products, name='order_products'),
]
