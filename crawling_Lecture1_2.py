import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.naver?query=파이썬'
response = requests.get(url) #통신이 잘되었으면 200으로뜸

if response.status_code == 200: #통신이 잘되었으면(200이떴으면) 실행
    html = response.text
    soup = BeautifulSoup(html, 'html.parser') 

    ul= soup.select_one('ul.basic1') # ul태그중 basic1 클래스를 가진 녀석을 뽑아오는 선택자
    #print(ul) # text만 뽑아오려면 get_text() 함수사용

    titles = ul.select('li > dl > dt > a')
    print(titles)
    for title in titles :
        print(title.get_text())
else :
    print(response.status_code)