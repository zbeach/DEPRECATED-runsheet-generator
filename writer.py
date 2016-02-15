import xlsxwriter
import time
from enum import Enum

class writer:
    def __init__(self):
        return None

    # Generate the runsheet workbook file
    def makeWorkbook(self, shifts, runsheetDirectoryStr):
        # Date of runsheet
        DATE = shifts[0].date
        # Date string formatted for runsheet filename
        fileDateStr = self.dateToDateStrForFilename(DATE)

        # Runsheet workbook file
        self.workbook = xlsxwriter.Workbook(runsheetDirectoryStr + fileDateStr + ".xlsx")

        # Make formats
        self.makeFormats()

        # Write to runsheet
        worksheet = self.writeRunsheet(shifts, self.workbook)

        self.workbook.close()

    # Format date string for runsheet filename
    def dateToDateStrForFilename(self, date):
        return time.strftime("%m-%d-%Y")

    # Make runsheet formats
    def makeFormats(self):
        # Runsheet header formats
        self.runsheetHeader1Format = self.workbook.add_format({
            'bold': True,
            'font_name': 'Arial',
            'font_size': 15,
            'align': 'center'
        })
        self.runsheetHeader2Format = self.workbook.add_format({
            'bold': True,
            'font_color': 'red',
            'font_name': 'Arial',
            'font_size': 13,
            'align': 'center'
        })

        # Table formats
        self.columnHeadersFormat = self.workbook.add_format({
            'bold': True,
            'font_name': 'Arial',
            'font_size': 10,
            'align': 'center'
        })
        self.categoriesFormat = self.workbook.add_format({
            'bold': True,
            'font_name': 'Arial',
            'font_size': 11,
            'align': 'left',
            'bg_color': '#d3d3d3'
        })
        self.centeredContentCellsFormat = self.workbook.add_format({
            'font_name': 'Arial',
            'font_size': 10,
            'align': 'center',

            'border': 1 # Continuous
        })
        self.leftAlignedContentCellsFormat = self.workbook.add_format({
            'font_name': 'Arial',
            'font_size': 10,
            'align': 'left',

            'border': 1 # Continuous
        })
        self.positionLastOnRouteFormat = self.workbook.add_format({
            'bold': True,
            'font_name': 'Arial',
            'font_size': 10,
            'align': 'left',

            'border': 1 # Continuous
        })
        self.busCellsFormatFormat = self.workbook.add_format({
            'bold': True,
            'font_name': 'Arial',
            'font_size': 10,
            'align': 'center',

            'border': 1 # Continuous
        })

    # Write to runsheet
    def writeRunsheet(self, shifts, workbook):
        # Worksheet containing runsheet
        worksheet = workbook.add_worksheet()

        # Date of runsheet
        DATE = shifts[0].date
        runsheetHeaderDateStr = self.formatDateStrForHeader(DATE)
        # Add runsheet header
        self.addRunsheetHeader(worksheet, runsheetHeaderDateStr)

        # Add column headers
        self.addColumnHeaders(worksheet)

        # Merge cells where needed
        self.mergeCells(worksheet)

        # Set column widths
        self.setColumnWidths(worksheet)

        return worksheet

    # Format date string for writing to header
    def formatDateStrForHeader(self, date):
        return time.strftime("%A %B %d, %Y")

    # Write runsheet header
    def addRunsheetHeader(self, worksheet, dateStr):
        # Format date string for writing to header
        dateStr = self.formatDateStrForHeader(dateStr)

        worksheet.write(0, 0, "Radford Transit", self.runsheetHeader1Format)
        worksheet.write(1, 0, dateStr, self.runsheetHeader2Format)
        worksheet.write(2, 0, None)

    # Write column headers
    def addColumnHeaders(self, worksheet):
        worksheet.write(3, 1, "Last Name", self.columnHeadersFormat)
        worksheet.write(3, 2, "First Name", self.columnHeadersFormat)
        worksheet.write(3, 3, "Bus #", self.columnHeadersFormat)
        worksheet.write(3, 4, "Route", self.columnHeadersFormat)
        worksheet.write(3, 5, "Start Time", self.columnHeadersFormat)
        worksheet.write(3, 6, "End Time", self.columnHeadersFormat)
        worksheet.write(3, 7, "Shift Change", self.columnHeadersFormat)

    # Merge cells where needed
    def mergeCells(self, worksheet):
        worksheet.merge_range('A1:I1', '')
        worksheet.merge_range('A2:I2', '')
        worksheet.merge_range('H4:I4', '')

    # Set column widths
    def setColumnWidths(self, worksheet):
        worksheet.set_column(0, 0, 2.33)
        worksheet.set_column(1, 1, 18.50)
        worksheet.set_column(2, 2, 14.33)
        worksheet.set_column(3, 3, 6.67)
        worksheet.set_column(4, 4, 22.16)
        worksheet.set_column(5, 5, 8.5)
        worksheet.set_column(6, 6, 8.5)
        worksheet.set_column(7, 7, 8.5)
        worksheet.set_column(8, 8, 8.5)

'''
# Generates the runsheet workbook
def makeWorkbook(shifts):
    fileDateStr = formatDateStrForFilename(shifts[0].dateStr)

    workbook = xlsxwriter.Workbook("/Users/zack/Desktop/Runsheet" + fileDateStr + ".xlsx")

    # Write shifts to worksheet
    worksheet = writeRunsheet(shifts, workbook)


    # Merge cells where needed
    mergeCells(worksheet)

    # Set column widths
    setColumnWidths(worksheet)

    # Create formats


    # Set formats
    worksheet.set_row(0, 15, runsheetHeader1Format)
    worksheet.set_row(1, 15, runsheetHeader2Format)
    worksheet.set_row(3, 15, columnHeadersFormat)

    # Close workbook
    workbook.close()

    return "Runsheet" + fileDateStr + ".xlsx"

###############################


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
    if shifts[0].lastOnRoute:
        worksheet.write(row, 4, shifts[0].position, positionLastOnRouteFormat)
    else:
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
        if shifts[i].lastOnRoute:
            worksheet.write(row, 4, shifts[i].position, positionLastOnRouteFormat)
        else:
            worksheet.write(row, 4, shifts[i].position, leftAlignedContentCellsFormat)
        worksheet.write(row, 5, shifts[i].startTimeStr, centeredContentCellsFormat)
        worksheet.write(row, 6, shifts[i].endTimeStr, centeredContentCellsFormat)
        worksheet.write(row, 7, None, centeredContentCellsFormat)
        worksheet.write(row, 8, None, centeredContentCellsFormat)
        row += 1

    return worksheet

'''