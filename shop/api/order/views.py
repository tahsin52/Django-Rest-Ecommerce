from django.shortcuts import render
from .models import Order, OrderItem
from ..cart.models import Cart
from .serializers import OrderSerializer, OrderCreateSerializer, OrderItemSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from ..user import permissions
from .pagination import OrderPagination


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = (permissions.PostOwnProfile, IsAuthenticated,)
    serializer_class = OrderSerializer
    pagination_class = OrderPagination

    #authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

    def post(self, request):

        user = request.user
        carts = Cart.objects.filter(user=user)
        carttotal = 0

        for cart in carts:
            carttotal += cart.quantity * cart.product.price
            return carttotal
        serializer = OrderItemSerializer(data=request.data)

        if serializer.is_valid():
            order = Order()
            order.name = serializer.data['name']
            order.street = serializer.data['street']
            order.city = serializer.data['city']
            order.state = serializer.data['state']
            order.zipcode = serializer.data['zipcode']
            order.phone = serializer.data['phone']
            order.user = user
            order.total = carttotal
            order.save()

            for cart in carts:
                item = OrderItem()
                item.order_id = order.id
                item.product_id = cart.product_id
                item.user = user
                item.quantity = cart.quantity
                item.price = cart.product.price
                item.total = cart.amount
                item.save()
            Cart.objects.filter(user=user).delete()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.PostOwnProfile,)
    serializer_class = OrderItemSerializer


    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.filter(user=user.id)

class OrderCreateView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.PostOwnProfile,)
    serializer_class = OrderSerializer
