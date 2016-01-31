import xlsxwriter
import time

# Generates the runsheet workbook
def makeWorkbook(shifts):
    fileDateStr = formatDateStrForFilename(shifts[0].dateStr)

    workbook = xlsxwriter.Workbook("data/Runsheet " + fileDateStr + ".xlsx")
    worksheet = workbook.add_worksheet()

    # Write shifts to worksheet
    writeRunsheet(shifts, worksheet)

    # Add headers
    addRunsheetHeader(worksheet, shifts[0].dateStr)
    addColumnHeaders(worksheet)

    # Merge cells where needed
    mergeCells(worksheet)

    # Set column widths
    setColumnWidths(worksheet)

    # Create formats
    formatRunsheetHeader1 = workbook.add_format({
        'bold': True,
        'font_name': 'Cambria',
        'font_size': 12,
        'align': 'center'
    })
    formatRunsheetHeader2 = workbook.add_format({
        'bold': True,
        'font_color': 'red',
        'font_name': 'Cambria',
        'font_size': 12,
        'align': 'center'
    })
    formatColumnHeaders = workbook.add_format({
        'bold': True,
        'font_name': 'Arial',
        'font_size': 10,
        'align': 'center'
    })
    formatCategories = workbook.add_format({
        'bold': True,
        'font_name': 'Arial',
        'font_size': 11,
        'align': 'center',

        'bg_color': 'gray'
    })

    # Set formats
    worksheet.set_row(0, 1, formatRunsheetHeader1)
    worksheet.set_row(1, 1, formatRunsheetHeader2)
    worksheet.set_row(3, 1, formatColumnHeaders)

    # Close workbook
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
def addRunsheetHeader(worksheet, dateStr):
    headerDateStr = formatDateStrForHeader(dateStr)

    worksheet.write(0, 0, "Radford Transit")
    worksheet.write(1, 0, headerDateStr)
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


# Writes shifts to worksheet
def writeRunsheet(shifts, worksheet):
    row = 4
    worksheet.write(row, 0, shifts[0].category)
    row = 5
    for i in range(0, len(shifts)):
        if i > 0:
            if shifts[i].startTime.tm_hour > shifts[i - 1].startTime.tm_hour:
                row += 1
                worksheet.write(row - 1, 0, shifts[i].category)
        worksheet.write(row, 1, shifts[i].lastName)
        worksheet.write(row, 2, shifts[i].firstName)
        worksheet.write(row, 4, shifts[i].position)
        worksheet.write(row, 5, shifts[i].startTimeStr)
        worksheet.write(row, 6, shifts[i].endTimeStr)
        row += 1

# Merges cells where needed
def mergeCells(worksheet):
    worksheet.merge_range('A1:I1', '')
    worksheet.merge_range('A2:I2', '')
    worksheet.merge_range('H4:I4', '')

# Sets column widths
def setColumnWidths(worksheet):
    worksheet.set_column(0, 0, 2.33)
    worksheet.set_column(1, 1, 18.50)
    worksheet.set_column(2, 2, 14.33)
    worksheet.set_column(3, 3, 6.67)
    worksheet.set_column(4, 4, 22.16)
    worksheet.set_column(5, 5, 9.33)
    worksheet.set_column(6, 6, 9.33)
    worksheet.set_column(7, 7, 8)
    worksheet.set_column(8, 8, 8)