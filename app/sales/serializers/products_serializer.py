from rest_framework.serializers import ModelSerializer
from ..models.products import Product

class ProductSerializer(ModelSerializer):
  class Meta:
    model = Product
    fields = ['id', 'name', 'description', 'price', 'category']
    readonly = ['created_at', 'updated_at']
    