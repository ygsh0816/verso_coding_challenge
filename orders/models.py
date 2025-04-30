from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='customer_orders')
    supplier = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='supplier_orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Customer '{self.customer.name}'  ---   Supplier '{self.supplier.name}' "

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    
