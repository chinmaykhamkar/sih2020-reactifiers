from django.contrib import admin
from .models import Customer, Farmer, MyUser

admin.site.register(Customer)
admin.site.register(Farmer)
admin.site.register(MyUser)