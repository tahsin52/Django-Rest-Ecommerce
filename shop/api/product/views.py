from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .pagination import ProductPagination
from rest_framework.permissions import IsAuthenticated


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination
    permission_classes = (IsAuthenticated,)
