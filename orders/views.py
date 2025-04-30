from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Company, Product, Order
from .serializers import CompanySerializer, ProductSerializer, OrderSerializer
from django.http import JsonResponse

def health_check(request):
    """Health check endpoint to verify the application is running."""
    return JsonResponse({"status": "ok", "message": "Application is healthy"})


class CompanyListCreateView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer