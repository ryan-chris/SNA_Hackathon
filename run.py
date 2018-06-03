from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import csv
import requests

def web_spider_outpage(max_page):
    '''
    crawler for Open API list of data.go.kr
    :param max_page: the end of page
    :return: list
    '''

    driver = webdriver.Chrome('/Users/interx/Desktop/Hackathon/chromedriver')
    page = 1
    url = 'https://www.data.go.kr/search/index.do'
    driver.get(url)

    data_list = []

    driver.find_element_by_xpath('//*[@id="openapiTab"]/a/span').click()

    while page < max_page:

        try:
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

        finally:
            driver.close()
            driver.quit()

    return data_list


def web_spider_detail_link(max_page):
    '''
    crawler for detail of Open API list of data.go.kr
    :param max_page: the end of page
    :return: data list
    '''
    driver = webdriver.Chrome('/Users/interx/Desktop/Hackathon/chromedriver')

    page = 1
    url = 'https://www.data.go.kr/search/index.do'
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="openapiTab"]/a/span').click()

    link_list = []
    while page < max_page:

        try:
            sleep(2)

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # openapi-list-wrapper > div:nth-child(1) > div.data-title > a
            links = soup.select(
                'div > div.data-title > a'
            )

            for link in links:
                print('https://www.data.go.kr' + link.get('href'))
                link_url = 'https://www.data.go.kr' + link.get('href')
                link_list.append(link_url)

                sleep(0.5)

            # move to next page
            page += 1
            sleep(3)

        finally:
            driver.close()
            driver.quit()

    return link_list


def web_spider_inpage():


    return None


def outpage_storeCSV(crawl_data_list):
    csvFile = open("../api_list_data.csv", "wt", encoding='euc-kr')
    writer = csv.writer(csvFile)

    try:
        for line in crawl_data_list:
            name = line[0]
            view = line[1].split(':')[1].strip().replace(',', '')
            num_application = line[2].split(':')[1].strip().replace(',', '')
            organization = line[3].split(':')[1].strip()
            category = line[4]
            writer.writerow([name, int(view), int(num_application), organization, category])

    finally:
        csvFile.close()


if __name__=='__main__':

    # test01: out-page
    #datascrap = web_spider_outpage(2) # scrapping website
    #print(datascrap)

    #outpage_storeCSV(datascrap)

    # test02: in-page
    datascrap = web_spider_detail_link(2)  # scrapping website
    print(datascrap)
