from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from ..serializers import CategorySerializer
from ..models import Category

class CategoriesViewSet(APIView):

  def get(self, request):
    queryset = Category.objects.all()

    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = CategorySerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)
  
  def post(self, request):
    category = CategorySerializer(data=request.data)

    if category.is_valid():
      category.save()
      return Response(category.data, status=status.HTTP_201_CREATED)
    
    return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)