
#셀레니움 마우스 클릭 실습

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.naver.com') #초기사이트 설정

#첫번째 실행할 마우스 클릭
driver.find_element(By.CSS_SELECTOR, '#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(8) > a').click()

time.sleep(5) #첫번째 실행할 마우스 클릭 후 5초뒤에

#첫번째 실행할 마우스 클릭 후 5초뒤에
driver.find_element(By.CSS_SELECTOR, '#menu > li:nth-child(3) > a').click()

time.sleep(200)
