from django.db import models
from user.models import Farmer, Customer 

class Crop(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField()
    farmer = models.ForeignKey(Farmer,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
