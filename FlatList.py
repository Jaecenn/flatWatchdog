from LocationsList import LocationsList
import sys
import time
import google_directions as maps

class Flat():

    def __init__(self, flatAddr, importantLocLength):
        self.totalScore = 0
        self.scores = []
        self.values = []
        self.flatAddr = flatAddr
        self.distSubscores = [0] * importantLocLength
        self.distSubvalues = [0] * importantLocLength
        self.url = "unknown URL"

    def __str__(self):
        return self.flatAddr + "; " + str(round(self.totalScore)) + "; " + str(self.scores) + "; " +  str(self.distSubvalues) + "; " +  str(self.values) + "; " + self.url

    def calculateTotalScore(self):
        self.totalScore = 0
        for parameterId in range(0, len(self.scores)):
            self.totalScore = self.totalScore + self.scores[parameterId]

class FlatList():

    def __init__(self):
        self.flatsAddr = []
        self.listOfFlats = []
        self.isLocationsInit = False
        # self.mainScores = []
        # self.totalScore = []

    def sortByScore(self):
        # print(len(self.flatsAddr))        

        for flatId in range(0, len(self.flatsAddr)):
            self.listOfFlats[flatId].calculateTotalScore()

        self.listOfFlats.sort(key=lambda x: x.totalScore, reverse=True)
        # self.totalScore, self.scores, self.flatsAddr, self.subscores, self.subvalues = zip(*sorted(zip(self.totalScore, self.scores, self.flatsAddr, self.subscores, self.subvalues),self.totalScore, reverse=True))
        # print(len(self.flatsAddr))     

    def setImportantLocations(self, locationsList):
        self.locationList = locationsList

    def calculateScores(self):

        self.isLocationsInit = True

        width = self.locationList.getLength()
        height = len(self.flatsAddr)

        if (width == 0 or height == 0):
            print("No address of apartment or no imporatant location given")
            sys.exit(-1)

        self.scores = [0] * height
        self.subscores = [[0 for x in range(width)] for y in range(height)]
        self.subvalues = [[0 for x in range(width)] for y in range(height)]

        for flatId in range(0, len(self.flatsAddr)):

            tempFlat = Flat(self.flatsAddr[flatId], self.locationList.getLength())
            tempFlat.scores.append(0)


            for loc in range(0, self.locationList.getLength()):
                time.sleep(0.1)

                # Equation: y = (4500 - x) / (4500 /30)   where maxTravel = 4500, weight = 30 (i.e. 30- x/150 =y)
                if (self.locationList.getDynamicFlag(loc) == True):
                    locAddress = self.locationList.getAddress(loc) + " blízko " + self.flatsAddr[flatId]
                else:
                    locAddress = self.locationList.getAddress(loc)

                
                value = maps.getTravelTime(True,  self.flatsAddr[flatId], locAddress )
                print(locAddress)
                print(str(value))
                print("MaxTravelTime" + str(self.locationList.getMaxTravelTime()))
                if (value > self.locationList.getMaxTravelTime()):
                    score = 0
                else:
                    score = (self.locationList.getMaxTravelTime() - value )  / (self.locationList.getMaxTravelTime() / self.locationList.getWeight(loc))

                # self.scores[flatId] = self.scores[flatId] + score
                # self.subscores[flatId][loc] = score
                # self.subvalues[flatId][loc] = value / 60
                tempFlat.scores[0] = tempFlat.scores[0] + score
                tempFlat.distSubscores[loc] = score
                tempFlat.distSubvalues[loc] = value / 60

            self.listOfFlats.append(tempFlat)        

    def addScoreParameter(self, maxValue, weight, scoreVector):

        if len(scoreVector) != len(self.flatsAddr):
            print("ER: Extra parameter series has incorrect length")
            sys.exit(-1)

        if self.isLocationsInit == False:
            print("ER: Calculation of distances must be done before any other parameter is added")
            sys.exit(-1)

        for flatId in range(0, len(self.flatsAddr)):
            value = scoreVector[flatId]

            if (value == 0):
                score = -2000
            elif (value > maxValue):
                score = 0
            else:
                score = (maxValue - value )  / (maxValue / (weight * 100))
                        
            self.listOfFlats[flatId].scores.append(score)  
            self.listOfFlats[flatId].values.append(value)  
                 

    def addURLs(self, urlList):

        if len(urlList) != len(self.flatsAddr):
            print("ER: URL list has incorrect length")
            sys.exit(-1)

        for flatId in range(0, len(self.flatsAddr)):
            self.listOfFlats[flatId].url = urlList[flatId]

    def prettyPrint(self):
        for flatId in range(0, len(self.flatsAddr)):
            print("**** " + self.flatsAddr[flatId] + ": " + str(self.scores[flatId]))
            print("(" + str(self.locationList.listOfLocations) + " )")
            print("(" + str(self.subvalues[flatId]) + " )")
            print("(" + str(self.subscores[flatId]) + " )")
            print("")


    def printInScoreOrder(self):

        self.sortByScore()

        with open("testResults.csv", "w") as outFile:
            print("Address, Total Score, Sub-Scores, URL")
            outFile.write("Address; Total Score; score [distances]; score [values]; distance1; distance2; distance3; kc / m^2; URL\n")

            for flatId in range(0, len(self.flatsAddr)):
                outFile.write(str(self.listOfFlats[flatId])+"\n")
                print(str(self.listOfFlats[flatId]))

            
            # sys.stdout.write("** " + self.flatsAddr[flatId] + " ** : " + str(round(self.totalScore[flatId])))
            # sys.stdout.write(", ")
            # for parameterId in range(0, len(self.mainScores)):
            #     sys.stdout.write(str(round(self.mainScores[parameterId][0][flatId])))
            #     sys.stdout.write(", ")
            # sys.stdout.write("\n")