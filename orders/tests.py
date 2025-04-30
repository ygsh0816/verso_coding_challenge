import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Company, Product, Order, OrderProduct
from django.forms.models import model_to_dict
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def companies():
    customer = Company.objects.create(name="Customer Inc.")
    supplier = Company.objects.create(name="Supplier LLC")
    return customer, supplier

@pytest.fixture
def products():
    product1 = Product.objects.create(name="Widget", price=9.99)
    product2 = Product.objects.create(name="Gadget", price=14.99)
    return product1, product2

@pytest.mark.django_db
def test_create_product(api_client):
    response = api_client.post(reverse('product-list'), {'name': 'Test Product', 'price': 19.99})
    assert response.status_code == 201
    assert Product.objects.count() == 1

@pytest.mark.django_db
def test_create_order(api_client, companies, products):
    customer, supplier = companies
    product1, product2 = products
    data = {
        "customer_id": customer.id,
        "supplier_id": supplier.id,
        "items": [
            {"product_id": product1.id, "quantity": 2},
            {"product_id": product2.id, "quantity": 3}
        ]
    }
    response = api_client.post(reverse('order-list'), data, format='json')
    
    assert response.status_code == 201
    assert Order.objects.count() == 1
    order = Order.objects.first()
    assert order.items.count() == 2
    assert order.items.filter(product=product1, quantity=2).exists()
    assert order.items.filter(product=product2, quantity=3).exists()

@pytest.mark.django_db
def test_update_order(api_client, companies, products):
    customer, supplier = companies
    product1, product2 = products

    # Create an order with initial items
    order = Order.objects.create(customer=customer, supplier=supplier)
    OrderProduct.objects.create(order=order, product=product1, quantity=1)

    # URL for updating the order
    url = reverse('order-detail', args=[order.id])

    # Data for updating the order
    data = {
        "customer_id": customer.id,
        "supplier_id": supplier.id,
        "items": [
            {"product_id": product1.id, "quantity": 5},  # Update quantity for product1
            {"product_id": product2.id, "quantity": 3}   # Add product2
        ]
    }

    # Send PUT request to update the order
    response = api_client.put(url, data, format='json')
    assert response.status_code == 200

    # Refresh the order from the database
    order.refresh_from_db()

    # Verify the updated order
    assert order.items.count() == 2
    assert order.items.filter(product=product1, quantity=5).exists()
    assert order.items.filter(product=product2, quantity=3).exists()

@pytest.mark.django_db
def test_delete_product(api_client, products):
    product1, _ = products
    url = reverse('product-detail', args=[product1.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert Product.objects.filter(id=product1.id).count() == 0

@pytest.mark.django_db
def test_list_orders(api_client, companies, products):
    customer, supplier = companies
    product1, product2 = products

    # Create an order with associated products
    order = Order.objects.create(customer=customer, supplier=supplier)
    OrderProduct.objects.create(order=order, product=product1, quantity=2)
    OrderProduct.objects.create(order=order, product=product2, quantity=3)

    # URL for listing orders
    response = api_client.get(reverse('order-list'))
    assert response.status_code == 200
    
    # Verify the response contains the order and its products
    assert len(response.data) >= 1
    order_data = response.data[0]
    assert order_data['customer'] == model_to_dict(customer)
    assert order_data['supplier'] == model_to_dict(supplier)
    assert 'items_detail' in order_data
    assert len(order_data['items_detail']) == 2
    # Verify the products in the items_detail field
    products = [item['product'] for item in order_data['items_detail']]
    assert [model_to_dict(product1), model_to_dict(product2)] == products
