from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Product, Profile, User, Cart, Order, OrderItem

admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.unregister(Group)
