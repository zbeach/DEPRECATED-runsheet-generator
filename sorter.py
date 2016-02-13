import csv
import shift

class sorter:

    def __init__(self, file, date):
        # Reader for csvfile
        reader = csv.reader(file, dialect=csv.excel)

        # Create shifts list
        self.shifts = self.createShifts(reader, date)

    # Create shift objects from reader
    def createShifts(self, reader, date):
        # Row containing column headers
        headersRow = next(reader)
        
        # Column indices in csvfile
        LAST_NAME_COLUMN = headersRow.index("Employee Last Name")
        FIRST_NAME_COLUMN = headersRow.index("Employee First Name")
        POSITION_COLUMN = headersRow.index("Position Name")
        CATEGORY_COLUMN = headersRow.index("Category")
        START_TIME_COLUMN = headersRow.index("Start Time")
        END_TIME_COLUMN = headersRow.index("End Time")
        DATE_COLUMN = headersRow.index("Date")
        DESCRIPTION_COLUMN = headersRow.index("Shift Description")

        shifts = []
        for row in reader:
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
        for i in shifts:
            print(str(i))

    # Sort shifts in runsheet presentation order
    #def sort(DAY_OF_OPERATIONS):
    #   return sortByHour(sortByCATEGORY_COLUMN(sortByPOSITION_COLUMN()))
