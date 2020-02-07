from rest_framework import serializers
from .models import Crop

class CropSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crop
        fields = "__all__"

class CropSerializerLoc(serializers.ModelSerializer):

    state = serializers.CharField(max_length = 50)
    district = serializers.CharField(max_length = 50)
    
    class Meta:
        model = Crop
        fields = "__all__"
