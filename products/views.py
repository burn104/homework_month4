from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import *
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data=data)


def product_item_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'message': 'product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ProductSerializer(product).data

    return Response(data=data)