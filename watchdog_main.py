from LocationsList import LocationsList
from FlatList import FlatList
import watchdog_scraper as scraper
import watchdog_attr as pricePerMeter
import sys

locList = LocationsList()


locList.addNewLocation('Siemensova 1, Praha 13', 9, False)
locList.addNewLocation('Sovova 503/3, Praha 8', 2, False)
locList.setMaxTravelTime(60 * 60)

# locList.addNewLocation('nám. Winstona Churchilla 1938/4, 130 67 Praha 3', 2, False)
#locList.addNewLocation('park', 8, True)



#testAddr = ['Praha 2', 'Mládí, Praha 5 - Stodůlky', 'Augustinova, Praha 4 - Chodov', 'Koněvova, Praha 3 - Žižkov', 'Sinkulova, Praha 4 - Podolí', 'Bulovka, Praha 8 - Libeň', 'Libeňský ostrov, Praha 8 - Libeň']
#page_source = scraper.getHTML('https://www.sreality.cz/hledani/prodej/byty/praha?velikost=2%2B1,3%2Bkk,3%2B1&bez-aukce=1', True, 'page-layout')

with open("testResults.csv", "a") as outFile:    
    outFile.write("Address; Total Score; score [distances]; score [values]; distance1; distance2; kc / m^2; URL\n")

maxItems = 20
maxPages = 30
minPage = 5

for x in range(minPage,maxPages + 1):
    flatList = FlatList()
    pageNum = x
    page_source = scraper.getHTML('https://www.sreality.cz/hledani/prodej/byty/praha?velikost=2%2B1,3%2Bkk,3%2B1&strana=' + str(pageNum) +'&bez-aukce=1', True, 'page-layout')

    inputAddr = scraper.getItemsList(page_source, 'span', 'locality ng-binding', maxItems)
    [perMeterScore, sqMetersList, priceList] = pricePerMeter.calculatPricePerMeter(page_source, maxItems)

    flatList.flatsAddr =  inputAddr
    flatList.setImportantLocations(locList)

    flatList.calculateScores()
    listURL = scraper.getURLS(page_source,maxItems)
    flatList.addURLs(listURL)

    flatList.addScoreParameter(110000, 1, perMeterScore)
    print("After price per meter")
    flatList.printInScoreOrder()
