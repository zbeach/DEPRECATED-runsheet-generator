import csv
import shift
import writer

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
                             i[END_TIME_CSV_COLUMN], \
                             i[DATE_CSV_COLUMN])
        shifts.append(currentShift)
    return shifts

# Sorts list of shifts
def sort(shifts):
    # Sort by category
    shifts = sortByCategory(shifts)
    # Sort by position within category
    shifts = sortByPositionWithinCategory(shifts)
    # Separate by hour
    shifts = sortByHour(shifts)
    return shifts

# Sorts list of shifts by category
def sortByCategory(shifts):
    for i in range(len(shifts)):
        for j in range(len(shifts)):
            if shifts[j].category > shifts[i].category:
                temp = shifts[i]
                shifts[i] = shifts[j]
                shifts[j] = temp
    return shifts

# Sorts list of shifts by position within category
def sortByPositionWithinCategory(shiftsIn):
    numberOfCategories = getNumberOfCategories(shiftsIn)
    categoryIndices = getCategoryIndices(shiftsIn)
    shiftsOut = []
    for i in range(len(categoryIndices)):
        start = categoryIndices[i]
        if i == len(categoryIndices) - 1:
            end = len(categoryIndices)
        else:
            end = categoryIndices[i + 1]
        shiftsOut = shiftsOut + (sortByPosition(shiftsIn[start:end]))
    return shiftsOut

# Sorts list of shifts by position
def sortByPosition(shiftsInCategory):
    for i in range(len(shiftsInCategory)):
        for j in range(len(shiftsInCategory)):
            if shiftsInCategory[j].positionNumber > shiftsInCategory[i].positionNumber:
                temp = shiftsInCategory[i]
                shiftsInCategory[i] = shiftsInCategory[j]
                shiftsInCategory[j] = temp
    return shiftsInCategory

# Gets number of categories in shifts list
def getNumberOfCategories(shifts):
    numberOfCategories = 0
    previousCategory = '#'
    for i in range(len(shifts)):
        if shifts[i].category != previousCategory:
            previousCategory = shifts[i].category
            numberOfCategories += 1

# Gets index for first shift of each category in list
def getCategoryIndices(shifts):
    indices = [0]
    previousCategory = shifts[0].category
    for i in range(len(shifts)):
        if shifts[i].category != previousCategory:
            previousCategory = shifts[i].category
            indices.append(i)
    return indices

# Separates shifts by hour
def sortByHour(shifts):
    for i in range(len(shifts)):
        for j in range(i, len(shifts) - 1):
            if shifts[j].startTime.tm_hour > shifts[j + 1].startTime.tm_hour:
                temp = shifts[j + 1]
                shifts[j + 1] = shifts[j]
                shifts[j] = temp
    return shifts


########## Main ##########

with open('data/EXPORT2.CSV', 'r') as csvfile:
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
    inputDate = "2/2/2016" # Test

    # Create list of shifts for runsheet
    shifts = createShifts(r, inputDate)

    # Sort shifts
    shifts = sort(shifts)

    # Generate workbook
    writer.makeWorkbook(shifts)

    for i in range(len(shifts)):
        print(shifts[i].toString())
