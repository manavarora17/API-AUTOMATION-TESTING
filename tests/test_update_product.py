import pytest
import requests

def test_update_product_positive():
    product_id = 1  # Assuming a valid product ID
    url = f"https://dummyjson.com/products/{product_id}"
    payload = {
        "name": "Updated Product Name",
        "price": 19.99,
        "description": "Updated test description"
        # Add other fields to update as needed
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    # Validate that the product details are correctly updated in the database

def test_update_product_negative():
    product_id = 9999  # Assuming an invalid product ID
    url = f"https://dummyjson.com/products/{product_id}"
    payload = {
        "name": "Updated Product Name",
        "price": 19.99,
        "description": "Updated test description"
        # Add other fields to update as needed
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 404
if __name__ == "__main__":
    
    pytest.main()