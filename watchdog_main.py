from LocationsList import LocationsList
from FlatList import FlatList
import watchdog_scraper as scraper
import watchdog_attr as pricePerMeter


locList = LocationsList()
flatList = FlatList()

locList.addNewLocation('Sovova 503/3, Praha 8', 2, False)
locList.addNewLocation('Siemensova 1, Praha 13', 8, False)
# locList.addNewLocation('nám. Winstona Churchilla 1938/4, 130 67 Praha 3', 2, False)
locList.addNewLocation('park', 6, True)

locList.setMaxTravelTime(75 * 60)

#testAddr = ['Praha 2', 'Mládí, Praha 5 - Stodůlky', 'Augustinova, Praha 4 - Chodov', 'Koněvova, Praha 3 - Žižkov', 'Sinkulova, Praha 4 - Podolí', 'Bulovka, Praha 8 - Libeň', 'Libeňský ostrov, Praha 8 - Libeň']
page_source = scraper.getHTML('https://www.sreality.cz/hledani/prodej/byty/praha?velikost=2%2B1,3%2Bkk,3%2B1&bez-aukce=1', True, 'page-layout')
inputAddr = scraper.getItemsList(page_source, 'span', 'locality ng-binding', 2)

[perMeterScore, sqMetersList, priceList] = pricePerMeter.calculatPricePerMeter(page_source, 2)

flatList.flatsAddr =  inputAddr
flatList.setImportantLocations(locList)

flatList.calculateScores()


flatList.printInScoreOrder()
# flatList.sortByScore()

# print(flatList.flatsAddr)
# print(flatList.scores)

# flatList.prettyPrint()

flatList.addScoreParameter(150000, 1, perMeterScore)
print("After price per meter")
flatList.printInScoreOrder()
