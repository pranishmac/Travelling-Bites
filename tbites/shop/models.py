from django.db import models
import datetime
from django.contrib.auth.models import User  
from django.forms import ModelForm  




# Create your models here.
class item(models.Model):
    item_id = models.AutoField
    item_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.item_name
    
    @staticmethod
    def get_products_by_id(ids):
        return item.objects.filter(id__in = ids)
    
class order(models.Model):
    item = models.ForeignKey('item',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    username = models.CharField(max_length=50, default='', blank=True)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(username):
        return order.objects.filter(username=username).order_by('-date')
