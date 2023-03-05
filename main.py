# Python Library
import time

import requests
import re
from bs4 import BeautifulSoup
import json
import logging
from openpyxl import Workbook

# USER Library
import request_data
import ProductID

# For check V anyway
from pyprnt import prnt

import stringcheese

# Danawa Product searching ajax using with HTTP POST
url = "https://prod.danawa.com/list/ajax/getProductList.ajax.php"

# Func DEBUG

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.info("=== LOGGING START ===")


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
    request_data.payload['page'] = 1
    got_list = getProductList()
    # pINFO = got_list.findAll(class_=re.compile("^prod_item prod_layer(?! product-pot)"))
    page_listing = got_list.findAll(class_=re.compile("^num now_on$|^num$"))
    for j in page_listing:
        request_data.payload['page'] = j.text
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

# CPU
logger.info("CPU START")
output = open("./crawl_data/CPU.txt", "a+")
output.write("제품\t정품\t벌크\t멀티팩\t코어\t쓰레드\t정규\t터보\tL3캐시\t내장그래픽\t메모리 지원클럭\tTDP\t소켓\t쿨러\n")
request_data.set_cpu()
for i in ProductID.CPU.values():
    request_data.payload['searchAttributeValue[]'] = i
    for j in showProductList():
        a = stringcheese.hotcheese_cpu(j)
        # print(a)
        output.write(a + "\n")
output.close()
logger.info("CPU DONE")

# MainBoard
logger.info("MAINBOARD START")
output = open("./crawl_data/MAINBOARD.txt", "a+")
output.write("제품\t가격\t폼팩터\t램\t클럭\t슬롯\tHDMI\tDP\tSATA\tM.2\t전원부\tDr.MOS\tRGB\tetc(LAN, AUDIO)\n")
request_data.set_mb()
for i in ProductID.MainBoard['Chipset'].values():
    request_data.payload['searchAttributeValue[]'] = i
    for j in ProductID.MainBoard['Manufacturer'].values():
        request_data.payload['searchMaker[]'] = j
        for k in showProductList():
            a = stringcheese.hotcheese_mb(k)
            # print(a)
            output.write(a + "\n")
output.close()
logger.info("MAINBOARD DONE")


# RAM
logger.info("DDR5 RAM START")
output = open("./crawl_data/RAM_DDR5.txt", "a+")
output.write("제품명\t클럭\t타이밍\t전압\t히트싱크\t색상\tLED\t용량+가격\n")
request_data.set_ram_PC_DDR5()
for i in ProductID.RAM['Manufacturer'].values():
    request_data.payload['searchMaker[]'] = i
    for j in showProductList():
        a = stringcheese.hotcheese_ram(j)
        # print(a)
        output.write(a + "\n")
output.close()
logger.info("DDR5 RAM DONE")

logger.info("DDR4 RAM START")
output = open("./crawl_data/RAM_DDR4.txt", "a+")
output.write("제품명\t클럭\t타이밍\t전압\t히트싱크\t색상\tLED\t용량+가격\n")
request_data.set_ram_PC_DDR4()
for i in ProductID.RAM['Manufacturer'].values():
    request_data.payload['searchMaker[]'] = i
    for j in showProductList():
        a = stringcheese.hotcheese_ram(j)
        # print(a)
        output.write(a + "\n")
output.close()
logger.info("DDR4 RAM DONE")


# VGA
logger.info("VGA START")
output = open("./crawl_data/VGA.txt", "a+")
output.write("제품\t가격\t정규클럭\t부스트클럭\t팬\t길이\t두께\t전원입력\t소모전력\t권장파워\tCUDA/SP\n")
request_data.set_vga()
for i in ProductID.VGA['GPU'].values():
    request_data.payload['searchAttributeValue[]'] = i
    for j in ProductID.VGA['Manufacturer'].values():
        request_data.payload['searchMaker[]'] = j
        for k in showProductList():
            a = stringcheese.hotcheese_vga(k)
            # print(a)
            output.write(a + "\n")
output.close()
logger.info("VGA DONE")


# SSD
logger.info("SSD START")
output = open("./crawl_data/SSD.txt", "a+")
output.write("제품\t크기\tPHY\t프로토콜\t낸드\t컨트롤러\tR\tW\tTRIM\tGC\tS.M.A.R.T\tECC\tDEVSLP\tSLC caching\tA/S\t용량+가격\n")
request_data.set_ssd()
for i in ProductID.SSD['Manufacturer'].values():
    request_data.payload['searchMaker[]'] = i
    for j in showProductList():
        for k in ProductID.list_dist:
            j = j \
                .replace(k, '') \
                .replace('Western Digital ', '') \
                .replace(' 벌크완제품에서 적출된 상품은 제품 외관에 사용감이 있을 수 있습니다.', ' 적출벌크')
        a = stringcheese.hotcheese_ssd(j)
        # print(a)
        output.write(a + "\n")
output.close()
logger.info("SSD DONE")


# HDD
logger.info("HDD START")
output = open("./crawl_data/HDD.txt", "a+")
output.write("제품\t용도\t크기\t물리규격\t버퍼\t회전수\t모델명/용량 - 가격\n")
request_data.set_hdd()
for i in ProductID.HDD['Manufacturer'].values():
    request_data.payload['searchMaker[]'] = i
    for j in showProductList():
        a = stringcheese.hotcheese_hdd(j)
        # print(a)
        output.write(a + "\n")
output.close()
logger.info("HDD DONE")


# CHA
logger.info("CHA START")
output = open("./crawl_data/CHA.txt", "a+")
output.write("제품명\t종류\tE-ATX\tATX\tmATX\tITX\t측면\t폭\t높이\t깊이\tVGA 지원\tCPU쿨러 지원\t가격(색상)\n")
request_data.set_cha()
for i in ProductID.CHA['Manufacturer'].values():
    request_data.payload['searchMaker[]'] = i
    for j in showProductList():
        a = stringcheese.hotcheese_cha(j)
        # print(a)
        output.write(a + "\n")
output.close()
logger.info("CHA DONE")


# PSU
logger.info("PSU START")
output = open("./crawl_data/PSU.txt", "a+")
output.write("제품\t종류\t정격\tActive PFC\t레일\t12V 가용률\tIDE\tPCIe 6핀\tPCIe 8핀\tPCIe 16핀\t모듈러\t대기전력 1W\t플랫케이블\t프리볼트\t깊이\t80+\tETA\tLAMBDA\t무상AS\t유상AS\t가격\n")
request_data.set_psu()
for i in ProductID.PSU['Manufacturer'].values():
    request_data.payload['searchMaker[]'] = i
    for j in ProductID.PSU['Type'].values():
        request_data.payload['searchAttributeValue[]'] = j
        for k in showProductList():
            a = stringcheese.hotcheese_psu(k)
            output.write(a + "\n")
output.close()
logger.info("PSU DONE")
logger.info('END')