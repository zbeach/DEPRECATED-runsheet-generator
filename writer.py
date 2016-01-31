import xlsxwriter

# Generates the runsheet workbook
def makeWorkbook(shifts):
    date = formatDateStr(shifts[0].dateStr)

    workbook = xlsxwriter.Workbook("data/Runsheet " + date + ".xlsx")
    worksheet = workbook.add_worksheet()

    # Write shifts to worksheet
    writeRunsheet(shifts, worksheet)

    workbook.close()

# Replaces forward slashes with hyphens in date string
def formatDateStr(dateStr):
    dateStr = dateStr.replace('/', '-')
    return dateStr

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