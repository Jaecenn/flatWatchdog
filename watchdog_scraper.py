#!/usr/bin/env python
from contextlib import closing
from selenium.webdriver import Chrome # pip install selenium

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def getHTML(url, bAwaitLoading, loadedIndicationID):

    if (bAwaitLoading == True):

        driver = webdriver.Chrome(executable_path='d://Python//watchdog//chromedriver.exe')

        driver.get(url)
        #button = browser.find_element_by_name('button')
        #button.click()
        # wait for the page to load
        WebDriverWait(driver, timeout=10).until(
            lambda x: x.find_element_by_id(loadedIndicationID))

        page_source = driver.page_source
        driver.quit()
    else:
        headers = {'User-Agent': 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko'}

        page = requests.get(url,
                            headers)

        page_source = page.text

    #print(page_source)
    return page_source


def getItemsList(page_source, type, type_tag):
    flatList = []
    html_soup = BeautifulSoup(page_source, 'html.parser')
    for taggedItem in html_soup.find_all(type, class_ = type_tag):
        flatList.append(taggedItem.text)
    print(flatList)
    return flatList

