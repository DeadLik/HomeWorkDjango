from django.db import models


class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(blank=False)
    address = models.TextField()
    publication_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Имя пользователя: {self.name} '
                f'email: {self.email} '
                f'номер телефона: {self.phone}')


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=0)
    publication_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Название товара: {self.title} '
                f'цена: {self.price} '
                f'количество на складе: {self.amount}шт')


class OrderModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    publication_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.name}: {list(map(str, self.products.all()))} = {self.total_price}'
