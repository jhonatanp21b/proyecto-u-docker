from django.db import models

class Category(models.Model):
  code = models.CharField(max_length=6, unique=True)
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'categories'
