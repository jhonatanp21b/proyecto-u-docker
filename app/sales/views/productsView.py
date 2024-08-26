from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from ..serializers import ProductSerializer
from ..models import Product

class ProductsViewSet(APIView):

  def get(self, request):
    queryset = Product.objects.all()

    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = ProductSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)
  
  def post(self, request):
    product = ProductSerializer(data=request.data)

    if product.is_valid():
      product.save()
      return Response(product.data, status=status.HTTP_201_CREATED)
    
    return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)