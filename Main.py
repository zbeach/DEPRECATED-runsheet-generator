import csv
import queue

with open('/Users/zack/Desktop/EXPORT.csv', 'r') as csvfile:
    r = csv.reader(csvfile, dialect=csv.excel)

    # First row of the CSV contains column headers
    HEADER_ROW = next(r)

    # Column indices from CSV file
    LAST_NAME_COLUMN = HEADER_ROW.index("Employee Last Name")
    FIRST_NAME_COLUMN = HEADER_ROW.index("Employee First Name")
    POSITION_COLUMN = HEADER_ROW.index("Position Name")
    CATEGORY_COLUMN = HEADER_ROW.index("Category")
    START_TIME_COLUMN = HEADER_ROW.index("Start Time")
    END_TIME_COLUMN = HEADER_ROW.index("End Time")
    DATE_COLUMN = HEADER_ROW.index("Date")

    # Runsheet date
    inputDate = "1/28/2016" # Test

    # Queue of all shifts on given date
    allShifts = queue.Queue()

    # Add all shifts from date to queue
    for row in r:
        if row[DATE_COLUMN] == inputDate:
            # Only add shifts that are not Operations Supervisor or Mega Bus Connect
            if (row[POSITION_COLUMN] != "Operations Supervisor") and (row[POSITION_COLUMN] != "Mega Bus Connect"):
                    allShifts.put(row)

    # Create list of shifts for runsheet
    shifts = [["" for x in range(6)] for x in range(allShifts.qsize())]
    for i in shifts:
        current = allShifts.get()
        i[0] = current[LAST_NAME_COLUMN]
        i[1] = current[FIRST_NAME_COLUMN]
        i[2] = current[POSITION_COLUMN]
        i[3] = current[START_TIME_COLUMN]
        i[4] = current[END_TIME_COLUMN]
        i[5] = current[CATEGORY_COLUMN]
        print(i);

    # Sort shifts for runsheet presentation
    # Add category separators
    # Generate XLSX


