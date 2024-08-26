from rest_framework.serializers import ModelSerializer
from ..models.categories import Category
from ..serializers.products_serializer import ProductSerializer

class CategorySerializer(ModelSerializer):
  products = ProductSerializer(many=True, read_only=True)

  class Meta:
    model = Category
    fields = ['id', 'name', 'description', 'products']
    readonly = ['created_at', 'updated_at']
    