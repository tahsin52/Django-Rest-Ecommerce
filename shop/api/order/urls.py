from django.urls import path, include
from rest_framework import routers
from .views import OrderView, OrderItemView, OrderCreateView

app_name = 'order'
router = routers.DefaultRouter()
router.register('order', OrderView,basename='order')
router.register('orderitem', OrderItemView,basename='orderitem')
router.register('ordercreate', OrderCreateView,basename='ordercreate')

urlpatterns = [
   path('', include(router.urls)),
]

