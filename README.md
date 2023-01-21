# getProductList.ajax.php

- Category

|  CPU  |  112747  |
|:-----:|:--------:|

- Marker

| MARKER  |         ID          |
|:-------:|:-------------------:|
|  Intel  | searchMakerRep3156  |
|   AMD   | searchMakerRep3132  |


- codename

|            Codename             |              ID               |
|:-------------------------------:|:-----------------------------:|
|              랩터레이크              | searchAttributeValueRep807919 |
|              엘더레이크              | searchAttributeValueRep748297 |
|               라파엘               | searchAttributeValueRep801673 |
|               버미어               | searchAttributeValueRep706786 |
|               세잔                | searchAttributeValueRep74091  |

- Category


# WIP
## Payload

```
priceRangeMinPrice: 
priceRangeMaxPrice: 
btnAllOptUse: true
searchAttributeValueRep[]: 753|658|805762|OR
searchAttributeValue[]: 753|658|805762|OR
page: 1
listCategoryCode: 753
categoryCode: 753
physicsCate1: 861
physicsCate2: 876
physicsCate3: 0
physicsCate4: 0
viewMethod: LIST
sortMethod: BEST
listCount: 90
group: 11
depth: 2
brandName: 
makerName: 
searchOptionName: 
sDiscountProductRate: 0
sInitialPriceDisplay: N
sPowerLinkKeyword: 그래픽카드
oCurrentCategoryCode: a:2:{i:1;i:97;i:2;i:753;}
sMallMinPriceDisplayYN: undefined
innerSearchKeyword:  -해외구매 -중고
listPackageType: 1
categoryMappingCode: 705
priceUnit: 0
priceUnitValue: 0
priceUnitClass: 
cmRecommendSort: N
cmRecommendSortDefault: N
bundleImagePreview: N
nPackageLimit: 5
bMakerDisplayYN: Y
dnwSwitchOn: 
isDpgZoneUICategory: N
isAssemblyGalleryCategory: Y
sProductListApi: search   
```
***
priceRangeMin/MaxPrice : price range  
btnAllOptUse : ?  
searchAttributeValueRep / searchAttributeValue : 옵션 753(VGA). 658(NVIDIA)/657(AMD), 805762(4090)/818815(7900XTX)  
page : 서칭 페이지  
listCategorycode : 상품 종류 753(VGA)  
categoryCode : 위와 동일  
physicsCate1: ?  
physicsCate2: ?  
physicsCate3: ?  
physicsCate4: ?  
viewMethod: LIST / IMAGE  
sortMethod: BEST / NEW / MinPrice / MaxPrice / MaxMall / BoardCount  
listCount : 페이지당 상품수 30/60/90 억지로 못 늘림

sPowerLinkKeyword : 상품리스트 상단 광고 삽입용 키워드   
innerSearchKeyword : 포함 혹은 제외(-)키워드   
nPackageLimit : 상품 유통 방식 노출 갯수