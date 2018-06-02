from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import sys

def web_spider_outpage(max_page):
    '''
    crawler for Open API list of data.go.kr
    :param max_page:
    :return: list
    '''

    driver = webdriver.Chrome('/Users/Chris/Downloads/chromedriver')
    page = 1
    url = 'https://www.data.go.kr/search/index.do'
    driver.get(url)

    data_list = []

    driver.find_element_by_xpath('//*[@id="openapiTab"]/a/span').click()

    while page < max_page:
        print('%s page', page)

        sleep(2)

        dataitems = driver.find_elements_by_css_selector('.data-item')
        for item in dataitems:
            temp = (item.find_element_by_css_selector('.data-title>a').text,
                    item.find_elements_by_css_selector('.data-title>span')[0].text,
                    item.find_elements_by_css_selector('.data-title>span')[1].text,
                    item.find_elements_by_css_selector('.data-meta>span')[1].text,
                    item.find_element_by_css_selector('span').text)

            data_list.append(temp)

        # move to next page
        page += 1
        sleep(3)
        driver.find_element_by_xpath('// *[ @ id = "search_more_openapi"] / div / ul / li[' + str(page+2) +'] / a').click()

    return data_list

def web_spider_inpage(max_page):
    '''
    crawler for detail of Open API list of data.go.kr
    :param max_page:
    :return:
    '''
    driver = webdriver.Chrome('/Users/Chris/Downloads/chromedriver')

    page = 1
    url = 'https://www.data.go.kr/search/index.do'
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="openapiTab"]/a/span').click()

    data_list = []
    while page < max_page:

        sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # openapi-list-wrapper > div:nth-child(1) > div.data-title > a
        links = soup.select(
            'div > div.data-title > a'
        )

        for link in links:
            print('https://www.data.go.kr' + link.get('href'))
            driver.get('https://www.data.go.kr' + link.get('href'))
            sleep(1)

            subdataitems = driver.find_elements_by_css_selector('.content')
            for item in subdataitems:
                temp = (item.find_element_by_css_selector('.dataset-detail>.detail-infos>.dataset-title>.title').text,
                        item.find_element_by_css_selector('h4.dataset-sub-title').text, # .dataset-detail>.detail-infos>.dataset-sub-title
                        item.find_element_by_css_selector('.functions>.api-functions>a').text)

                data_list.append(temp)

        # move to next page
        page += 1
        sleep(3)

    return data_list

if __name__=='__main__':

    datascrap = web_spider_outpage(10) # scrapping website
    print(datascrap)
