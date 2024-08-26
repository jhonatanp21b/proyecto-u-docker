from django.db import models
from .categories import Category

class Product(models.Model):
  code = models.CharField(max_length=6, unique=True)
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=255)
  category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
  price = models.IntegerField()
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'products'
