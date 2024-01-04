from django.db import models
from django.contrib.auth.models import User


class ShoppingCart(models.Model):



    item_name = models.CharField(max_length=100)
    item_quantity  = models.IntegerField()
    cart_total = models.IntegerField()


class Pizza(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    image_url = models.CharField(max_length=200,default='')







class Order(models.Model):
    order_id = models.AutoField(unique=True, primary_key=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, default=None)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    order_items = models.CharField(max_length = 10000)
    order_amount = models.IntegerField()
    street = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zipcode = models.CharField(max_length = 6)
    phone_number = models.CharField(max_length = 999999)
    
    
    
    def __str__(self):
        
        return f"Order number :{self.order_id} by {self.first_name} {self.last_name} "