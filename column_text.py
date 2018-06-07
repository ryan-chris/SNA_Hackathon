from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from selenium import webdriver
from time import sleep


def in_spider_parameter(driver1):
    title = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#c_right_view > dl > dt'))).text
    org = driver1.find_element_by_css_selector('#c_left_view > dl > dd:nth-child(2)').text
    requestVar = driver1.find_element_by_css_selector('#c_right_view > div:nth-child(6) > table').text
    responseVar = driver1.find_element_by_css_selector('#c_right_view > div:nth-child(8) > table').text

    return (title, org, requestVar, responseVar)


def web_spider_parameter(link_list):

    driver = webdriver.Chrome('/Users/interx/Desktop/Hackathon/chromedriver')

    total = []
    count = 1

    for url in link_list:
        print('%s Count', count)

        driver.get(url)
        print(url)
        sleep(2)

        condition = [elem.text for elem in driver.find_elements_by_css_selector('.dataset-items > div.detail-wrapper.clearfix.multiple > div.detail-viewer > div.detail-option-info > div#functions > ul > li > a')]
        print(condition, len(condition))

        if len(condition) == 1:
            #print('if')
            driver.find_element_by_xpath('//*[@id="functions"]/ul/li/a').click()
            sleep(2)

            total.append(in_spider_parameter(driver))


        elif len(condition) > 1:
            for i in range(len(condition)):
                #print('elif')
                driver.find_element_by_xpath('//*[@id="functions"]/ul/li[' + str(i + 1) + ']/a').click()
                sleep(2)

                total.append(in_spider_parameter(driver))
                driver.execute_script("window.history.go(-1)")
                sleep(2)

        driver.execute_script("window.history.go(-1)")
        sleep(2)
        count += 1


    driver.close()
    driver.quit()

    return total

'''
# test
url = 'https://www.data.go.kr/dataset/15000099/openapi.do'

driver = webdriver.Chrome('/Users/interx/Desktop/Hackathon/chromedriver')  # path of chromedriver
driver.get(url)
sleep(2)

print(len([elem.text for elem in driver.find_elements_by_css_selector('.dataset-items > div.detail-wrapper.clearfix.multiple > div.detail-viewer > div.detail-option-info > div#functions > ul > li > a')]))

#print(driver.find_element_by_css_selector('#c_right_view > dl > dt').text)

#print(driver.find_element_by_css_selector('#c_left_view > dl > dd:nth-child(2)').text)

#print(driver.find_element_by_css_selector('#c_right_view > div:nth-child(6) > table').text)

#print(driver.find_element_by_css_selector('#c_right_view > div:nth-child(8) > table').text)

driver.close()
driver.quit()

'''

if __name__=='__main__':
    df = pd.read_csv('/Users/interx/Desktop/Hackathon/api_list_data.csv',
                     names=['서비스명', '열람수', '활용신청건수', '제공기관', '카테고리', 'url'])
    #print(df.shape)
    link_list = df['url'].tolist()
    print(link_list)

    test = web_spider_parameter(link_list[:1300])
    print(test)
    

'''
//*[@id="functions"]/ul/li[1]/a
//*[@id="functions"]/ul/li[2]/a
//*[@id="functions"]/ul/li[3]/a
//*[@id="functions"]/ul/li[4]/a
'''