# MNA db crawler
문나와 DB 업데이트를 위한 다나와 상품리스트 크롤러입니다.  


|    Part    | Work  |
|:----------:|:-----:|
|    CPU     |   ✓   |
| Mainboard  |   ✓   |
|    RAM     |   ✓   |
|    VGA     |   ✓   |
|    SSD     |   ✓   |
|    HDD     |   ✓   |
|    CHA     |   X   |
|    PSU     |   X   |
|    FAN     |   X   |
| CPU Cooler |   X   |
|    KBD     |   X   |
|   Mouse    |   X   |

***
### main.py
대가리입니다~  

### ProductID.py
제조사의 경우 SearchMaker[] 에 넣으시고
기타 옵션은 searchAttributeValue[] 에 넣으시면 됩니다~

신생 제조사나 새로운 칩셋(PCH, GPU)등이 나왔다면 이 파일 수정하시면 됩니다.

### request_data.py
다나와 서버에 문 두드리는 친구입니다

### stringcheese.py
정규표현식으로 떡칠된 친구입니다.  
제품 스펙 읽은 후 이 친구로 처리하시면 됩니다.  
문자열 찢어 먹으니까 스트링치즈죠 ㅇㅅㅇ  
위의 ProductID.py와 더불어 신제품 나오면 이 친구 수정할 일이 있을껍니다

## Thanks to
stackoverflow, wikidocs, monster_energy