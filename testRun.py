from LocationsList import LocationsList
from FlatList import FlatList

locList = LocationsList()
flatList = FlatList()

locList.addNewLocation('Sovova 503/3, Praha 8', 2, False)
locList.addNewLocation('Siemensova 1, Praha 13', 8, False)
locList.addNewLocation('nám. Winstona Churchilla 1938/4, 130 67 Praha 3', 2, False)
locList.addNewLocation('park', 6, True)

locList.setMaxTravelTime(75 * 60)

testAddr = ['Praha 2', 'Mládí, Praha 5 - Stodůlky', 'Augustinova, Praha 4 - Chodov', 'Koněvova, Praha 3 - Žižkov', 'Sinkulova, Praha 4 - Podolí', 'Bulovka, Praha 8 - Libeň', 'Libeňský ostrov, Praha 8 - Libeň']


flatList.flatsAddr =  testAddr
flatList.setImportantLocations(locList)

flatList.calculateScores()
flatList.sortByScore()

print(flatList.flatsAddr)
print(flatList.scores)

flatList.prettyPrint()
