from django.db import models

from .api.product.models import Product
from .api.user.models import Profile,User
from .api.cart.models import Cart
from .api.order.models import Order, OrderItem