import time

class shift:

    def __init__(self, positionNumber, position, category, \
             lastName, firstName, startTime, endTime):
        self.positionNumber = positionNumber
        self.position = position
        if self.position == "Training":
            self.category = "T"
        else:
            self.category = category
        self.lastName = lastName
        self.firstName = firstName
        self.startTime = time.strptime(startTime,  "%I:%M %p")
        self.startTimeStr = str(self.startTime.tm_hour) + ":" + str(self.startTime.tm_min).zfill(2)
        self.endTime = time.strptime(endTime, "%I:%M %p")
        self.endTimeStr = str(self.endTime.tm_hour) + ":" + str(self.endTime.tm_min).zfill(2)

    # Returns a string representation of the shift
    def toString(self):
        # If position is Training, set the output position number to "00"
        if self.positionNumber == 0:
            positionNumberStr = "00"
        # Otherwise, just convert the position number to a string
        else:
            positionNumberStr = str(self.positionNumber)

        return positionNumberStr + self.category + ", " + \
               self.firstName + " " + self.lastName + ", " + \
               self.startTimeStr + "-" + self.endTimeStr