# Register your models here.
from django.contrib import admin
from .models import Company, Product, Order, OrderProduct

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'created_at')
    search_fields = ('name', 'address')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'supplier', 'created_at')
    search_fields = ('customer__name', 'supplier__name')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    inlines = [OrderProductInline]

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')
    search_fields = ('order__id', 'product__name')
    list_filter = ('order__created_at',)