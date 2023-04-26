from selenium import webdriver
import time
from openpyxl import Workbook
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import warnings 


driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=8pSC6QgxFzI&t=593s")

driver.execute_script("window.scrollTo(0, 800)")
time.sleep(3)

last_height = driver.execute_script("return document.documentElement.scrollHeight")

# 스크롤을 2번 내리는 구문
#while True: # 끝까지 내릴때
for i in range(0,2): # 2번만 내리겠다.
    #스크롤을 내리고 
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    #댓글이 다 돌때 까지 기다리기위해 3 초 기다림
    time.sleep(3)

    #내린상태의 높이를 반환(new_height)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")

    # 다 내렸을때  더이상 스크롤이 안내려가니까 before과 높이가 같으니까 그말은 즉슨
    # 스크롤을 다 내렸다고 판단 할 수 있다
    # 그때 break 문으로 더이상 loop를 돌지 않는다
    if new_height == last_height: 
        break

    #내린상태의 높이값이 new_height 한테 있으니까 이걸 마지막 높이로 재정의
    last_height = new_height

time.sleep(5)

#=============================================================================== 여기까지 댓글이 다 렌더링 될때까지 기다림

html_source = driver.page_source #page_sourc = 
soup = BeautifulSoup(html_source, 'html.parser')



#div중에 id가 header-author인걸 찾고 id가 autor-text인걸 찾고, span부분
id_list = soup.select("#author-text > span") 
content_list = soup.select("#content-text")

print(len(id_list))
print(len(content_list))

id_list_zip = []
content_list_zip = []

for i in range(0, len(id_list)) : 
    id_list_zip.append(str(id_list[i].text).strip()) 
    content_list_zip.append(content_list[i].text)

sdict = {
    '작성자:' : id_list_zip,
    '댓글:' : content_list_zip
}

you_tube = pd.DataFrame(sdict)
you_tube.to_csv('youtube_result.csv')

#for i in content_list : 
#    print(i.text)
#    print('-------------------------------------')

#for i in id_list : 
#    print(str(i.text)).strip() # i는 bs4의 객체이기 떄문에 text 내장변수가 있다

#yt-formatted-string 요소 중에 id가 content-text인것들 찾기
#comment_list = soup.select("yt-formatted-string#content-text")

#print(comment_list)