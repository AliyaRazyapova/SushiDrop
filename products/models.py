from django.db import models


class CategoryProduct(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    gramms = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='img/')
