import requests
from bs4 import BeautifulSoup
from openpyxl import workbook

#네이버 증권 사이트
url = 'https://finance.naver.com/'

#url 요청
response = requests.get(url)

#해당 url의 정보모두 텍스트로 저장
html = response.text

#html
soup = BeautifulSoup(html, 'html.parser') 

tbody = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular > table > tbody')

print(tbody)
price_list = tbody.select('td') #td에 해당하는것만

slist = tbody.select('a')

count = 0
for i in range(0,len(price_list),2) :
    temp = slist[count]

    print("종목이름:", temp.text, \
          "종목코드:", str(temp) [str(temp).find('code=')+5 : (str(temp).find('code=')+5)+6], \
          "현재가:", price_list[i].text, \
          "전일대비:", price_list[i+1].text )

    count += 1
#for i in slist:
    #print(  str(i) [str(i).find('code=')+5 : (str(i).find('code=')+5)+6]   ) #종목코드 위치 가져오기 (슬라이싱 기법 )
    #print(i.text)

