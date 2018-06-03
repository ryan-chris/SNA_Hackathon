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

    driver = webdriver.Chrome('/Users/Chris/Downloads/chromedriver')
    page = 1
    url = 'https://www.data.go.kr/search/index.do'
    driver.get(url)

    data_list = []

    driver.find_element_by_xpath('//*[@id="openapiTab"]/a/span').click()

    try:
        while page < max_page:
            print('%s page', page)

            sleep(3)

            dataitems = driver.find_elements_by_css_selector('.data-item')
            for item in dataitems:
                temp = (item.find_element_by_css_selector('.data-title>a').text,
                        item.find_elements_by_css_selector('.data-title>span')[0].text,
                        item.find_elements_by_css_selector('.data-title>span')[1].text,
                        item.find_elements_by_css_selector('.data-meta>span')[1].text,
                        item.find_element_by_css_selector('span').text,
                        item.find_element_by_css_selector('.data-title>a').get_attribute('href'))

                data_list.append(temp)

            # move to next page
            page += 1
            sleep(1)

            if page == 11:
                driver.find_element_by_xpath('//*[@id="search_more_openapi"]/div/ul/li[13]/a/i').click()
            elif page % 10 == 0 or page % 10 == 1:
                driver.find_element_by_xpath('//*[@id="search_more_openapi"]/div/ul/li['+ str((page % 10)+12) +']/a').click()
            else:
                driver.find_element_by_xpath('//*[@id="search_more_openapi"]/div/ul/li['+ str((page % 10)+2) +']/a').click()

            sleep(1)

    finally:
        driver.close()
        driver.quit()

    return data_list


def web_spider_inpage(link_list):
    '''
    crawler for detail corresponding to the web_spider_outpage function.
    :param link_list: each url(detail page)
    :return: each attributes list in page
    '''

    driver = webdriver.Chrome('/Users/interx/Desktop/Hackathon/chromedriver')

    data_list = []

    try:
        for link in link_list:
            print(link)
            driver.get(link)
            sleep(1)

            dataitems = driver.find_elements_by_css_selector('.content')
            for item in dataitems:
                temp = (item.find_element_by_css_selector('.dataset-detail > div > h1 > div.title').text,
                        item.find_element_by_css_selector('.dataset-detail > div > h4').text,
                        item.find_element_by_css_selector('.dataset-items > div.detail-wrapper.clearfix.multiple > div.detail-viewer > div:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2)').text,
                        item.find_element_by_css_selector('.dataset-items > div.detail-wrapper.clearfix.multiple > div.detail-viewer > div:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(4)').text,
                        item.find_element_by_css_selector('.dataset-items > div.detail-wrapper.clearfix.multiple > div.detail-viewer > div:nth-child(1) > table > tbody > tr:nth-child(8) > td:nth-child(2)').text,
                        item.find_element_by_css_selector('.dataset-items > div.detail-wrapper.clearfix.multiple > div.detail-viewer > div:nth-child(1) > table > tbody > tr:nth-child(8) > td:nth-child(4)').text,
                        [elem.text for elem in item.find_elements_by_css_selector('.dataset-items > div.detail-wrapper.clearfix.multiple > div.detail-viewer > div.detail-option-info > div#functions > ul > li > a')])

                data_list.append(temp)

    finally:
            driver.close()
            driver.quit()

    return data_list


def outpage_storeCSV(crawl_data_list):
    csvFile = open("../api_list_data.csv", "wt", encoding='utf-8', newline='')
    writer = csv.writer(csvFile)

    try:
        for line in crawl_data_list:
            name = line[0]
            view = line[1].split(':')[1].strip().replace(',', '')
            num_application = line[2].split(':')[1].strip().replace(',', '')
            organization = line[3].split(':')[1].strip()
            category = line[4]
            url = line[5]
            writer.writerow([name, int(view), int(num_application), organization, category, url])

    finally:
        csvFile.close()


def inpage_storeCSV(crawl_data_list):
<<<<<<< HEAD
    csvFile = open("../api_detail_data.csv", "wt", encoding='utf-8', newline='')
=======
    csvFile = open("../api_detail_data.csv", encoding='utf-8', newline='')
>>>>>>> 067bc0aa32293f86dcbb4401a12f54c3fdbeacac
    writer = csv.writer(csvFile)

    try:
        for line in crawl_data_list:
            service = line[0]
            description = line[1]
            register_date = line[2]
            fixed_date = line[3]
            team = line[4]
            contact = line[5]
            addin = line[6]
            writer.writerow([service, description, register_date, fixed_date, team, contact, addin])

    finally:
        csvFile.close()


def main():

    # out-page result
<<<<<<< HEAD
    outresult = web_spider_outpage(254)

    # Creating a links list
    links = [link[-1] for link in outresult]

    # Store result to CSV file
    outpage_storeCSV(outresult)
=======
    outresult = web_spider_outpage(25)
    outpage_storeCSV(outresult)

    # collecting all links
    links = web_spider_detail_link(254)
>>>>>>> 067bc0aa32293f86dcbb4401a12f54c3fdbeacac

    # in-page result
    inresult = web_spider_inpage(links)

    # Store result to CSV file
    inpage_storeCSV(inresult)


if __name__=='__main__':

    main()

    '''
    # test01: out-page
    datascrap = web_spider_outpage(2) # scrapping website
    print(datascrap)

    outpage_storeCSV(datascrap)

    # test02: creating a link list
    links = web_spider_detail_link(2)
    print(links, len(links))


    # test03: in-page
    test_link = ['https://www.data.go.kr/dataset/15000124/openapi.do', 'https://www.data.go.kr/dataset/15000099/openapi.do',
                 'https://www.data.go.kr/dataset/15012005/openapi.do', 'https://www.data.go.kr/dataset/15000496/openapi.do',
                 'https://www.data.go.kr/dataset/15003169/openapi.do', 'https://www.data.go.kr/dataset/15000268/openapi.do',
                 'https://www.data.go.kr/dataset/15000515/openapi.do', 'https://www.data.go.kr/dataset/15000581/openapi.do',
                 'https://www.data.go.kr/dataset/15012420/openapi.do', 'https://www.data.go.kr/dataset/15000495/openapi.do']

    datascrap = web_spider_inpage(test_link)  # scrapping website
    print(datascrap)
    inpage_storeCSV(datascrap)
    '''
