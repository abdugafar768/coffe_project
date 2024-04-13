from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    phone = models.CharField(max_length=30)


    def __str__(self):
        return self.username

class Category(models.Model):
    image = models.ImageField(upload_to='product_photos/', null=True, blank=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_photos/', null=True, blank=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Basket(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    address = models.TextField()

    def total_price(self):
        return self.product.price * self.quantity


class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    address = models.TextField()

    def total_price(self):
        return self.product.price * self.quantity

