from rest_framework import serializers
from .models import Company, Product, Order, OrderProduct

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address']

class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)  # Ensure price is returned as a decimal
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']
    
    def to_representation(self, instance):
        """Override to_representation to convert Decimal to float."""
        representation = super().to_representation(instance)
        representation['price'] = float(representation['price'])  # Convert Decimal to float
        return representation

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Include full product details for output
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, source='product')

    class Meta:
        model = OrderProduct
        fields = ['product', 'product_id', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    customer = CompanySerializer(read_only=True)  # Include full customer details for output
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), write_only=True, source='customer')
    supplier = CompanySerializer(read_only=True)  # Include full supplier details for output
    supplier_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), write_only=True, source='supplier')
    items = OrderProductSerializer(many=True, write_only=True)  # For input
    items_detail = OrderProductSerializer(many=True, read_only=True, source='items')  # For output

    class Meta:
        model = Order
        fields = ['id', 'customer', 'customer_id', 'supplier', 'supplier_id', 'created_at', 'items', 'items_detail']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        order = Order.objects.create(**validated_data)
        for item in items_data:
            OrderProduct.objects.create(order=order, **item)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        instance.customer = validated_data.get('customer', instance.customer)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.save()

        if items_data:
            instance.items.all().delete()
            for item in items_data:
                OrderProduct.objects.create(order=instance, **item)
        return instance