'''
@Author :LI_JIA_HAO
@Email ：291630817@qq.com
'''
import json
from threading import Thread

from selenium import webdriver
from urllib.parse import quote
from bs4 import BeautifulSoup
import requests
from functools import wraps
import redis


# def _async(func):
#     '''
#     异步处理函数数据,装饰器
#     :param func:
#     :return:
#     '''
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         thr = Thread(target = func, args = args, kwargs = kwargs)
#         thr.start()
#     return wrapper

def cjjc_spider(keyword):
    keyword = quote(keyword)
    url = 'https://cjjc.weblio.jp/content/' + keyword
    page_text = requests.get(url).text
    soup = BeautifulSoup(page_text,'lxml')
    try:
        content = soup.find('div',class_='Cgkgj').text
        content2 = soup.find_all('div',class_= "kiji")
    except:
        result = ['查找为空']
        # cache.delete('cjjc_' + keyword)
        # cache.set('cjjc_' + keyword, json.dumps(result), 60 * 60)
    result = []
    result.append(content)
    for i in content2:
        result.append(i)

    # cache.delete('cjjc_' + keyword)
    # cache.set('cjjc_' + keyword, json.dumps(result), 60 * 60)
    return result
# @_async
def kotobank_spider(keyword):
    keyword = quote(keyword)
    url = 'https://kotobank.jp/gs/?q=' + keyword

    browser = webdriver.Chrome()
    browser.get(url)
    page_text = browser.page_source
    soup = BeautifulSoup(page_text, 'lxml')
    try:
        content2 = soup.find_all('div',class_= "gsc-expansionArea")
    except Exception as e:
        print(e)
        result = ['查找为空']
        # cache.delete('koto_' + keyword)
        # cache.set('koto_' + keyword, json.dumps(result), 60 * 60)

    result = []
    for i in content2:
        result.append(i)
    # cache.delete('koto_' + keyword)
    # cache.set('koto_' + keyword, json.dumps(result), 60 * 60)
    return result
# @_async
def dictionary_spider(keyword):
    keyword = quote(keyword)
    url = 'https://dictionary.goo.ne.jp/srch/kanji/' + keyword + '/m0u/'
    browser = webdriver.Chrome()
    browser.get(url)
    page_text = browser.page_source
    browser.close()
    soup = BeautifulSoup(page_text,'lxml')
    try:
        content2 = soup.find_all('div', class_="search-list")
    except Exception as e:
        print(e)
        result = '查找为空'
        # cache.delete('dict_' + keyword)
        # cache.set('dict_' + keyword, json.dumps(result), 60 * 60)
    result = ['''
    <head>
      <base target="_blank" />
      <base href="https://dictionary.goo.ne.jp/srch/kanji/">
</head>''']
    for i in content2:
        if 'NR-ad' in i.text:
            print(i,'****')
        else:
            result.append(i)
    # cache.delete('dict_' + keyword)
    # cache.set('dict_' + keyword, json.dumps(result), 60 * 60)
    return result

def mian_(key):
    cjjc_spider(key)
    dictionary_spider(key)    # cjjc_spider(key),
    kotobank_spider(key)

if __name__ == '__main__':
    # print(dictionary_spider('ちんぽ'))
    print(cjjc_spider('营业'))
    # mian_('ちんぽ')

