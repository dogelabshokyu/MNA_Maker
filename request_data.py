payload = {
    'priceRangeMinPrice': '',
    'priceRangeMaxPrice': '',
    'btnAllOptUse': 'true',
    'searchMakerRep[]': '',
    'searchAttributeValue[]':'',
    'page': '1',
    'listCategoryCode': '751',
    'categoryCode': '751',
    'physicsCate1': '861',
    'physicsCate2': '875',
    'physicsCate3': '0',
    'physicsCate4': '0',
    'viewMethod': 'LIST',   # LIST/IMAGE
    'sortMethod': 'BEST',   # BEST/NEW/MinPrice/MaxPrice/MaxMall/BoardCount
    'listCount': '30',      # 30/60/90
    'group': '11',
    'depth': '2',
    'brandName': '',
    'makerName': '',
    'searchOptionName': '',
    'sDiscountProductRate': '0',
    'sInitialPriceDisplay': 'N',
    'sMallMinPriceDisplayYN': '',
    'undefined': '',
    'innerSearchKeyword': '',   # exclude with -"string"
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
    'Referer': 'https://prod.danawa.com/list/?cate=112751',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def set_listing(a):
    payload['sortMethod'] = str(a)
def set_cpu():
    payload['listCategoryCode'] = '747'
    payload['categoryCode'] = '747'
    payload['physicsCate1'] = '861'
    payload['physicsCate2'] = '873'
    payload['physicsCate3'] = '0'
    payload['physicsCate4'] = '0'
def set_cpu_maker(): # fixed Intel
    payload['searchMaker'] = '3156'

def set_cpu_arch(): # fixed RaptorLake
    #payload['searchAttributeValueRep[]'] = '747|32302|807919|OR'
    payload['searchAttributeValue[]'] = '747|32302|807919|OR'