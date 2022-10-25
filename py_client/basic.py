from xml.dom.minidom import Notation
import requests

endpoint = "https://www.httpbin.org/status/200/"
endpoint = "https://www.httpbin.org/anything"
endpoint = "http://localhost:8000/api/"
  


get_response = requests.get(endpoint, params={"abc": 123}, json={"product_id": 123})  # API # HTTP Request
#print(get_response.text.encode("utf-8")) # print the raw text response
print(get_response.status_code)

 

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict
print(get_response.json())
