from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Crop
from .serializers import CropSerializer, CropSerializerLoc

@api_view(["GET","POST"])
def CropListView(request):

    if request.method == "GET":
        crops = Crop.objects.all()
        data = []
        for i in crops:
            data.append({'name': i.name, 'quantity': i.quantity, 'price': i.price, 'image': i.image, 'farmer': i.farmer, 'state': i.farmer.state, 'district': i.farmer.district})
        serializer = CropSerializerLoc(data,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = CropSerializer(data= request.data)
        if serializer.is_valid():
            print("HERE")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(["GET","DELETE","PUT"])
def CropDetail(request,pk):
    try:
        crop = Crop.objects.get(pk=pk)
    except Crop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = {'name': crop.name, 'quantity': crop.quantity, 'price': crop.price, 'image': crop.image, 'farmer': crop.farmer, 'state': crop.farmer.state, 'district': crop.farmer.district}
        serializer = CropSerializerLoc(data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CropSerializer(crop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        crop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)