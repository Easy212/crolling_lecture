#

import requests

from bs4 import BeautifulSoup

url = 'https://www.naver.com'
result = requests.get(url) #<Response[200]> 반환
html = result.text #html 내용반환
soup = BeautifulSoup(html, 'html.parser') #파싱(규격화) 'html.parser'는 정확한 규격으로 맞춰줌
print(soup)

