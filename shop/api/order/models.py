from django.db import models
from datetime import datetime
from ..user.models import User, Adress
from ..product.models import Product
from django.db.models.signals import post_save

from ..product.models import Product


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    total = models.FloatField()
    note = models.TextField()
    status = models.CharField(choices=STATUS, default='New', max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.FloatField()
    price = models.FloatField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product)

# TOTALİ BİR FONKSİYON YAZIP QUANTİTY VE PRİCE İLE ÇARPIP GÖSTEREBİLİRİZ ?
