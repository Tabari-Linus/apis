import requests

endpoint = "http://localhost:8000/api/products/1678889/"
  


get_response = requests.get(endpoint)  # API # HTTP Request

print(get_response.json())