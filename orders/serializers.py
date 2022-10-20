
from .models import Order
from rest_framework import serializers


class OrderCreationSerializer(serializers.ModelSerializer):
    
    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()
    
    class Meta:
        model = Order
        fields = ['size', 'order_status', 'quantity']
        

class OrderDetailSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField(default='PENDING')
    quantity = serializers.IntegerField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    
    class Meta:
        model = Order
        fields = ['size', 'order_status', 'quantity', 'created', 'updated']
    
    
    
        
        