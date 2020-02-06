from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyUser, Customer, Farmer
from .serializers import FarmerSerializer, UserSerializer, CustomerSerializer

@api_view(["POST"])
def add_customer(request):

    if request.method == 'POST':
        serializer = UserSerializer(data={"username" : request.data["username"], "password": request.data["password"],"is_customer":"True"})
        if serializer.is_valid():
            serializer.save()
            ser_customer = CustomerSerializer(data = {"user":serializer.data['id'], "phone_number": request.data["phone_number"]})
            if ser_customer.is_valid():
                ser_customer.save()
                return Response(ser_customer.data)
            return Response(ser_customer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def add_farmer(request):

    if request.method == 'POST':
        serializer = UserSerializer(data={"username" : request.data["username"], "password": request.data["password"],"is_farmer":"True"})
        if serializer.is_valid():
            serializer.save()
            ser_farmer = FarmerSerializer(data = {"user":serializer.data['id'],"state": request.data["state"], "district": request.data["district"], "phone_number": request.data["phone_number"]})
            if ser_farmer.is_valid():
                ser_farmer.save()
                return Response(ser_farmer.data)
            return Response(ser_farmer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)