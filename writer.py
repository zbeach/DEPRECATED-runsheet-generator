import xlsxwriter
import time
import sorter

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
        self.dateStrForFilename = time.strftime("%m-%d-%Y", date)
        return self.dateStrForFilename

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
        self.busCellsFormat = self.workbook.add_format({
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

        # String representation of date of runsheet
        runsheetHeaderDateStr = time.strftime("%A %B %d, %Y", shifts[0].date)
        # Add runsheet header
        self.addRunsheetHeader(worksheet, runsheetHeaderDateStr)

        # Write table contents
        self.writeTable(shifts, worksheet)

        return worksheet

    # Write runsheet header
    def addRunsheetHeader(self, worksheet, dateStr):
        worksheet.write(0, 0, "Radford Transit", self.runsheetHeader1Format)
        worksheet.write(1, 0, dateStr, self.runsheetHeader2Format)
        worksheet.write(2, 0, None)

    # Write table contents
    def writeTable(self, shifts, worksheet):
        # Add column headers
        self.addColumnHeaders(worksheet)

        # Merge cells where needed
        self.mergeCells(worksheet)

        # Set column widths
        self.setColumnWidths(worksheet)

        # List of route shifts
        routeShifts = sorter.sorter.getRouteShifts(sorter.sorter, shifts)
        # List of non-route shifts
        nonRouteShifts = sorter.sorter.getNonRouteShifts(sorter.sorter, shifts)

        # First row
        ROW_1 = 4
        # Row iterator
        row = ROW_1
        # Write row for each route category and route shift
        self.writeCategoryHeader(worksheet, row, routeShifts[0].category)
        currentStartHour = routeShifts[0].startTime.tm_hour
        row += 1
        for i in routeShifts:
            # If new start time, write category header
            if i.startTime.tm_hour != currentStartHour:
                currentStartHour = i.startTime.tm_hour
                self.writeCategoryHeader(worksheet, row, i.category)
                # Increment row
                row += 1
            # Write shift
            self.writeShift(worksheet, row, i)
            row += 1

        # Write row for each non-route category and non-route shift
        self.writeCategoryHeader(worksheet, row, nonRouteShifts[0].category)
        currentCategory = nonRouteShifts[0].category
        row += 1
        for i in nonRouteShifts:
            # If new category, write category header
            if i.category != currentCategory:
                currentCategory = i.category
                self.writeCategoryHeader(worksheet, row, i.position)
                # Increment row
                row += 1
            # Write shift
            self.writeShift(worksheet, row, i)
            row += 1

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

    # Write category header
    def writeCategoryHeader(self, worksheet, row, category):
        # If category is 'Tr', set it to "Training"
        if category == 'Tr':
            category = "Training"
        # If category is more than one character long, category is "Other"
        elif len(category) != 1:
            category = "Other"

        # Write
        worksheet.write(row, 0, category, self.categoriesFormat)
        for i in range(1, 9):
            worksheet.write(row, i, None, self.categoriesFormat)

    # Write shift row
    def writeShift(self, worksheet, row, shift):
        worksheet.write(row, 0, None, self.centeredContentCellsFormat)
        worksheet.write(row, 1, shift.lastName, self.leftAlignedContentCellsFormat)
        worksheet.write(row, 2, shift.firstName, self.leftAlignedContentCellsFormat)
        worksheet.write(row, 3, None, self.busCellsFormat)
        # If shift is last on route, write position in bold
        if shift.lastOnRoute == True:
            worksheet.write(row, 4, shift.positionName, self.positionLastOnRouteFormat)
        else:
            worksheet.write(row, 4, shift.positionName, self.leftAlignedContentCellsFormat)
        worksheet.write(row, 5, self.timeToTimeStrForRunsheet(shift.startTime), self.centeredContentCellsFormat)
        worksheet.write(row, 6, self.timeToTimeStrForRunsheet(shift.endTime), self.centeredContentCellsFormat)
        worksheet.write(row, 7, None, self.centeredContentCellsFormat)
        worksheet.write(row, 8, None, self.centeredContentCellsFormat)

    # Return string representation of time
    def timeToTimeStrForRunsheet(self, timeStr):
        return time.strftime("%I:%M %p", timeStr).lstrip('0')