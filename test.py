""" 셀레니움 실습 """

from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver.exe')

url = 'https://www.naver.com'
driver.get(url)

time.sleep(3) #로그인하고 바로메일로 가려고할때 통신이 느릴경우 로그인도안되고 넘어갈수 잇기때문

url = 'https://www.daum.net'
driver.get(url)

driver.quit()