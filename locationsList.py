class LocationsList():

    def __init__(self):
        self.listOfLocations = []
        self.prioritySum = 0

    def addNewLocation(self, address, priority, dynamicAddress):

        if (priority > 10):
            print("Priority higher than 10 is not allowed - value decreased to 10")
            priority = 10

        weight = self.calculateWeight(priority)

        for loc in self.listOfLocations:
            loc[1] = (loc[2] / self.prioritySum) * 100

        self.listOfLocations.append([address, weight, priority, dynamicAddress])


    def calculateWeight(self, priority):
        self.prioritySum += priority
        weight = (priority / self.prioritySum) * 100
        return weight

    def getAddress(self, id):
        return self.listOfLocations[id][0]

    def getWeight(self, id):
        return self.listOfLocations[id][1]

    def getLength(self):
        return len(self.listOfLocations)

    def getDynamicFlag(self, id):
        return self.listOfLocations[id][3]

    def setMaxTravelTime(self, travelMax):
        self.travelMax = travelMax

    def getMaxTravelTime(self):

        return self.travelMax