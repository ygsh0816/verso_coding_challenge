from django.urls import path
from .views import (
    CompanyListCreateView,
    CompanyDetailView,
    ProductListCreateView,
    ProductDetailView,
    OrderListCreateView,
    OrderDetailView
)

urlpatterns = [
    # Company URLs
    path('companies/', CompanyListCreateView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),

    # Product URLs
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Order URLs
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]