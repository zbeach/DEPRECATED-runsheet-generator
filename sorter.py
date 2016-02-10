import csv
from enum import Enum

# Row containing column headers
headersRow = None

def __init__(self, READER):
    # Row containing column headers
    self.headersRow = next(READER)

# Column indices in csvfile
class Columns(Enum):
    lastName = headersRow.index("Employee Last Name")
    firstName = headersRow.index("Emplyee Last Name")
    position = headersRow.index("Position Name")
    category = headersRow.index("Category")
    startTime = headersRow.index("Start Time")
    endTime = headersRow.index("End Time")
    date = headersRow.index("Date")
    description = headersRow.index("Shift Description")

def sort(DAY_OF_OPERATIONS):
    return sortByHour(sortByCategory(sortByPosition()))