import time

class shift:

    def __init__(self, positionNumber, position, category, \
             lastName, firstName, startTime, endTime):
        self.positionNumber = positionNumber
        self.position = position
        if self.position == "Training":
            self.category = "Training"
        else:
            self.category = category
        self.lastName = lastName
        self.firstName = firstName
        self.startTime = startTime
        self.endTime = endTime

    def toString(self):
        return str(self.positionNumber) + self.category + ", " + \
               self.firstName + " " + self.lastName + ", " + self.startTime + " - " + self.endTime