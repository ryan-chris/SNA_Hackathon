from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import sys

driver = webdriver.Chrome('/Users/Chris/Downloads/chromedriver')

url = 'https://www.data.go.kr/search/index.do'
driver.get(url)

driver.find_element_by_xpath('//*[@id="openapiTab"]/a/span').click()
sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

'''
test = soup.findAll('div', attrs={'class': 'data-title'})
for elem in test:
    print(elem.text.strip())
'''

dataitems = driver.find_elements_by_css_selector('.data-item')
for item in dataitems:
    print('타이틀', item.find_element_by_css_selector('.data-title>a').text)
    print('조회수', item.find_elements_by_css_selector('.data-title>span')[0].text)
    print('활용신청건수', item.find_elements_by_css_selector('.data-title>span')[1].text)
    print('기관', item.find_elements_by_css_selector('.data-meta>span')[1].text)
    print('카테고리', item.find_element_by_css_selector('span').text)

driver.close()
driver.quit()
sys.exit()

