from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.IntegerField()
    category = models.ForeignKey('category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name