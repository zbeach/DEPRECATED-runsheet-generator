import xlsxwriter
import time

# Generates the runsheet workbook
def makeWorkbook(shifts):
    fileDateStr = formatDateStrForFilename(shifts[0].dateStr)
    headerDateStr = formatDateStrForHeader(shifts[0].dateStr)

    workbook = xlsxwriter.Workbook("data/Runsheet " + fileDateStr + ".xlsx")
    worksheet = workbook.add_worksheet()

    # Write shifts to worksheet
    #writeRunsheet(shifts, worksheet)

    addRunsheetHeader(worksheet, fileDateStr)
    addColumnHeaders(worksheet)

    #TEST
    worksheet.write(2, 0, headerDateStr)

    workbook.close()

# Replaces forward slashes with hyphens in date string
def formatDateStrForFilename(dateStr):
    dateStr = dateStr.replace('/', '-')
    return dateStr

# Returns provided date in header format
def formatDateStrForHeader(dateStr):
    date = time.strptime(dateStr, "%m/%d/%Y")
    return time.strftime("%A %B %d, %Y", date)

# Writes runsheet header
def addRunsheetHeader(worksheet, date):
    worksheet.write(0, 0, "Radford Transit")
    worksheet.write(1, 0, date)
    worksheet.write(2, 0, None)

# Adds column headers
def addColumnHeaders(worksheet):
    worksheet.write(3, 1, "Last Name")
    worksheet.write(3, 2, "First Name")
    worksheet.write(3, 3, "Bus #")
    worksheet.write(3, 4, "Route")
    worksheet.write(3, 5, "Start Time")
    worksheet.write(3, 6, "End Time")
    worksheet.write(3, 7, "Shift Changes")


'''
# Writes shifts to worksheet
def writeRunsheet(shifts, worksheet):
    row = 0
    worksheet.write(row, 0, shifts[0].category)
    row = 1
    for i in range(0, len(shifts)):
        if i > 0:
            if shifts[i].startTime.tm_hour > shifts[i - 1].startTime.tm_hour:
                row += 1
                worksheet.write(row - 1, 0, shifts[i].category)
        worksheet.write(row, 1, shifts[i].lastName)
        worksheet.write(row, 2, shifts[i].firstName)
        worksheet.write(row, 3, shifts[i].position)
        worksheet.write(row, 4, shifts[i].startTimeStr)
        worksheet.write(row, 5, shifts[i].endTimeStr)
        row += 1
'''