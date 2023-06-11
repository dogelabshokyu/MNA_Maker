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


def put_categoryCode(listcatecode, phycate1, phycate2, phycate3='0', phycate4='0'):
    payload['listCategoryCode'] = str(listcatecode)
    payload['categoryCode'] = str(listcatecode)
    payload['physicsCate1'] = str(phycate1)
    payload['physicsCate2'] = str(phycate2)
    payload['physicsCate3'] = str(phycate3)
    payload['physicsCate4'] = str(phycate4)

def put_detailcategorycode(a, b, c, d, e='0', f='0'):
    payload['listCategoryCode'] = str(a)
    payload['categoryCode'] = str(b)
    payload['physicsCate1'] = str(c)
    payload['physicsCate2'] = str(d)
    payload['physicsCate3'] = str(e)
    payload['physicsCate4'] = str(f)

def payload_reset():
    payload['searchAttributeValue[]'] = ''
    payload['searchMaker[]'] = ''
    payload['searchAttributeValue[]'] = ''

def set_cpu():
    payload_reset()
    put_categoryCode('747', '861', '873')


def set_mb():
    payload_reset()
    put_categoryCode('751', '861', '875')


def set_ram():
    payload_reset()
    put_categoryCode('752', '861', '874')


def set_ram_PC_DDR5():
    payload_reset()
    put_categoryCode('41201', '861', '874')


def set_ram_PC_DDR4():
    payload_reset()
    put_categoryCode('1326', '861', '874')


def set_vga():
    payload_reset()
    put_categoryCode('753', '861', '876')


def set_ssd():
    payload_reset()
    put_categoryCode('760', '861', '32617')
    payload['searchAttributeValue[]'] = '760|14689|86069|OR'

def set_hdd():
    payload_reset()
    put_categoryCode('763', '861', '877')


def set_cha():
    payload_reset()
    put_categoryCode('775', '861', '879')
    payload['searchAttributeValue[]'] = '775|976|5160|OR'

def set_psu():
    payload_reset()
    put_categoryCode('777', '861', '880')


def set_cpu_cooler():
    payload_reset()
    put_categoryCode('30256', '862', '887')

def set_cpu_aio():
    payload_reset()
    put_categoryCode('1545', '862', '887')

def set_sys_fan():
    payload_reset()
    put_categoryCode('1548', '862', '887')