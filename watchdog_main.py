from LocationsList import LocationsList
from FlatList import FlatList
import watchdog_scraper as scraper
import watchdog_attr as pricePerMeter
import sys
import time



# locList.addNewLocation('nám. Winstona Churchilla 1938/4, 130 67 Praha 3', 2, False)
#locList.addNewLocation('park', 8, True)
#testAddr = ['Praha 2', 'Mládí, Praha 5 - Stodůlky', 'Augustinova, Praha 4 - Chodov', 'Koněvova, Praha 3 - Žižkov', 'Sinkulova, Praha 4 - Podolí', 'Bulovka, Praha 8 - Libeň', 'Libeňský ostrov, Praha 8 - Libeň']
#page_source = scraper.getHTML('https://www.sreality.cz/hledani/prodej/byty/praha?velikost=2%2B1,3%2Bkk,3%2B1&bez-aukce=1', True, 'page-layout')

timestr = time.strftime("%Y%m%d-%H%M%S")
resultFile = "result_" + timestr + ".csv"

with open(resultFile, "a") as outFile:    
    outFile.write("Address; Total Score; score [distances]; score [values]; distance1; distance2; distance to park; kc / m^2; URL\n")

maxItems = 20
maxPages = 5
minPage = 1

propertyType = "barak"

if propertyType == "pozemek":
    maxTravelTime = 100
    maxSqMeterPrice = 7000
    prefix = 'https://www.sreality.cz/hledani/prodej/domy/rodinne-domy,projekty-na-klic/praha,stredocesky-kraj?velikost=3-pokoje,4-pokoje,5-a-vice&stav=dobry-stav,velmi-dobry-stav,ve-vystavbe,developerske-projekty,novostavby&cena-od=0&cena-do=9000000&strana='
    postfix = '&bez-aukce=1'

if propertyType == "barak":
    maxTravelTime = 100
    maxSqMeterPrice = 110000
    prefix = 'https://www.sreality.cz/hledani/prodej/domy/rodinne-domy,projekty-na-klic/praha,stredocesky-kraj?velikost=3-pokoje,4-pokoje,5-a-vice&stav=dobry-stav,velmi-dobry-stav,ve-vystavbe,developerske-projekty,novostavby&cena-od=0&cena-do=9000000&strana='
    postfix = '&bez-aukce=1'
    
    locList = LocationsList()
    locList.addNewLocation('Siemensova 1, Praha 13', 8, False)
    locList.addNewLocation('Sovova 503/3, Praha 8', 1, False)
    locList.addNewLocation('park', 1, True)
    locList.setMaxTravelTime(maxTravelTime * 60)


if propertyType == "byt":
    maxTravelTime = 60
    maxSqMeterPrice = 110000
    prefix = 'https://www.sreality.cz/hledani/prodej/byty/praha?velikost=3%2Bkk,3%2B1,4%2Bkk,4%2B1&cena-od=0&cena-do=9000000&strana='
    postfix = '&bez-aukce=1'

if propertyType == "byt_pronajem":
    maxTravelTime = 60
    maxSqMeterPrice = 500
    prefix = 'https://www.sreality.cz/hledani/pronajem/byty/praha?navic=balkon,lodzie,terasa&velikost=3%2Bkk,3%2B1,2%2Bkk,2%2B1,4%2Bkk,4%2B1&cena-od=0&cena-do=24000&strana='
    postfix = ''

locList = LocationsList()
locList.addNewLocation('Siemensova 1, Praha 13', 5, False)
locList.addNewLocation('Sovova 503/3, Praha 8', 3, False)
locList.addNewLocation('park', 8, True)
locList.setMaxTravelTime(maxTravelTime * 60)

for x in range(minPage,maxPages + 1):
    flatList = FlatList()
    pageNum = x
#    page_source = scraper.getHTML('https://www.sreality.cz/hledani/prodej/byty/praha?velikost=2%2B1,3%2Bkk,3%2B1&strana=' + str(pageNum) +'&bez-aukce=1', True, 'page-layout')
#    page_source = scraper.getHTML('https://www.sreality.cz/hledani/prodej/byty/praha?velikost=3%2Bkk,3%2B1,4%2Bkk,4%2B1&cena-od=0&cena-do=9000000&strana=' + str(pageNum) +'&bez-aukce=1', True, 'page-layout')    
    page_source = scraper.getHTML(prefix + str(pageNum) + postfix, True, 'page-layout')
    inputAddr = scraper.getItemsList(page_source, 'span', 'locality ng-binding', maxItems)
    [perMeterScore, sqMetersList, priceList] = pricePerMeter.calculatPricePerMeter(page_source, maxItems)

    flatList.flatsAddr =  inputAddr
    flatList.setImportantLocations(locList)

    flatList.calculateScores()
    listURL = scraper.getURLS(page_source,maxItems)
    flatList.addURLs(listURL)

    flatList.addScoreParameter(maxSqMeterPrice, 1, perMeterScore)
    print("After price per meter")
    flatList.printInScoreOrder(resultFile)
