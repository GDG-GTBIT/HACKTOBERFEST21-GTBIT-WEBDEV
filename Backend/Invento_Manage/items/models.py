from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
   
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    product_id = models.CharField(max_length=50)
    quantity = models.IntegerField()
    category = models.CharField(max_length=20,default = 'null')

    def __str__(self):
        return self.product_id

    
class Inventory_User(models.Model):
    phone_num = models.CharField(max_length=11, unique=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.phone_num


