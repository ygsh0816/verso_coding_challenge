# Verso Coding Task

This project is a Django REST API for managing companies, products, and orders. It includes endpoints for creating, updating, and retrieving orders with nested product details.

## Features

- **Company Management**: Create, update, and retrieve companies.
- **Product Management**: Create, update, and retrieve products.
- **Order Management**: Create, update, and retrieve orders with nested product details.
- **Test Coverage**: Includes unit tests for key functionalities.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ygsh0816/verso_coding_challenge.git
   cd verso-coding-task
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Company Endpoints
- `GET /api/companies/`: List all companies.
  #### Response 
  <pre>
  [
    {
        "id": 2,
        "name": "New Company",
        "address": "123 Business Street1"
    },
    {
        "id": 3,
        "name": "Latest Inc",
        "address": "Falana Dhimkana"
    }
  ] 
  </pre>
- `POST /api/companies/`: Create a new company.
    #### Request Data
    <pre>
    {
        "name": "Customer Inc.",
        "address": "123 Business Street"
    }
  </pre> 
- `GET /api/companies/<id>/`: Retrieve a specific company.
- `PUT /api/companies/<id>/`: Update a specific company(Complete Object).
- `PATCH /api/companies/<id>/`: Update a specific company(Certain attributes).
- `DELETE /api/companies/<id>/`: Delete a specific company.

### Product Endpoints
- `GET /api/products/`: List all products.
- `POST /api/products/`: Create a new product.
    #### Request Data
    <pre>
    {
        "name": "Widget",
        "price": 9.99
    }
  </pre>
- `GET /api/products/<id>/`: Retrieve a specific product.
- `PUT /api/products/<id>/`: Update a specific product(Complete Object).
- `PATCH /api/products/<id>/`: Update a specific product(Certain attributes).
- `DELETE /api/products/<id>/`: Delete a specific product.


### Order Endpoints
- `GET /api/orders/`: List all orders.
- `POST /api/orders/`: Create a new order.
  #### Request Data
    <pre>
      {
        "customer_id": 2,
        "supplier_id": 3,
        "items": [
          {
            "product_id": 3,
            "quantity": 2
          },
          {
            "product_id": 2,
            "quantity": 3
          }
        ]
      }
      </pre>
- `GET /api/orders/<id>/`: Retrieve a specific order.
- `PUT /api/orders/<id>/`: Update a specific order(Complete Object).
- `PATCH /api/orders/<id>/`: Update a specific order(Certain attributes).
- `DELETE /api/orders/<id>/`: Delete a specific order.

#### Orders POST API request Data



## Running Tests

Run the following command to execute the test suite:
```bash
pytest
```

# Future Improvements

### Validation in Models and Serializers
- Add custom validation in the `OrderSerializer` to ensure that the customer and supplier are not the same.
- Validate that the quantity in `OrderProduct` is greater than zero.

### Error Handling
- Improve error handling in views and serializers to provide more descriptive error messages.
- Add exception handling for edge cases like invalid product IDs in the `items` field.

### Test Coverage
- Add more test cases to cover edge cases, such as:
  - Creating an order with invalid data.
  - Updating an order with invalid or missing `items`.
  - Deleting an order and ensuring associated `OrderProduct` entries are also deleted.
- Use parameterized tests to reduce redundancy in test cases.

### Performance Optimization
- Use `select_related` and `prefetch_related` in queries to optimize database access for related fields (e.g., `customer_orders` and `supplier_orders`).

### API Documentation
- Use a tool like [drf-yasg](https://drf-yasg.readthedocs.io/) or [Swagger](https://swagger.io/) to generate API documentation for better developer experience.

### Pagination
- Add pagination to the list views for `Order`, `Product`, and `Company` to handle large datasets efficiently.

### Authentication and Permissions
- Add authentication (e.g., JWT or session-based) and permissions to restrict access to certain endpoints.

### Data Integrity
- Add database constraints, such as unique constraints for `Company` names or indexes for frequently queried fields.

### CI/CD Integration
- Set up Continuous Integration (CI) pipelines using tools like GitHub Actions to automatically run tests and linting on every commit.

## 🧪 Code Quality & Best Practices

To ensure high-quality, maintainable, and secure code, the following tools and practices could be followed:

### 1. **Code Formatting**
- Use **`black`** for automatic code formatting to maintain a consistent style across the project.
  - Black enforces a uniform code style, making the codebase easier to read and review.
    ```bash
    black .

### 2. **Linting**
- Use **`flake8`** or **`ruff`** for linting to identify and fix potential issues in the code.
  - **`flake8`**: A popular Python linter that checks for PEP 8 compliance and other common issues.
  - **`ruff`**: A fast Python linter that can replace `flake8` and other tools with additional features.
    ```bash
    ruff check .
    ```

### 3. **Static Type Checking**
- Use **`mypy`** to enforce type hints and catch type-related errors before runtime.
  - Adding type hints improves code readability and helps developers understand function inputs and outputs.
    ```bash
    mypy .
    ```

### 4. **Testing**
- Use **`pytest`** for writing and running tests.
  - Pytest is a powerful testing framework that supports fixtures, parameterized tests, and more.
    ```bash
    pytest
    ```

### 5. **Test Coverage**
- Use **`coverage`** to measure test coverage and ensure all critical parts of the code are tested.
    ```bash
    pytest --cov=.
    ```

### 6. **Security Scanning**
- Use **`bandit`** to scan the codebase for common security vulnerabilities.
  - Bandit analyzes Python code for security issues, such as unsafe function calls or improper handling of sensitive data.
    ```bash
    bandit -r .
    ```

### 7. **Dependency Vulnerability Audit**
- Use **`pip-audit`** to check for known vulnerabilities in project dependencies.
  - Pip-audit scans the `requirements.txt` or installed packages for vulnerabilities and suggests updates.
    ```bash
    pip-audit
    ```

### 8. **Pre-commit Hooks**
- Use **`pre-commit`** to automate code quality checks before committing changes.
  - Pre-commit hooks can run tools like `black`, `ruff`, `mypy`, and `pytest` automatically.
  - Example `.pre-commit-config.yaml`:
    ```yaml
    repos:
      - repo: https://github.com/charliermarsh/ruff
        rev: v0.0.285
        hooks:
          - id: ruff
      - repo: https://github.com/pre-commit/mirrors-mypy
        rev: v1.2.0
        hooks:
          - id: mypy
    ```
  - Install pre-commit hooks:
    ```bash
    pre-commit install
    ```

---


