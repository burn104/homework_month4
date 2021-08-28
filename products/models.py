from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               blank=True, null=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    review = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name= 'Prod')

    def __str__(self):
        return self.text