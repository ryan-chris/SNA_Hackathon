import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver

def web_spider_meta(link_list):

    url = link_list
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    meta = soup.select('div.side > div > ul > li')
    meta_list = [elem.text.strip().replace(' ','').replace('\r','') for elem in meta]

    return meta_list

def web_spider_addlist(link_list):

    url = link_list
    driver = webdriver.Chrome('/Users/interx/Desktop/Hackathon/chromedriver')  # path of chromedriver
    driver.get(url)

    association_data_list = []
    items = driver.find_elements_by_css_selector('.content')
    try:
        for item in items:
            names = [elem.text for elem in
                     item.find_elements_by_css_selector('#relational-viewer > table > tbody > tr > td.title > a')]
            org = [elem2.text for elem2 in
                     item.find_elements_by_css_selector('#relational-viewer > table > tbody > tr > td.text-left')]
            number = [elem3.text for elem3 in
                     item.find_elements_by_css_selector('#relational-viewer > table > tbody > tr > td.text-right')]

            temp = [names, org, number]
            association_data_list.append(temp)

    finally:
        driver.close()
        driver.quit()

    return association_data_list

'''
url = 'https://www.data.go.kr/dataset/15000124/openapi.do'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'lxml')

test = soup.findAll('ul', class_='meta-items')
test_list = [elem.text.strip().replace(' ','').replace('\r','') for elem in test]

#print(test_list)

test2 = soup.select('div.side > div > ul > li')
test2_list = [tag.get_text().strip().replace(' ','') for tag in test2]

print(test2_list)

test3 = soup.select('.dataset-items > div.detail-wrapper.clearfix.multiple > div.detail-viewer > div.detail-option-info > div#functions > ul > li > a')
test3_list = [url.text for url in test3]

#print(test3_list)

test4 = soup.select('div#relational-viewer > table > tbody > tr > td.title > a')
test4_list = [asurl for asurl in test4]

#print(test4_list)


driver = webdriver.Chrome('/Users/interx/Desktop/Hackathon/chromedriver')  # path of chromedriver
driver.get(url)
items = driver.find_elements_by_css_selector('.content')
for item in items:
    test5 = [elem.text for elem in item.find_elements_by_css_selector('#relational-viewer > table > tbody > tr > td.title > a')]
    test6 = [elem2.text for elem2 in item.find_elements_by_css_selector('#relational-viewer > table > tbody > tr > td.text-left')]
    test7 = [elem3.text for elem3 in item.find_elements_by_css_selector('#relational-viewer > table > tbody > tr > td.text-right')]
print(test5, test6, test7)
'''

if __name__=='__main':
