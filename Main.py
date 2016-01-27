import csv

contents = [["" for x in range(5)] for x in range(5)]
contents[0][4] = "hello"

with open('/Users/zack/Desktop/EXPORT.csv', 'r') as csvfile:
    r = csv.reader(csvfile, dialect=csv.excel)

    HEADER_ROW = next(r)
    print(HEADER_ROW)
    LAST_NAME_COLUMN = HEADER_ROW.index("Employee Last Name")
    FIRST_NAME_COLUMN = HEADER_ROW.index("Employee First Name")
    POSITION_COLUMN = HEADER_ROW.index("Position Name")
    CATEGORY_COLUMN = HEADER_ROW.index("Category")
    START_TIME_COLUMN = HEADER_ROW.index("Start Time")
    END_TIME_COLUMN = HEADER_ROW.index("End Time")

