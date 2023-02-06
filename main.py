# Python Library
import requests
import re
from bs4 import BeautifulSoup
import json

# USER Library
import request_data
import ProductID

url = "https://prod.danawa.com/list/ajax/getProductList.ajax.php"


def recompilerException(keyword, keyfrom, whenexcept):
    rce_tmp = re.compile(keyword).search(keyfrom)
    if rce_tmp == None:
        rce_tmp = whenexcept
    else:
        rce_tmp = rce_tmp.group()
    return rce_tmp

request_data.set_cpu()
# request_data.set_cpu_maker()
# request_data.set_cpu_arch()
request_data.set_listing('MinPrice')  # BEST/NEW/MinPrice/MaxPrice/MaxMall/BoardCount

response = requests.request("post", url, headers=request_data.headers, data=request_data.payload)
response.raise_for_status()
yammysoup = BeautifulSoup(response.text, "lxml")
# print(yammysoup)

pINFO = yammysoup.findAll(class_=re.compile("^prod_item prod_layer$(?!product-pot$)"))
# pINFO = yammysoup.findAll(class_="prod_item prod_layer width_change")
# print(pINFO)
infoJAR = {}
for i in pINFO:
    rawtext = i.text
    purestr = rawtext \
        .replace("		", "") \
        .replace("\n", "") \
        .replace("이미지보기", "") \
        .replace("인기", "") \
        .replace("동영상 재생", "") \
        .replace("\t", "")
    tmp = re.sub(' 순위[0-9]* ', "", purestr)
    purestr = tmp
    clrstr = rawtext \
        .replace("		", "") \
        .replace("\n", "") \
        .replace("이미지보기", "") \
        .replace("인기", "") \
        .replace("동영상 재생", "") \
        .replace(" 순위", "순위 ") \
        .replace(" / ", '	') \
        .replace("상세 스펙", "	")

    # pName = re.compile('^.+(?=상세 스펙)').search(purestr).group()
    pName = recompilerException('^.+(?=상세 스펙)', purestr, 'X')
    pSocket = recompilerException('소켓.{3,4}(?=\))', purestr, 'X')
    pCore = recompilerException('(?<= / )[0-9+]{1,8}(?=코어)', purestr, 'X')
    pThread = recompilerException('(?<= / ).{1,6}(?=쓰레드)', purestr, 'X')
    pBaseCLK = recompilerException('(?<=기본 클럭: )[0-9.]+(?=GHz)', purestr, 'X')
    pBoostCLK = recompilerException('(?<=최대 클럭: )[0-9.]+(?=GHz)', purestr, 'X')
    pTDP = recompilerException('(?<=TDP: ).{1,10}W|(?<=PBP/MTP: ).{1,10}W', purestr, 'X')
    pPCIE = recompilerException('PCIe[0-9., ]+(?= / )', purestr, 'X')
    pMem0 = recompilerException('(?<=메모리 규격: )[a-zA-Z0-9, ]+(?= / )', purestr, 'X')
    pMem1 = recompilerException('[0-9]{4}MHz|[0-9]{4}, [0-9]{4}MHz', purestr, 'X')
    pdGPU = recompilerException('(?<=내장그래픽: ).{2,3}(?= / )', purestr, 'X')
    if pdGPU == "탑재":
        pdGPU = re.compile('(?<=내장그래픽: 탑재 / ).{1,15}(?= / )|(?<=내장그래픽: 탑재 / ).{1,15}(?= 등록월)') \
            .search(purestr).group()
    pBundleCooler = recompilerException('(?<=쿨러: ).{1,20}(?= / )|(?<=쿨러: ).{1,20}(?=등록월)|(?<=쿨러: ).{1,20}(?= 등록월)', purestr, '미기재')
    pRiceRetail = recompilerException('(?<=[0-9]몰상품비교)[0-9,]+원(?=가격정보 더보기정품)', purestr, 'X')
    pRiceBulk = recompilerException('(?<=[0-9]몰상품비교)[0-9,]+원(?=가격정보 더보기벌크)', purestr, 'X')
    pRiceMultiRetail = recompilerException('(?<=[0-9]몰상품비교)[0-9,]+원(?=가격정보 더보기멀티팩\(정품\))', purestr, 'X')

    # print(rawtext)
    # print(purestr)
    printer = pName + '\t' \
              + pSocket + '\t' \
              + pCore + '\t' \
              + pThread + '\t' \
              + pBaseCLK + '\t' \
              + pBoostCLK + '\t' \
              + pTDP + '\t' \
              + pPCIE + '\t' \
              + pMem0 + '\t' \
              + pMem1 + '\t' \
              + pdGPU + '\t' \
              + pBundleCooler + '\t' \
              + pRiceRetail + '\t' \
              + pRiceMultiRetail + '\t' \
              + pRiceBulk
    print(printer)
