import sorter
import writer
import GUI
import os
import platform

# Make GUI
gui = GUI.GUI()

# File containing raw data
CSV_FILE = open(gui.output[0], 'r')
# Directory of output file
RUNSHEET_DIRECTORY_STR = gui.output[1] + "/"
# Runsheet date
DAY_OF_OPERATIONS = gui.output[2]

# Shift sorter
s = sorter.sorter(CSV_FILE)

# Create and sort shifts list
shifts = s.sort(s.createShifts(DAY_OF_OPERATIONS))

# Runsheet writer
w = writer.writer()

# Runsheet workbook
w.makeWorkbook(shifts, RUNSHEET_DIRECTORY_STR)

# Open generated runsheet
if platform.system() == "Darwin":
    os.system("open " + RUNSHEET_DIRECTORY_STR + w.dateStrForFilename + ".xlsx")
elif platform.system() == "Windows":
    os.system("start " + RUNSHEET_DIRECTORY_STR + w.dateStrForFilename + ".xlsx")