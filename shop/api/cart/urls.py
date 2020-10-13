from django.urls import path, include
from rest_framework import routers
from .views import CartView, CartListView

app_name = 'cart'
router = routers.DefaultRouter()
router.register('cart', CartView, basename='cart')
router.register('cartlist', CartListView, basename='cart')


urlpatterns = [
   path('', include(router.urls)),
   #path('/<int:id>/', include(router.urls)),
]

