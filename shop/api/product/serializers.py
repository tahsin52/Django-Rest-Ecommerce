from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    price = serializers.DecimalField(decimal_places=2, max_digits=20)
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'active', 'image']
        read_only_fields = ['id', 'title', 'description', 'price', 'active', 'image']
