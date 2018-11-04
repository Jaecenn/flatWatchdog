import watchdog_scraper as scraper
import re
import stringParsingUtils as parseUtils

def calculateScore(price, sqMeters):    
    return round(int(price)/int(sqMeters))

def truncateResults(field, maxCount):
    if len(field) < maxCount:
        return field
    else: 
        field = field[0:maxCount]
        return field


def calculatPricePerMeter(page_source, maxCount=20):

    sqMetersList = scraper.getItemsList(page_source, 'span', 'name ng-binding')
    sqMetersList = sqMetersList[3:(len(sqMetersList) -3)]

    sqMetersList = truncateResults(sqMetersList, maxCount)

    sqMetersList = [parseUtils.getSqMetersValue(item) for item in sqMetersList]

    priceList = scraper.getItemsList(page_source, 'span', 'price ng-scope')
    priceList = truncateResults(priceList, maxCount)
    priceList =  [parseUtils.getPriceValue(item) for item in priceList]

    perMeterScore = [ calculateScore(price, sqMetersList[ind]) for ind, price in enumerate(priceList)]

    return [perMeterScore, sqMetersList, priceList]


# page_source = scraper.getHTML('https://www.sreality.cz/hledani/prodej/byty/praha?velikost=2%2B1,3%2Bkk,3%2B1&bez-aukce=1', True, 'page-layout')


# [perMeterScore, sqMetersList, priceList] = calculatPricePerMeter(page_source)

# print(sqMetersList)
# print(priceList)
# print(perMeterScore)




