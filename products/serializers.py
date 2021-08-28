from rest_framework import serializers
from products.models import Product, Tag, Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title description price'.split()


# class ProductCreateSerializer(serializers.Serializer):
#     title = serializers.CharField(min_length=3, max_length=100)
#     description = serializers.CharField(max_length=1000)
#     price = serializers.FloatField()
#     category_id = serializers.IntegerField()
#     tags = serializers.ListField(child=serializers.IntegerField())


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'title review'.split()