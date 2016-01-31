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
    for i in range(len(shifts)):
        worksheet.write(i, 0, shifts[i].lastName)
        worksheet.write(i, 1, shifts[i].firstName)
        worksheet.write(i, 2, shifts[i].position)
        worksheet.write(i, 3, shifts[i].startTimeStr)
        worksheet.write(i, 4, shifts[i].endTimeStr)