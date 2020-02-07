from django.contrib import admin
from .models import Customer, Farmer, MyUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(MyUser, UserAdmin)
admin.site.register(Customer)
admin.site.register(Farmer)
# admin.site.register(MyUser)