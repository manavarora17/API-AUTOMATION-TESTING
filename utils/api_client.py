import requests

BASE_URL = "https://dummyjson.com"

def get_all_products():
    url = f"{BASE_URL}/products"
    response = requests.get(url)
    return response

def get_product_by_id(product_id):
    url = f"{BASE_URL}/products/{product_id}"
    response = requests.get(url)
    return response

def add_product(payload):
    url = f"{BASE_URL}/products/add"
    response = requests.post(url, json=payload)
    return response

def update_product(product_id, payload):
    url = f"{BASE_URL}/products/{product_id}"
    response = requests.put(url, json=payload)
    return response

def delete_product(product_id):
    url = f"{BASE_URL}/products/{product_id}"
    response = requests.delete(url)
    return response
