import requests
from bs4 import BeautifulSoup

url = 'https://terms.naver.com/search.naver?query=파이썬'
response = requests.get(url) #통신이 잘되었으면 200으로뜸

if response.status_code == 200: #통신이 잘되었으면(200이떴으면) 실행
    html = response.text
    soup = BeautifulSoup(html, 'html.parser') 

    title = soup.select_one('#content > div:nth-child(3) > ul > li > div.info_area > div > strong > a') # select_one은 하나의 html요소를 찾는함수
    #print(title)
    print(title.get_text()) # text만 뽑아오려면 get_text() 함수사용
else :
    print(response.status_code)