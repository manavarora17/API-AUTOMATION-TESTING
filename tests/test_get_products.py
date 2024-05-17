import pytest
import requests

@pytest.mark.parametrize("endpoint", [
    "/products"
])
def test_get_products(endpoint):
    url = f"https://dummyjson.com{endpoint}"
    response = requests.get(url)
    assert response.status_code == 200
    assert len(response.json()) > 0  # Assuming response is a non-empty list


if __name__ == "__main__":
    
    pytest.main()