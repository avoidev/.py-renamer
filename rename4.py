import os
import pyodbc
import re
import sys

conn = pyodbc.connect('Driver={SQL Server};'  # SQL Connections
                      'Server=ServerName;'
                      'Database=DatabaseName;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT X FROM X WHERE X ORDER BY X')  # SQL pull data for costcode

costcode = []  # costcode list

for row in cursor:  # importing and trimming costcode list data
    row = row[0]
    costcode.append(row)

costcode.append('9999')  # added to help prevent going over list index and creating errors.

cursor.execute('SELECT X FROM X WHERE X ORDER BY X')  # SQL Pull data for costname

costname = []  # costname list

for row in cursor:  # importing and trimming costcode list data
    row = row[0]
    costname.append(row)

costname = [b.replace('*', '-') for b in costname]  # Replacing forbidden characters
costname = [b.replace('\\', '-') for b in costname]  # Replacing forbidden characters
costname = [b.replace('/', '-') for b in costname]  # Replacing forbidden characters

match = 0
a = costcode
b = 0

for file in os.listdir('.'):  # Usually files are XXXX_XXX_X.pdf
    match = 0
    trim = re.sub("\d\d\d\d_", '', file)  # Trimming number off the front of files. XXXX_XXX_X.pdf -> XXX_X.pdf
    trim = re.sub("_\d", '_', trim) # Trimming of Number at the end. XXX_X.pdf -> XXX_.pdf
    while match == 0:
        if a[b] >= max(costcode):
            match = 1
            b = 0
        else:
            if a[b] + '_' not in trim:  # Looks for costcode number followed by _ so that other numbers don't trigger
                                        # the rename
                b += 1
            else:
                costcodename = costname.__getitem__(costcode.index(a[b]))
                if costcodename in file:  # Skips already renamed files
                    print(file)
                    print("Not required")
                    b = 0  # Resets counter
                    match = 1  # Ends loops.

                else:  # Renames file.
                    print(file + " is now " + costname.__getitem__(costcode.index(a[b])) + " " + file)
                    os.rename(file, (costname.__getitem__(costcode.index(a[b]))) + " " + file)
                    b = 0  # Resets counter
                    match = 1  # Ends loops.

print("End of script")


