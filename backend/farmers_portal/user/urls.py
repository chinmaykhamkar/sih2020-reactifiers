from django.urls import path
from . import views

urlpatterns = [
    path('add_customer/',views.add_customer),
    path('add_farmer/',views.add_farmer),
    # path('login/', obtain_auth_token)
]
