from django.db import models

# Create your models here.


class ShoppingCart(models.Model):



    item_name = models.CharField(max_length=100)
    item_quantity  = models.IntegerField()
    cart_total = models.IntegerField()


class Pizza(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    image_url = models.CharField(max_length=200,default='')

