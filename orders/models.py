from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.

ORDER_SIZE = (
    ('L', 'Large'),
    ('S', 'Small')
)


class Topping(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Pizza(models.Model):
    style = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=1, choices=ORDER_SIZE, default='S')
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f"{self.size} size {self.style} pizza. Price({self.price})"


class Extra(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Extra {self.name} costs {self.price}"


class Sub(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=1, choices=ORDER_SIZE, default='S')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    extras = models.ManyToManyField(Extra, blank=True)

    def __str__(self):
        return f"{self.size} size {self.name} sub. Price({self.price})"


class Pasta(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} Pasta. Price({self.price})"


class Salad(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} Salad. Price({self.price})"


class DinnerPlatter(models.Model):
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=1, choices=ORDER_SIZE, default='S')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.size} size {self.name} dinner platter. Price({self.price})"


class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user}:  Order Item: {self.order}  Price : {self.price}"


class OrderItem(models.Model):
    item = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Item: {self.item}. Price:{self.price}"


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ManyToManyField(OrderItem, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    orderedTime = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.user}:  Order Items: {self.order.in_bulk()}"
