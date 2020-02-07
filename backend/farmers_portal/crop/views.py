from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Crop
from .serializers import CropSerializer

# @api_view(["GET"])
# def CropListView(request):

#     if request.method == "GET":
#         crops = Crop.objects.all()
#         serializer = CropSerializer(crops,many=True)
#         return Response(serializer.data)
    
#     elif request.method == "POST":
#         serializer = CropSerializer(data= requesyt.data)

#         if serializer.is_valid():
#             serializer.save()


# def Crop