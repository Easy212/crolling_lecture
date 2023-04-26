#셀레니움 키보드 입력 실습

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.naver.com')

elem = driver.find_element(By.CSS_SELECTOR, '#query')

elem.send_keys('코로나') #검색어 입력
elem.send_keys(Keys.RETURN) #엔터키입력
time.sleep(300) #종료시간