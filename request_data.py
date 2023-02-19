payload = {
    'priceRangeMinPrice': '',
    'priceRangeMaxPrice': '',
    'btnAllOptUse': 'true',
    'searchMaker[]': '',
    'searchAttributeValue[]': '',
    'page': '1',
    'listCategoryCode': '751',
    'categoryCode': '751',
    'physicsCate1': '861',
    'physicsCate2': '875',
    'physicsCate3': '0',
    'physicsCate4': '0',
    'viewMethod': 'LIST',  # LIST/IMAGE
    'sortMethod': 'BEST',  # BEST/NEW/MinPrice/MaxPrice/MaxMall/BoardCount
    'listCount': '90',  # 30/60/90
    'group': '11',
    'depth': '2',
    'brandName': '',
    'makerName': '',
    'searchOptionName': '',
    'sDiscountProductRate': '0',
    'sInitialPriceDisplay': 'N',
    'sMallMinPriceDisplayYN': '',
    'undefined': '',
    'innerSearchKeyword': '-해외구매 -중고 -렌탈',  # exclude with -"string"
    'innerDetailSearchKeyword': '!해외구매|!중고|!렌탈',
    'listPackageType': '1',
    'categoryMappingCode': '703',
    'priceUnit': '0',
    'priceUnitValue': '0',
    'priceUnitClass': '',
    'cmRecommendSort': 'N',
    'cmRecommendSortDefault': 'N',
    'bundleImagePreview': 'N',
    'nPackageLimit': '5',
    'bMakerDisplayYN': 'Y',
    'dnwSwitchOn': '',
    'isDpgZoneUICategory': 'N',
    'isAssemblyGalleryCategory': 'Y ',
    'sProductListApi': 'search'
}

headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '1000',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://prod.danawa.com',
    'Referer': 'https://prod.danawa.com/list/?cate=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def set_listing(a):
    payload['sortMethod'] = str(a)


def put_categoryCode(a, b, c, d='0', e='0'):
    payload['physicsCate1'] = str(b)
    payload['physicsCate2'] = str(c)
    payload['physicsCate3'] = str(d)
    payload['physicsCate4'] = str(e)
    payload['listCategoryCode'] = str(a)
    payload['categoryCode'] = str(a)


def set_cpu():
    put_categoryCode('747', '861', '873')


def set_mb():
    put_categoryCode('751', '861', '875')


def set_ram():
    put_categoryCode('752', '861', '874')


def set_ram_PC_DDR5():
    put_categoryCode('41201', '861', '874')


def set_ram_PC_DDR4():
    put_categoryCode('1326', '861', '874')


def set_vga():
    put_categoryCode('753', '861', '876')


def set_ssd():
    put_categoryCode('760', '861', '32617')
    payload['searchAttributeValueRep[]'] = '760|14689|86069|OR'

# def set_cpu_arch(): # fixed RaptorLake
# payload['searchAttributeValueRep[]'] = '747|32302|807919|OR'
# payload['searchAttributeValue[0]'] = '747|32302|807919|OR'
# payload['searchAttributeValue[1]'] = '747|32302|748297|OR'
# payload['searchAttributeValue[2]'] = '747|32302|801673|OR'
# payload['searchAttributeValue[3]'] = '747|32302|706786|OR'

# def set_cpu_market(): #set distribution cannel
# payload['searchAttributeValue[4]'] = '747|53|352|OR'  # 정품
# payload['searchAttributeValue[5]'] = '747|53|710710|OR'  # 멀티팩(정품)
