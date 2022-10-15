from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response



class HelloAuthView(generics.GenericAPIView):
    def get(self, requets):
        return Response(data={"message": "Hello Auth"}, status=status.HTTP_200_OK)
