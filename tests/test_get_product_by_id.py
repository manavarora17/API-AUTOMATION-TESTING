import pytest
import requests

def test_get_product_by_id_positive():
    product_id = 1  # Assuming a valid product ID
    url = f"https://dummyjson.com/products/{product_id}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() is not None

def test_get_product_by_id_negative():
    product_id = 9999  # Assuming an invalid product ID
    url = f"https://dummyjson.com/products/{product_id}"
    response = requests.get(url)
    assert response.status_code == 404
if __name__ == "__main__":
    
    pytest.main()