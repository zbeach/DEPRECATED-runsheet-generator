import time

class shift:

    def __init__(self, positionName, category, lastName, firstName, startTimeStr, endTimeStr, dateStr, description):
        self.position = self.positionNameToPosition(positionName)
        self.category = category
        self.lastName = lastName
        self.firstName = firstName
        self.startTime = self.timeStrToTime(startTimeStr)
        self.endTime = self.timeStrToTime(endTimeStr)
        self.date = self.dateStrToDate(dateStr)
        self.description = description

    # Convert position string to position number
    def positionNameToPosition(self, name):
        # Index of space character after the last digit of the position number in the position name
        INDEX_AFTER_POSITION_NUMBER = 2
        # Only return shift if position name is not "Mega Bus Connect"
        if name != "Mega Bus Connect":
            # If position name is "Training", set position number to 0
            if name == "Training":
                return 0;
            # Otherwise, set position number to first two characters of position name parsed to int
            else:
                return int(name[0:INDEX_AFTER_POSITION_NUMBER])

    # Convert string representation of time to time
    def timeStrToTime(self, timeStr):
        return time.strptime(timeStr, "%I:%M %p")

    # Convert string representation of date to date
    def dateStrToDate(self, dateStr):
        return time.strptime(dateStr, "%m/%d/%Y")

    # Returns string representation of this shift instance
    def __str__(self):
        return str(self.position) + \
               self.category + \
               " - " + \
               self.firstName + \
               " " + \
               self.lastName + \
               " - " + \
               time.strftime("%I:%M %p", self.startTime)

'''
# Extracts position number from position name
def toPositionNumber(positionName):
    # Set position numbers
    INDEX_AFTER_END_OF_POSITION_NUMBER = 2
    if (positionName != "Training") and (positionName != ""):
        return int(positionName[:INDEX_AFTER_END_OF_POSITION_NUMBER])
    else:
        return 0





import time

class shift:

    lastOnRoute = None

    def __init__(self, positionNumber, position, category, \
             lastName, firstName, startTime, endTime, dateStr, description):
        self.positionNumber = positionNumber
        self.position = position
        self.position = self.position.replace(" (Full Service)", "")
        self.position = self.position.replace(" (City Only Service)", "")
        if self.position == "Training":
            self.category = "T"
            self.position = description
        else:
            self.category = category
        if (self.category != 'T'):
            INDEX = 2
            self.position = self.position[:INDEX] + self.category + self.position[INDEX:]
        self.lastName = lastName
        self.firstName = firstName
        self.startTime = time.strptime(startTime,  "%I:%M %p")
        self.startTimeStr = str(self.startTime.tm_hour) + ":" + str(self.startTime.tm_min).zfill(2)
        self.endTime = time.strptime(endTime, "%I:%M %p")
        self.endTimeStr = str(self.endTime.tm_hour) + ":" + str(self.endTime.tm_min).zfill(2)
        self.dateStr = dateStr

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
'''