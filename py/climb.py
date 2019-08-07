#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from requests_html import HTML
from selenium import webdriver
from bs4 import BeautifulSoup
import  requests
import json
import re
import time

temp = []

def star(url, index):
    driver = webdriver.PhantomJS(executable_path=r'/home/user/下載/phantomjs-2.1.1-linux-i686/bin/phantomjs')  # PhantomJs
    driver.get(url)
    time.sleep(3)
    pageSource = driver.page_source  # 取得網頁原始碼
    #print(pageSource)

    soup = BeautifulSoup(pageSource, "lxml")
    re = soup.find('div', class_='eea-preview-items').find_all('div', class_='photoAlbumEntry')
    
    for i in re:
        temp.append(str(index) + ":" + i.find('h2').text + "," + i.find('a')['href'] + ";")

def run():    
    for j in range(0, 500):
        print(j)
        star('http://crgis.rchss.sinica.edu.tw/temples#c1=Temple&b_start=' + str(j * 20), j)

    fi = open('./log.txt', 'w')
    fi.write(''.join(temp))
    fi.close()
    
    print(temp)

run()