import fnmatch, os, pyodbc, datetime
import re

conn = pyodbc.connect('Driver={SQL Server};'  # SQL Connections
                      'Server=XXXXXXXXX;'
                      'Database=XXXXXXXXX;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT Code FROM CostCentres WHERE Code <> 318 ORDER BY Code ASC')  # SQL pull data for costcode

costcode = []  # costcode list

for row in cursor:  # importing and trimming costcode list data
    row = row[0]
    costcode.append(row)

cursor.execute('SELECT Name FROM CostCentres WHERE Code <> 318 ORDER BY Code ASC')  # SQL Pull data for costname

costname = []  # costname list

for row in cursor:  # importing and trimming costcode list data
    row = row[0]
    costname.append(row)

costname = [b.replace('*', '-') for b in costname]  # Replacing forbidden characters
costname = [b.replace('\\', '-') for b in costname]  # Replacing forbidden characters
costname = [b.replace('/', '-') for b in costname]  # Replacing forbidden characters

a = costcode
b = 2
match = 0

for file in os.listdir("."):
    match = 0
    trim = re.sub("\d\d\d\d_", '', file)
    trim = re.sub("_\d\d\d", '', trim)
    while match == 0:
        if a[b] not in trim:
            b += 1
        else:
            print("Trim: " + trim)
            print(a[b])
            print(costcode.index(a[b]))
            index = int(costcode.index(a[b]))
            print(costname.__getitem__(index))
            match = 1
            os.rename(file, (costname.__getitem__(costcode.index(a[b]))) + " " + file)
            b = 0

print("done!")
