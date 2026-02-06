from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product
from products.serializers import ProductListSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for order items."""
    product_details = ProductListSerializer(source='product', read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_id', 'product_details', 'quantity', 'price_at_purchase']
        read_only_fields = ['id', 'product', 'price_at_purchase']


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for orders with simplified product selection."""
    items = OrderItemSerializer(many=True, read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    quantity = serializers.IntegerField(write_only=True, default=1)
    
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'user', 'customer_name', 
            'customer_phone', 'phone_contact', 'shipping_address', 'total_amount', 
            'status', 'created_at', 'items', 'product', 'quantity'
        ]
        read_only_fields = ['id', 'order_number', 'user', 'created_at', 'total_amount']
        
    def create(self, validated_data):
        product = validated_data.pop('product')
        quantity = validated_data.pop('quantity')
        user = self.context['request'].user
        
        # Calculate total amount automatically
        validated_data['total_amount'] = product.price * quantity
        
        if user.is_authenticated:
            validated_data['user'] = user
            
        order = Order.objects.create(**validated_data)
        
        # Create the order item
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price_at_purchase=product.price
        )
                
        return order
