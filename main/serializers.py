from rest_framework import serializers
from .models import *

class MyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPhoto
        fields = ('id', 'title', 'image')