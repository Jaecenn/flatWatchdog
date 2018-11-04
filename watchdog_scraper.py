#!/usr/bin/env python
from contextlib import closing
#from selenium.webdriver import Chrome # pip install selenium

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def getHTML(url, bAwaitLoading, loadedIndicationID):

    if (bAwaitLoading == True):

        driver = webdriver.Chrome(executable_path='c://Program Files (x86)//Python//chromedriver.exe')
        #driver = webdriver.Chrome('d://Python//watchdog//chromedriver.exe')
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


def truncateResults(field, maxCount):
    if len(field) < maxCount:
        return field
    else: 
        field = field[0:maxCount]
        return field

def getItemsList(page_source, type, type_tag, maxCount=20):
    flatList = []
    html_soup = BeautifulSoup(page_source, 'html.parser')
    for taggedItem in html_soup.find_all(type, class_ = type_tag):
        flatList.append(taggedItem.text)
    #print(flatList)
    flatList = truncateResults(flatList, maxCount)
    return flatList

def getURLS(page_source, maxCount=20):
    flatList = []
    html_soup = BeautifulSoup(page_source, 'html.parser')
    for taggedItem in html_soup.find_all('a', href=True):
        if "Prodej bytu" in taggedItem.text:            
            flatList.append("https://www.sreality.cz" + taggedItem.attrs['href'])
    #print(flatList)
    flatList = truncateResults(flatList, maxCount)
    return flatList