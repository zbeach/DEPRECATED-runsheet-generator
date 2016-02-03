import xlsxwriter
import time

# Generates the runsheet workbook
def makeWorkbook(shifts):
    fileDateStr = formatDateStrForFilename(shifts[0].dateStr)

    workbook = xlsxwriter.Workbook("data/Runsheet" + fileDateStr + ".xlsx")

    # Write shifts to worksheet
    worksheet = writeRunsheet(shifts, workbook)

    # Add headers
    addRunsheetHeader(worksheet, shifts[0].dateStr)
    addColumnHeaders(worksheet)

    # Merge cells where needed
    mergeCells(worksheet)

    # Set column widths
    setColumnWidths(worksheet)

    # Create formats
    runsheetHeader1Format = workbook.add_format({
        'bold': False,
        'font_name': 'Arial',
        'font_size': 15,
        'align': 'center'
    })
    runsheetHeader2Format = workbook.add_format({
        'bold': False,
        'font_color': 'red',
        'font_name': 'Arial',
        'font_size': 13,
        'align': 'center'
    })
    columnHeadersFormat = workbook.add_format({
        'bold': True,
        'font_name': 'Arial',
        'font_size': 10,
        'align': 'center'
    })

    # Set formats
    worksheet.set_row(0, 15, runsheetHeader1Format)
    worksheet.set_row(1, 15, runsheetHeader2Format)
    worksheet.set_row(3, 15, columnHeadersFormat)

    # Close workbook
    workbook.close()

    return "Runsheet" + fileDateStr + ".xlsx"

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
    worksheet.write(3, 7, "Shift Change")


# Writes shifts to worksheet
def writeRunsheet(shifts, workbook):

    worksheet = workbook.add_worksheet()

    categoriesFormat = workbook.add_format({
        'bold': True,
        'font_name': 'Arial',
        'font_size': 11,
        'align': 'left',
        'bg_color': '#d3d3d3'
    })
    centeredContentCellsFormat = workbook.add_format({
        'font_name': 'Arial',
        'font_size': 10,
        'align': 'center',

        'border': 1 # Continuous
    })
    leftAlignedContentCellsFormat = workbook.add_format({
        'font_name': 'Arial',
        'font_size': 10,
        'align': 'left',

        'border': 1 # Continuous
    })
    busCellsFormat = workbook.add_format({
        'font_name': 'Arial',
        'font_size': 10,
        'bold': True,
        'align': 'center',

        'border': 1 # Continuous
    })

    # Write first column row
    row = 4
    worksheet.write(row, 0, shifts[0].category, categoriesFormat)
    for i in range(1, 9):
        worksheet.write(row, i, None, categoriesFormat)

    # Write first shift row
    row += 1
    worksheet.write(row, 0, None, centeredContentCellsFormat)
    worksheet.write(row, 1, shifts[0].lastName, leftAlignedContentCellsFormat)
    worksheet.write(row, 2, shifts[0].firstName, leftAlignedContentCellsFormat)
    worksheet.write(row, 3, None, busCellsFormat)
    worksheet.write(row, 4, shifts[0].position, leftAlignedContentCellsFormat)
    worksheet.write(row, 5, shifts[0].startTimeStr, centeredContentCellsFormat)
    worksheet.write(row, 6, shifts[0].endTimeStr, centeredContentCellsFormat)
    worksheet.write(row, 7, None, centeredContentCellsFormat)
    worksheet.write(row, 8, None, centeredContentCellsFormat)

    # Write remaining rows
    row += 1

    for i in range(1, len(shifts)):
        if shifts[i].category == 'T':
            if shifts[i - 1].category != 'T':
                worksheet.write(row, 0, "Training", categoriesFormat)
                for j in range(1, 9):
                    worksheet.write(row, j, None, categoriesFormat)
                row += 1
        elif shifts[i].startTime.tm_hour > shifts[i - 1].startTime.tm_hour:
            worksheet.write(row, 0, shifts[i].category, categoriesFormat)
            for j in range(1, 9):
                worksheet.write(row, j, None, categoriesFormat)
            row += 1
        worksheet.write(row, 0, None, centeredContentCellsFormat)
        worksheet.write(row, 1, shifts[i].lastName, leftAlignedContentCellsFormat)
        worksheet.write(row, 2, shifts[i].firstName, leftAlignedContentCellsFormat)
        worksheet.write(row, 3, None, busCellsFormat)
        worksheet.write(row, 4, shifts[i].position, leftAlignedContentCellsFormat)
        worksheet.write(row, 5, shifts[i].startTimeStr, centeredContentCellsFormat)
        worksheet.write(row, 6, shifts[i].endTimeStr, centeredContentCellsFormat)
        worksheet.write(row, 7, None, centeredContentCellsFormat)
        worksheet.write(row, 8, None, centeredContentCellsFormat)
        row += 1

    return worksheet

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
    worksheet.set_column(5, 5, 8.5)
    worksheet.set_column(6, 6, 8.5)
    worksheet.set_column(7, 7, 8.5)
    worksheet.set_column(8, 8, 8.5)