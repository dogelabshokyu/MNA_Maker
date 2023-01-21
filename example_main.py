import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


'''
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
items = soup.find_all('li', attrs={'class':re.compile('^prod_item prod_layer')}) # li 태그 중에서 클래스가 prod_item으로 시작하는 모든 값
for item in items[:30]:
  name = item.find('p', attrs={'class':'prod_name'}).a.get_text().strip()
  date = item.find('dl', attrs={'class':'meta_item mt_date'}).dd.get_text()
  spec_item = items[0].find('div', attrs={'class':'spec_list'}).get_text().strip()
  print('상품명:',name)
  price_lists = item.find_all('li', adttrs={'id':re.compile('^productInfoDetail')})
  for price_list in price_lists:
    storage = price_list.find('p', attrs={'class':'memory_sect'}).get_text().strip()
    price = price_list.find('p', attrs={'class':'price_sect'}).a.strong.get_text()
    print('가격: {0}원 ({1})'.format(price,storage.replace("\n", "",).replace("	","")))
  print('------'*15)
'''

def getCPUPrice(url):
  res = requests.get(url, headers=headers)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, 'lxml')
  items = soup.find_all('li', attrs={'class': re.compile('^prod_item prod_layer')})
  items = soup.find_all('li',
                        attrs={'class': re.compile('^prod_item prod_layer')})  # li 태그 중에서 클래스가 prod_item으로 시작하는 모든 값
  for item in items[:30]:
    name = item.find('p', attrs={'class': 'prod_name'}).a.get_text().strip()
    #date = item.find('dl', attrs={'class': 'meta_item mt_date'}).dd.get_text()
    spec_item = items[0].find('div', attrs={'class': 'spec_list'}).get_text().strip()
    print()
    if 'APPLE' in name:
      print('애플 제품은 제외합니다.')
    else:
      print('상품명:', name)
      #print('출시일: {0}'.format(date))
      print('상품 스펙: {}'.format(spec_item))
      price_lists = item.find_all('li', attrs={'id': re.compile('^productInfoDetail')})
      for price_list in price_lists:
        storage = price_list.find('p', attrs={'class': 'memory_sect'}).get_text().strip()
        price = price_list.find('p', attrs={'class': 'price_sect'}).a.strong.get_text()
        print('가격(용량): {0}원({1})'.format(price, storage))
      link = item.find('p', attrs={'class': 'prod_name'}).a['href']
      print(link)
    print()
    print('------' * 25)

intel_12="https://prod.danawa.com/list/?cate=11341237"
intel_13="https://prod.danawa.com/list/?cate=11345419"
ryzen_4="https://prod.danawa.com/list/?cate=11339002"
ryzen_5="https://prod.danawa.com/list/?cate=11344988"

for i in {intel_12,intel_13,ryzen_4,ryzen_5}:
  getCPUPrice(i)

#getCPUPrice("https://prod.danawa.com/list/?cate=112747")