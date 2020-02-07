from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))

class MyUser(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    
    def password_check(self,password):
        if password == self.password:
            return True
        else:
            return False


class Farmer(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE, primary_key=True)
    state = models.CharField(choices = state_choices, max_length = 50)
    district = models.CharField(max_length=50)
    phone_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.user.username + " " + str(self.user.id)

class Customer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete= models.CASCADE, primary_key=True)
    phone_number = models.IntegerField(unique=True)
    def __str__(self):
        return self.user.username + " " + str(self.user.id)
