from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import *



class HelloAuthView(generics.GenericAPIView):
    def get(self, requets):
        return Response(data={"message": "Hello Auth"}, status=status.HTTP_200_OK)
    
    
class UserCreateView(generics.GenericAPIView):
    
    serializer_class = UserCreationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
