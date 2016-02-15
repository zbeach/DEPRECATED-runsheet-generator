import csv
import shift

class sorter:

    def __init__(self, file):
        # Reader for csvfile
        self.reader = csv.reader(file, dialect=csv.excel)

    # Create shift objects from reader
    def createShifts(self, date):

        # Row containing column headers
        headersRow = next(self.reader)
        
        # Column indices in csvfile
        LAST_NAME_COLUMN = headersRow.index("Employee Last Name")
        FIRST_NAME_COLUMN = headersRow.index("Employee First Name")
        POSITION_COLUMN = headersRow.index("Position Name")
        CATEGORY_COLUMN = headersRow.index("Category")
        START_TIME_COLUMN = headersRow.index("Start Time")
        END_TIME_COLUMN = headersRow.index("End Time")
        DATE_COLUMN = headersRow.index("Date")
        DESCRIPTION_COLUMN = headersRow.index("Shift Description")

        # Shifts list
        shifts = []

        # Build shifts list
        for row in self.reader:
            # Filter by DATE_COLUMN
            if row[DATE_COLUMN] == date:
                # Filter by CATEGORY_COLUMNs that are route shift categories
                if row[POSITION_COLUMN] != "Operations Supervisor" and row[POSITION_COLUMN] != "Mega Bus Connect":
                    # Append new shift object to shifts list with fields from current row
                    shifts.append(shift.shift(row[POSITION_COLUMN], \
                                              row[CATEGORY_COLUMN], \
                                              row[LAST_NAME_COLUMN], \
                                              row[FIRST_NAME_COLUMN], \
                                              row[START_TIME_COLUMN], \
                                              row[END_TIME_COLUMN], \
                                              row[DATE_COLUMN], \
                                              row[DESCRIPTION_COLUMN]))
        return shifts

    # Sort shifts list
    def sort(self, shifts):
        # Sort by category
        shifts = self.sortByCategory(shifts)

        # Sort by starting hour within categories
        shifts = self.sortByStartHourWithinCategories(shifts)

        # Sort by position within starting hours
        shifts = self.sortByPositionWithinStartHour(shifts)

        return shifts

    # Sort shifts by category
    def sortByCategory(self, shifts):
        # Sort
        for i in range(len(shifts) - 1):
            for j in range(len(shifts) - 1):
                # If current shift's category is greater than or equal to previous shifts category, swap the shifts
                if shifts[j].category >= shifts[j+1].category:
                    temp = shifts[j+1]
                    shifts[j+1] = shifts[j]
                    shifts[j] = temp

        return shifts

    # Returns list of all categories
    def getCategories(self, shifts):
        # Categories list
        categories = []
        for i in range(0, len(shifts)):
            if shifts[i].category not in categories:
                categories.append(shifts[i].category)

        return categories

    # Sort shifts by starting hour within categories
    def sortByStartHourWithinCategories(self, shiftsIn):
        # List of shift categories
        categories = self.makeCategories(shiftsIn)
        # List of unique shift categories
        uniqueCategories = self.makeUniqueCategories(categories)

        shiftsOut = []
        # Sort by starting hour for each category
        for i in range(len(uniqueCategories)-1):
            # Set indices for category range
            startIndex = categories.index(uniqueCategories[i])
            endIndex = categories.index(uniqueCategories[i+1])
            # Sort shifts in current category by starting hour
            shiftsOut = shiftsOut + self.sortByStartHour(shiftsIn[startIndex:endIndex])
        # Perform sort on last category
        startIndex = endIndex
        endIndex = len(categories)
        shiftsOut = shiftsOut + self.sortByStartHour(shiftsIn[startIndex:endIndex])

        return shiftsOut

    # Returns list containing category for each shift
    def makeCategories(self, shifts):
        # List of shift categories
        categories = []
        for i in shifts:
            categories.append(i.category)
        return categories

    # Returns list containing each unique category
    def makeUniqueCategories(self, categories):
        uniqueCategories = []
        for i in categories:
            if i not in uniqueCategories:
                uniqueCategories.append(i)
        return uniqueCategories

    # Sort shifts by starting hour
    def sortByStartHour(self, subShifts):
        for i in range(len(subShifts) - 1):
            for j in range(len(subShifts) - 1):
                # If current shift's starting time is greater than or equal to previous shift's starting time,
                #   swap the shifts
                if subShifts[j].startTime.tm_hour >= subShifts[j+1].startTime.tm_hour:
                    temp = subShifts[j+1]
                    subShifts[j+1] = subShifts[j]
                    subShifts[j] = temp
        return subShifts

    # Sort shifts by position within starting hour
    def sortByPositionWithinStartHour(self, shiftsIn):
        # List of route shifts
        routeShifts = self.getRouteShifts(shiftsIn)
        # List of non-route shifts
        nonRouteShifts = self.getNonRouteShifts(shiftsIn)

        # List of starting hours
        startHours = self.makeStartHours(routeShifts)
        # Sort list of starting hours
        startHours.sort()

        # List of unique starting hours
        uniqueStartHours = self.makeUniqueStartHours(startHours)
        # Sort list of unique starting hours
        uniqueStartHours.sort()

        shiftsOut = []
        # Sort by position for each starting hour
        for i in range(len(uniqueStartHours)-1):
            # Set indices for starting hour range
            startIndex = startHours.index(uniqueStartHours[i])
            endIndex = startHours.index(uniqueStartHours[i+1])
            # Sort shifts in current starting hour by position
            shiftsOut = shiftsOut + self.sortByPosition(routeShifts[startIndex:endIndex])
        # Perform sort on last starting hour
        startIndex = endIndex
        endIndex = len(startHours)
        shiftsOut = shiftsOut + self.sortByPosition(routeShifts[startIndex:endIndex])

        # Append non-route shifts to list of shifts
        shiftsOut = shiftsOut + nonRouteShifts

        return shiftsOut

    # Returns list of route shifts extracted from list of shifts
    def getRouteShifts(self, shifts):
        routeShifts = []
        for i in shifts:
            if i.position != 0:
                routeShifts.append(i)
        return routeShifts

    # Returns list of non-route shifts extracted from list of shifts
    def getNonRouteShifts(self, shifts):
        nonRouteShifts = []
        for i in shifts:
            if i.position == 0:
                nonRouteShifts.append(i)
        return nonRouteShifts

    # Returns list containing starting hour for each shift
    def makeStartHours(self, shifts):
        # List of shift starting hours
        startHours = []
        for i in shifts:
            startHours.append(i.startTime.tm_hour)
        return startHours

    # Returns list containing each unique starting hour
    def makeUniqueStartHours(self, startHours):
        uniqueStartHours = []
        for i in startHours:
            if i not in uniqueStartHours:
                uniqueStartHours.append(i)
        return uniqueStartHours

    # Sort shifts by position
    def sortByPosition(self, subShifts):
        for i in range(len(subShifts) - 1):
            for j in range(len(subShifts) - 1):
                # If current shift's position is greater than or equal to previous shift's position, swap the shifts
                if subShifts[j].position >= subShifts[j+1].position:
                    temp = subShifts[j+1]
                    subShifts[j+1] = subShifts[j]
                    subShifts[j] = temp
        return subShifts