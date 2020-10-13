from django.db import models
from ..user.models import User
from ..product.models import Product




class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product)

    @property
    def amount(self):
        return self.quantity * self.product.price

