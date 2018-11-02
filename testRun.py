from locationsList import locationsList

locList = locationsList()

locList.addNewLocation('Sovova 503/3, Praha 8', 3)
locList.addNewLocation('Bla', 6)
locList.addNewLocation('Gle, Praha 8', 1)
locList.addNewLocation('Hle, Praha 8', 11)

print(locList.getWeight(1))