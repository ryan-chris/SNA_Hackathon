from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

def web_spider_out(max_page):
    '''
    crawler for Open API list of data.go.kr
    :param max_page:
    :return: title, view, government, category
    '''

    driver = webdriver.Chrome('/Users/Chris/Downloads/chromedriver')
    page = 1
    url = 'https://www.data.go.kr/search/index.do'
    driver.get(url)

    titles_data = []
    gov_data = []
    category_data = []

    driver.find_element_by_xpath('//*[@id="openapiTab"]/a/span').click()

    while page < max_page:

        sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        titles = soup.findAll('div', attrs={'class': 'data-title'})
        gov = soup.findAll('div', attrs={'class': 'data-meta'})
        cat = soup.find_all('span', attrs={'class': 'category-filter visible-desktop'}, string=True)

        tempTitle = [elem.text.strip() for elem in titles]
        tempGov = [elem.text.strip() for elem in gov]
        tempCat = [elem.text.strip() for elem in cat]

        titles_data.append(tempTitle)
        gov_data.append(tempGov)
        category_data.append(tempCat)

        # move to next page
        page += 1
        sleep(7)

    return [titles_data, gov_data, category_data]



if __name__=='__main__':

    datascrap = web_spider_out(2) # scrapping website
    print(datascrap)

    for elem in datascrap[0]:
        for i in elem:
            i.split(' ')
            print(i)