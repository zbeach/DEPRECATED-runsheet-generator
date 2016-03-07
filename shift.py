import time

class shift:

    def __init__(self, positionName, category, lastName, firstName,
                 startTimeStr, endTimeStr, dateStr, description):
        self.position = self.positionNameToPosition(positionName)
        self.category = self.setCategory(category, positionName)
        self.lastName = lastName.replace("(Line Instructor)", "(L.I.)").replace(
            "(City Only Service)", "").replace("(Regular Service)", "")
        self.firstName = firstName
        self.startTime = self.timeStrToTime(startTimeStr)
        self.endTime = self.timeStrToTime(endTimeStr)
        self.date = self.dateStrToDate(dateStr)
        self.description = description
        self.lastOnRoute = False
        self.positionName = self.setFinalPositionName(positionName)

    # Convert position string to position number
    def positionNameToPosition(self, name):
        # Index of space character after the last digit of the position number
        #   in the position name
        INDEX_AFTER_POSITION_NUMBER = 2
        # Only return shift if position name is not "Mega Bus Connect"
        if name != "Mega Bus Connect":
            # If position name is "Training", set position number to 0
            if name == "Training":
                return 0;
            # Otherwise, set position number to first two characters of position
            #   name parsed to int
            else:
                return int(name[0:INDEX_AFTER_POSITION_NUMBER])

    # Set category
    def setCategory(self, category, positionName):
        # If non-route shift category, set category to first two characters of
        #   position name
        if category == '':
            LAST_CATEGORY_CHARACTER_INDEX = 2
            return positionName[0:LAST_CATEGORY_CHARACTER_INDEX]
        else: return category

    # Convert string representation of time to time
    def timeStrToTime(self, timeStr):
        return time.strptime(timeStr, "%I:%M %p")

    # Convert string representation of date to date
    def dateStrToDate(self, dateStr):
        return time.strptime(dateStr, "%m/%d/%Y")

    # Add category to position name
    def setFinalPositionName(self, positionName):

        # If this is a route shift, insert the category after the position
        #   number
        if len(self.category) == 1:
            positionName = positionName[0:2] + self.category + \
                           positionName[2:len(positionName)]
            return positionName.replace("(Full Service)", "")
        # If this is a non-route shifts, set position name to be the shift
        #   description
        else:
            return self.description

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