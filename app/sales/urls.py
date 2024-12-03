from django.urls import path
from .views import categoriesView, productsView

urlpatterns = [
  path('categories/', categoriesView.CategoriesViewSet.as_view()),
  path('products/', productsView.ProductsViewSet.as_view(), name="products"),
]