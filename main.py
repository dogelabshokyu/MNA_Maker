# Python Library
import requests
import re
from bs4 import BeautifulSoup
import json

# USER Library
import request_data
import ProductID

# For check V anyway
from pyprnt import prnt

import stringchesse

# Danawa Product searching ajax using with HTTP POST
url = "https://prod.danawa.com/list/ajax/getProductList.ajax.php"

# Put all Product Spec
infoJAR = {}


# V for Product Counting
# count_num = 0


def recompilerException(keyword, keyfrom, whenexcept='X', group=0):
    rce_tmp = re.compile(keyword).search(keyfrom)
    if rce_tmp == None:
        rce_tmp = whenexcept
    else:
        rce_tmp = rce_tmp.group(group)
    return rce_tmp


def tabsonic(*args):
    text = ''
    for i in args:
        text += i + "\t"
    return text


def sort_seller():
    print("WIP")


'''
MODIFY POST PAYLOAD UNDER HERE
'''
# Setting POST Body Payload
request_data.set_listing('MinPrice')  # BEST/NEW/MinPrice/MaxPrice/MaxMall/BoardCount
request_data.payload['page'] = 1

'''
POST HTTP and Get Product List as Payload

CPU prod_item prod_layer
MB  prod_item prod_layer width_change

'''


def getProductList():
    response = requests.request("post", url, headers=request_data.headers, data=request_data.payload)
    response.raise_for_status()
    yammy_soup = BeautifulSoup(response.text, "lxml")
    return yammy_soup


def showProductList():
    gotList = getProductList()
    #pINFO = gotList.findAll(class_=re.compile("^prod_item prod_layer(?! product-pot)"))
    page_listing = gotList.findAll(class_=re.compile("^num now_on$|^num$"))
    for j in page_listing:
        request_data.payload['page'] = j
        gotList = getProductList()
        pINFO = gotList.findAll(class_=re.compile("^prod_item prod_layer(?! product-pot)"))
        counter = range(len(pINFO))
        for i in pINFO:
            rawtext = i.text
            purestr = rawtext \
                .replace("		", "") \
                .replace("\n", "") \
                .replace("이미지보기", "") \
                .replace("인기", "") \
                .replace("동영상 재생", "") \
                .replace("\t", "")
            tmp_text = purestr
            purestr = re.sub(' 순위[0-9]* ', "", tmp_text)
            yield purestr


'''# CPU
request_data.set_cpu()
for i in ProductID.CPU.values():
    request_data.payload['searchAttributeValue[]'] = i
    for j in showProductList():
        a = stringchesse.string_JSON_cpu(j)
        b = stringchesse.cooking_cpu(a)
        print(b)

# MainBoard
request_data.set_mb()
for i in ProductID.MainBoard['Chipset'].values():
    request_data.payload['searchAttributeValue[]'] = i
    for j in ProductID.MainBoard['Manufacturer'].values():
        request_data.payload['searchMaker[]'] = j
        for k in showProductList():
            a = stringchesse.stringJSON_MB(k)
            b = stringchesse.cooking_mb(a)
            print(b)


# RAM
request_data.set_ram_PC_DDR5()
for i in ProductID.RAM['Manufacturer'].values():
    request_data.payload['searchMaker[]'] = i
    for j in showProductList():
        print(j)

request_data.set_ram_PC_DDR4()
for i in ProductID.RAM['Manufacturer'].values():
    request_data.payload['searchMaker[]'] = i
    for j in showProductList():
        print(j)

'''

# VGA
request_data.set_vga()
for i in ProductID.VGA['GPU'].values():
    request_data.payload['searchAttributeValue[]'] = i
    for j in ProductID.VGA['Manufacturer'].values():
        request_data.payload['searchMaker[]'] = j
        for k in showProductList():
            a = stringchesse.stringjson_vga(k)
            b = stringchesse.cooking_vga(a)
            print(b)
