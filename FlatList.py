from LocationsList import LocationsList
import sys
import time
import google_directions as maps


class FlatList():

    def __init__(self):
        self.flatsAddr = []

    def sortByScore(self):
        self.scores, self.flatsAddr, self.subscores, self.subvalues = zip(*sorted(zip(self.scores, self.flatsAddr, self.subscores, self.subvalues)))

    def setImportantLocations(self, locationsList):
        self.locationList = locationsList

    def calculateScores(self):

        width = self.locationList.getLength()
        height = len(self.flatsAddr)

        if (width == 0 or height == 0):
            print("No address of apartment or no imporatant location given")
            sys.exit(-1)

        self.scores = [0] * height
        self.subscores = [[0 for x in range(width)] for y in range(height)]
        self.subvalues = [[0 for x in range(width)] for y in range(height)]

        for flatId in range(0, len(self.flatsAddr)):
            for loc in range(0, self.locationList.getLength()):
                time.sleep(0.1)

                # Equation: y = (4500 - x) / (4500 /30)   where maxTravel = 4500, weight = 30 (i.e. 30- x/150 =y)
                if (self.locationList.getDynamicFlag(loc) == True):
                    locAddress = self.locationList.getAddress(loc) + " blízko " + self.flatsAddr[flatId]
                else:
                    locAddress = self.locationList.getAddress(loc)

                print(locAddress)
                value = maps.getTravelTime(True,  self.flatsAddr[flatId], locAddress )

                if (value > self.locationList.getMaxTravelTime()):
                    score = 0
                else:
                    score = (self.locationList.getMaxTravelTime() - value )  / (self.locationList.getMaxTravelTime() / self.locationList.getWeight(loc))

                self.scores[flatId] = self.scores[flatId] + score
                self.subscores[flatId][loc] = score
                self.subvalues[flatId][loc] = value / 60


                print(score)

    def prettyPrint(self):
        for flatId in range(0, len(self.flatsAddr)):
            print("**** " + self.flatsAddr[flatId] + ": " + str(self.scores[flatId]))
            print("(" + str(self.locationList.listOfLocations) + " )")
            print("(" + str(self.subvalues[flatId]) + " )")
            print("(" + str(self.subscores[flatId]) + " )")
            print("")
