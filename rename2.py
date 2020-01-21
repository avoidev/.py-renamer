import fnmatch, os, pyodbc, datetime


conn = pyodbc.connect('Driver={SQL Server};'  # SQL Connections
                      'Server=XXXXXXXX;'
                      'Database=XXXXXXXX;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT Code FROM CostCentres')  # SQL pull data for costcode

costcode = []  # costcode list

for row in cursor:  # importing and trimming costcode list data
    row = row[0]
    costcode.append(row)

cursor.execute('SELECT Name FROM CostCentres')  # SQL Pull data for costname

costname = []  # costname list

for row in cursor: # importing and trimming costcode list data
    row = row[0]
    costname.append(row)

costname = [b.replace('*', '-') for b in costname]  # Replacing forbidden characters

# costcodenumber = int('201')
# costcodenumberfix = costcode.index(str(costcodenumber + 1))
# print(costcodenumberfix)

for file in os.listdir('.'):
    for item in costcode:
        if fnmatch.fnmatch(file, '*_' + item + '_*.txt'):
            costcodenumber = int(item)
            print(costcodenumber)
            print(costcode.index(str(costcodenumber)))
            a = int(costcode.index(str(costcodenumber)))
            print(a)
            # a = a - 3
            print(a)
            print(costname.__getitem__(a))
            os.rename(file, (costname.__getitem__(a) + " " + file))
