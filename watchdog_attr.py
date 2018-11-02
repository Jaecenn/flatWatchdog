import watchdog_scraper as scraper
import re
import stringParsingUtils as parseUtils

def calculateScore(price, sqMeters):    
    return round(int(price)/int(sqMeters)/1000 - 200)


page_source = scraper.getHTML('https://www.sreality.cz/hledani/prodej/byty/praha?velikost=2%2B1,3%2Bkk,3%2B1&bez-aukce=1', True, 'page-layout')

flatList = scraper.getItemsList(page_source, 'span', 'locality ng-binding')
print(flatList)

sqMetersList = scraper.getItemsList(page_source, 'span', 'name ng-binding')
sqMetersList = sqMetersList[3:(len(sqMetersList) -3)]
sqMetersList = [parseUtils.getSqMetersValue(item) for item in sqMetersList]

priceList = scraper.getItemsList(page_source, 'span', 'price ng-scope')
priceList =  [parseUtils.getPriceValue(item) for item in priceList]

perMeterScore = [ calculateScore(price, sqMetersList[ind]) for ind, price in enumerate(priceList)]


print(sqMetersList)
print(priceList)
print(perMeterScore)




