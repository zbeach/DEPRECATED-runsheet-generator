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
                # Filter by POSITION_COLUMNs that are not Operations Supervisor or Mega Bus Connect
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

        # Create list of categories
        categories = self.createCategories(shifts)

        # Sort by starting hour
        shifts = self.sortByStartHour(shifts)
        # Sort by position
        shifts = self.sortByPosition(shifts)

        return shifts

    # Sort shifts by category
    def sortByCategory(self, shifts):
        for i in range(len(shifts) - 1):
            for j in range(len(shifts) - 1):
                # If current shift's category is greater than or equal to previous shifts category, swap the shifts
                if shifts[j].category >= shifts[j+1].category:
                    temp = shifts[j+1]
                    shifts[j+1] = shifts[j]
                    shifts[j] = temp
        return shifts

    # Sort shifts by starting hour
    def sortByStartHour(self, shifts):
        for i in range(len(shifts) - 1):
            for j in range(len(shifts) - 1):
                # If current shift's starting time is greater than or equal to previous shift's starting time,
                #   swap the shifts
                if shifts[j].startTime.tm_hour >= shifts[j+1].startTime.tm_hour:
                    temp = shifts[j+1]
                    shifts[j+1] = shifts[j]
                    shifts[j] = temp
        return shifts

    # Sort shifts by position
    def sortByPosition(self, shifts):
        return shifts

    # Create list of categories
    def createCategories(self, shifts):
        categories = []
        for i in shifts:
            if i.category not in categories:
                categories.append(i.category)

        return categories