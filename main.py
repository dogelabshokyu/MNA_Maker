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

import stringcheese

# Danawa Product searching ajax using with HTTP POST
url = "https://prod.danawa.com/list/ajax/getProductList.ajax.php"

# Put all Product Spec
infoJAR = {}


# V for Product Counting
# count_num = 0

'''

'''
def recompilerException(keyword, keyfrom, whenexcept='X', group=0):
    rce_tmp = re.compile(keyword).search(keyfrom)
    if rce_tmp == None:
        rce_tmp = whenexcept
    else:
        rce_tmp = rce_tmp.group(group)
    return rce_tmp


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
    got_list = getProductList()
    #pINFO = got_list.findAll(class_=re.compile("^prod_item prod_layer(?! product-pot)"))
    page_listing = got_list.findAll(class_=re.compile("^num now_on$|^num$"))
    for j in page_listing:
        request_data.payload['page'] = j
        got_list = getProductList()
        pINFO = got_list.findAll(class_=re.compile("^prod_item prod_layer(?! product-pot)"))
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


'''
# CPU
request_data.set_cpu()
for i in ProductID.CPU.values():
    request_data.payload['searchAttributeValue[]'] = i
    for j in showProductList():
        a = stringcheese.hotcheese_cpu(j)
        print(a)
'''

'''
# MainBoard
request_data.set_mb()
for i in ProductID.MainBoard['Chipset'].values():
    request_data.payload['searchAttributeValue[]'] = i
    for j in ProductID.MainBoard['Manufacturer'].values():
        request_data.payload['searchMaker[]'] = j
        for k in showProductList():
            a = stringcheese.hotcheese_mb(k)
            print(a)
'''
'''
# RAM
request_data.set_ram_PC_DDR5()
for i in ProductID.RAM['Manufacturer'].values():
    request_data.payload['searchMaker[]'] = i
    for j in showProductList():
        a = stringcheese.hotcheese_ram(j)
        print(a)


request_data.set_ram_PC_DDR4()
for i in ProductID.RAM['Manufacturer'].values():
    request_data.payload['searchMaker[]'] = i
    for j in showProductList():
        a = stringcheese.hotcheese_ram(j)
        print(a)
'''


'''
# VGA
request_data.set_vga()
for i in ProductID.VGA['GPU'].values():
    request_data.payload['searchAttributeValue[]'] = i
    for j in ProductID.VGA['Manufacturer'].values():
        request_data.payload['searchMaker[]'] = j
        for k in showProductList():
            a = stringcheese.hotcheese_vga(k)
            print(a)
'''

# SSD
