from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import *
from .serializers import ProductSerializer, TagSerializer, ReviewSerializer
# Create your views here.

@api_view(['GET'])
def product_list_view(request):
    product = Product.objects.all()
    data = ProductSerializer(product, many=True).data
    return Response(data=data)

@api_view(['GET'])
def product_item_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'message': 'product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ProductSerializer(product).data

    return Response(data=data)

@api_view(['GET'])
def product_review_view(request, review):
    product = Product.objects.get(rev=review)
    data = ReviewSerializer(product).data
    return Response(data=data)

@api_view(['GET'])
def product_tag_view(request, tags):
    product = Product.objects.get(tag=tags)
    data = TagSerializer(product).data
    return Response(data=data)

@api_view(['POST'])
def product_create(request):
    if request.method == "POST":
        product = Product()
        product.title = request.POST.get("title")
        product.price = request.POST.get("price")
        product.save()
    return HttpResponseRedirect("/")

@api_view(['POST'])
def product_edit(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == 'POST':
            product.title = request.POST.get('title')
            product.price = request.POST.get('price')
            product.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, "edit.html", {"person": product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

api_view(['GET'])
def product_delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")