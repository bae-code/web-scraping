import json
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from bs4 import BeautifulSoup
import os
movie_list = []
title_list = []
a= 1


for i in range(1990,2007):

    url =f'https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&openStartDt={i}&openEndDt={i}&itemPerPage=100'
    res = requests.get(url)
    text = res.text

    d = json.loads(text)

    for i in d['movieListResult']['movieList']:
        b = i['movieNm'].replace(' ','')
        title = ''.join(filter(str.isalnum, b))
        genre =i['repGenreNm']
        openDt = i['openDt'][:4]
        movie_list.append([a,openDt,title,genre])
        title_list.append(title)
        a+=1
        
########## title_list 제목 리스트를 전달받는다 #############################
##########################################################################

driver = webdriver.Chrome("chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl" )
for x , i in enumerate(title_list):
    vali = os.path.isfile("{i}.jpg")
    if vali != True:
        a = ''.join(filter(str.isalnum, i))
        elem = driver.find_element_by_name("q")
        elem.send_keys(f'영화 {a} 포스터')
        elem.send_keys(Keys.RETURN)

        driver.find_element_by_name("q").clear()
        driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
        imgURL=driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")

        
        urllib.request.urlretrieve(imgURL, f"{i}.jpg")
        time.sleep(2)
    print(x)
    
  ######################### 중간중간 자주 끊겨서 x 를 출력해주고 index값을 받아와서 추가작업에 혼선이 없게 작업했다######################
  #################################################################################################################################
