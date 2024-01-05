from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ShoppingCart(models.Model):



    item_name = models.CharField(max_length=100)
    item_quantity  = models.IntegerField()
    cart_total = models.IntegerField()


class Pizza(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    image_url = models.CharField(max_length=200,default='')
    
    
    def __str__(self):
        return self.name







class Order(models.Model):  
    order_id = models.CharField(default=  None, unique = True, max_length = 400,blank=True,null = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, default=None,null = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    order_items = models.CharField(max_length = 10000)
    order_amount = models.IntegerField()
    street = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zipcode = models.CharField(max_length = 6)
    phone_number = models.CharField(max_length = 999999)
    paid =models.BooleanField(default = False)
    date_of_order = models.DateTimeField(default= timezone.now)
    
    # related to razorpay
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)
    
    
    
    def __str__(self):
        
        return f"Order number :{self.order_id} by {self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if self.order_id is None and self.date_of_order and self.id:
            self.order_id = self.date_of_order.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)