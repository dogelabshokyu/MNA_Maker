import requests
from bs4 import BeautifulSoup

import request_data
import ProductID

url = "https://prod.danawa.com/list/ajax/getProductList.ajax.php"
response = requests.request("post", url, headers=request_data.headers, data=request_data.payload)
response.raise_for_status()
yammysoup = BeautifulSoup(response.text, "html.parser")
print(yammysoup)

print(ProductID.CPU.intel)