# Python Library
import requests
from bs4 import BeautifulSoup
import json

# USER Library
import request_data
import ProductID

url = "https://prod.danawa.com/list/ajax/getProductList.ajax.php"
response = requests.request("post", url, headers=request_data.headers, data=request_data.payload)
response.raise_for_status()
yammysoup = BeautifulSoup(response.text, "lxml")
#print(yammysoup)

pINFO = yammysoup.findAll(class_="prod_item prod_layer width_change")
#pINFO = yammysoup.findAll(class_="prod_item prod_layer width_change")
#print(pINFO)

for i in pINFO:
    everytext = i.text
    purestr = everytext\
        .replace("		","")\
        .replace("\n","")\
        .replace("이미지보기", "")\
        .replace("인기","")\
        .replace("동영상 재생","")

    clrstr = everytext.replace("		","").replace("\n","").replace("이미지보기", "")\
        .replace("인기","").replace("동영상 재생","").replace(" 순위","순위 ").replace(" / ", '	').replace("상세 스펙","	")
    print(purestr)
    #print(clrstr)