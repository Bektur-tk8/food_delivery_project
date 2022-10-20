from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Order
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404




class HelloOrderView(generics.GenericAPIView):
    def get(self, requets):
        return Response(data={"message": "Hello Orders"}, status=status.HTTP_200_OK)
    

class OrderCreateListView(generics.GenericAPIView):
    
    serializer_class = serializers.OrderCreationSerializer
    queryset = Order.objects.all()
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
    


class OrderDetailView(generics.GenericAPIView):
    
    serializer_class = serializers.OrderDetailSerializer
    
    # def get_object(self, pk):
    #     try:
    #         return Order.objects.get(pk=pk)
    #     except Order.DoesNotExist:
    #         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    
    def get(self, request, pk):
        # order = self.get_object(pk)
        order = get_object_or_404(Order, pk=pk)
        serializer = self.serializer_class(order)
        return Response(serializer.data, status = status.HTTP_200_OK)
        

    def put(self, request, pk):
        # order = self.get_object(pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        pass
