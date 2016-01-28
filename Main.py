import csv
import queue

with open('/Users/zack/Desktop/EXPORT.csv', 'r') as csvfile:
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

    # All shifts on given date
    allShifts = []

    # Add all shifts from date in CSV file to list
    for row in r:
        if row[DATE_CSV_COLUMN] == inputDate:
            # Only add shifts that are not Operations Supervisor or Mega Bus Connect
            if (row[POSITION_CSV_COLUMN] != "Operations Supervisor") and (row[POSITION_CSV_COLUMN] != "Mega Bus Connect"):
                    allShifts.append(row)

    # Create list of shifts for runsheet
    # Set column constants
    LAST_NAME_COLUMN = 0
    FIRST_NAME_COLUMN = 1
    POSITION_COLUMN = 2
    POSITION_NUMBER_COLUMN = 3
    START_TIME_COLUMN = 4
    END_TIME_COLUMN = 5
    CATEGORY_COLUMN = 6

    # Initialize with default value of "" for every element
    shifts = [["" for x in range(7)] for x in range(len(allShifts))]
    for i in range(len(shifts)):
        current = allShifts[i]
        shifts[i][LAST_NAME_COLUMN] = current[LAST_NAME_CSV_COLUMN]
        shifts[i][FIRST_NAME_COLUMN] = current[FIRST_NAME_CSV_COLUMN]
        shifts[i][POSITION_COLUMN] = current[POSITION_CSV_COLUMN]
        shifts[i][POSITION_NUMBER_COLUMN] = 0
        shifts[i][START_TIME_COLUMN] = current[START_TIME_CSV_COLUMN]
        shifts[i][END_TIME_COLUMN] = current[END_TIME_CSV_COLUMN]
        shifts[i][CATEGORY_COLUMN] = current[CATEGORY_CSV_COLUMN]

    # Set position numbers
    INDEX_AFTER_END_OF_POSITION_NUMBER = 2
    for i in shifts:
        if (i[POSITION_COLUMN] != "Training") and (i[POSITION_COLUMN] != ""):
            i[POSITION_NUMBER_COLUMN] = int(i[POSITION_COLUMN][:INDEX_AFTER_END_OF_POSITION_NUMBER])

    # Sort shifts by category
    temp = [["" for x in range(7)] for x in range(len(shifts))]
    j = 0 # Position in temp
    for i in shifts:
        if i[CATEGORY_COLUMN] == "A":
            temp[j] = i
            j += 1
    for i in shifts:
        if i[CATEGORY_COLUMN] == "B":
            temp[j] = i
            j += 1
    for i in shifts:
        if i[CATEGORY_COLUMN] == "C":
            temp[j] = i
            j += 1
    for i in shifts:
        if i[CATEGORY_COLUMN] == "D":
            temp[j] = i
            j += 1
    for i in shifts:
        if i[CATEGORY_COLUMN] == "E":
            temp[j] = i
            j += 1
    for i in shifts:
        if i[POSITION_COLUMN] == "Training":
            temp[j] = i
            j += 1
    shifts = temp

    # Sort shifts by position
    numberOfShiftsInCurrentCategory = 0
    for i in shifts:
        if i[CATEGORY_COLUMN] == "A":
            numberOfShiftsInCurrentCategory += 1

    temp = [["" for x in range(7)] for x in range(len(shifts))]
    j = 0 # Position in temp
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 10:
            temp[j] = shifts[i]
            j += 1
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 11:
            temp[j] = shifts[i]
            j += 1
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 12:
            temp[j] = shifts[i]
            j += 1
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 20:
            temp[j] = shifts[i]
            j += 1
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 30:
            temp[j] = shifts[i]
            j += 1
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 31:
            temp[j] = shifts[i]
            j += 1
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 40:
            temp[j] = shifts[i]
            j += 1
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 41:
            temp[j] = shifts[i]
            j += 1
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 50:
            temp[j] = shifts[i]
            j += 1
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 51:
            temp[j] = shifts[i]
            j += 1
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 60:
            temp[j] = shifts[i]
            j += 1
    for i in range(numberOfShiftsInCurrentCategory):
        if shifts[i][POSITION_NUMBER_COLUMN] == 61:
            temp[j] = shifts[i]
            j += 1
    shifts = temp

    for i in shifts:
        print(i)


    # Add category separators
    # Generate XLSX