import pytest
import requests

def test_add_product_positive():
    url = "https://dummyjson.com/products/add"
    payload = {
        "name": "New Product",
        "price": 10.99,
        "description": "Test description"
        # Add other required fields as per API documentation
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    # Validate that the product is correctly added to the database

def test_add_product_negative():
    url = "https://dummyjson.com/products/add"
    payload = {}  # Missing required fields
    response = requests.post(url, json=payload)
    assert response.status_code == 400
if __name__ == "__main__":
    
    pytest.main()