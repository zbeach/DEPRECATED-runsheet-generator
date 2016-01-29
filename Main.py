import csv
import shift

# Extracts position number from position name
def toPositionNumber(positionName):
    # Set position numbers
    INDEX_AFTER_END_OF_POSITION_NUMBER = 2
    if (positionName != "Training") and (positionName != ""):
        return int(positionName[:INDEX_AFTER_END_OF_POSITION_NUMBER])
    else:
        return 0

# Creates shifts list for given date from CSV data
def createShifts(r, date):
    data = [] # Data for all shifts on given date
    # Add all shifts from date in CSV file to list
    for row in r:
        if row[DATE_CSV_COLUMN] == date:
            # Only add shifts that are not Operations Supervisor or Mega Bus Connect
            if (row[POSITION_CSV_COLUMN] != "Operations Supervisor") and (row[POSITION_CSV_COLUMN] != "Mega Bus Connect"):
                    data.append(row)

    # Create list of shift objects
    shifts = []
    for i in data:
        currentShift = shift.shift(toPositionNumber(i[POSITION_CSV_COLUMN]), \
                             i[POSITION_CSV_COLUMN], \
                             i[CATEGORY_CSV_COLUMN], \
                             i[LAST_NAME_CSV_COLUMN], \
                             i[FIRST_NAME_CSV_COLUMN], \
                             i[START_TIME_CSV_COLUMN], \
                             i[END_TIME_CSV_COLUMN])
        shifts.append(currentShift)
    return shifts


########## Main ##########

with open('data/EXPORT.CSV', 'r') as csvfile:
    r = csv.reader(csvfile, dialect=csv.excel)

    # First row of the CSV contains column headers
    HEADER_ROW = next(r)

    # Column indices from CSV file
    LAST_NAME_CSV_COLUMN = HEADER_ROW.index("Employee Last Name")
    FIRST_NAME_CSV_COLUMN = HEADER_ROW.index("Employee First Name")
    POSITION_CSV_COLUMN = HEADER_ROW.index("Position Name")
    CATEGORY_CSV_COLUMN = HEADER_ROW.index("Category")
    START_TIME_CSV_COLUMN = HEADER_ROW.index("Start Time")
    END_TIME_CSV_COLUMN = HEADER_ROW.index("End Time")
    DATE_CSV_COLUMN = HEADER_ROW.index("Date")

    # Runsheet date
    inputDate = "1/28/2016" # Test

    # Create list of shifts for runsheet
    shifts = createShifts(r, inputDate)

    for i in shifts:
        print(i.toString())


    # Sort by category, then by position
    # Add category separators
    # Generate XLSX