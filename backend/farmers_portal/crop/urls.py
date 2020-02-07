from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.CropListView),
    path('detail/<int:pk>/',views.CropDetail),
]
