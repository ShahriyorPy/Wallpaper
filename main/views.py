from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import *


# Create your views here.

class PhotosListAPIView(APIView):

    def get(self, request):
        images = MyPhoto.objects.all()
        serializer = MyPhotoSerializer(images,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MyPhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoListAPIView(APIView):
    def get(self, request, pk):
        photo = MyPhoto.objects.get(id=pk)
        serializer = MyPhotoSerializer(photo)
        return Response(serializer.data)


    def delete(self, instance, pk):
        photo = MyPhoto.objects.filter(id=pk).delete()
        data = {
            "success": True,
            "xabar": "Rasm o'chirildi!"
        }
        return Response(data, status=status.HTTP_200_OK)
