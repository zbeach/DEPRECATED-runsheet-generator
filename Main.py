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

    # Queue of all shifts on given date
    allShifts = queue.Queue()

    # Add all shifts from date to queue
    for row in r:
        if row[DATE_CSV_COLUMN] == inputDate:
            # Only add shifts that are not Operations Supervisor or Mega Bus Connect
            if (row[POSITION_CSV_COLUMN] != "Operations Supervisor") and (row[POSITION_CSV_COLUMN] != "Mega Bus Connect"):
                    allShifts.put(row)

    # Create list of shifts for runsheet
    # Set column constants
    LAST_NAME_COLUMN = 0
    FIRST_NAME_COLUMN = 1
    POSITION_COLUMN = 2
    START_TIME_COLUMN = 3
    END_TIME_COLUMN = 4
    CATEGORY_COLUMN = 5

    # Initialize with default value of "" for every element
    shifts = [["" for x in range(6)] for x in range(allShifts.qsize())]
    for i in shifts:
        current = allShifts.get()
        i[LAST_NAME_COLUMN] = current[LAST_NAME_CSV_COLUMN]
        i[FIRST_NAME_COLUMN] = current[FIRST_NAME_CSV_COLUMN]
        i[POSITION_COLUMN] = current[POSITION_CSV_COLUMN]
        i[START_TIME_COLUMN] = current[START_TIME_CSV_COLUMN]
        i[END_TIME_COLUMN] = current[END_TIME_CSV_COLUMN]
        i[CATEGORY_COLUMN] = current[CATEGORY_CSV_COLUMN]

    # Sort shifts for runsheet presentation
    temp = [["" for x in range(6)] for x in range(len(shifts))]
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

    # Add category separators
    # Generate XLSX







