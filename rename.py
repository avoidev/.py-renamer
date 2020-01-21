import fnmatch, os, pyodbc, datetime


conn = pyodbc.connect('Driver={SQL Server};'  # SQL Connections
                      'Server=XXXXXXX;'
                      'Database=XXXXXXXXX;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT Code FROM CostCentres')  # SQL pull data for costcode

costcode = []  # costcode list

for row in cursor:  # importing and trimming costcode list data
    row = row[0]
    costcode.append(row)

cursor.execute('SELECT Name FROM CostCentres')  # SQL Pull data for costname

costname = [] # costname list

for row in cursor: # importing and trimming costcode list data
    row = row[0]
    costname.append(row)

costname = [b.replace('*', '-') for b in costname]  # Replacing forbidden characters

f = open("OUTPUT.txt", "w")  # Begin Log
f.write(str(datetime.datetime.now()))
f.write("\n")

for file in os.listdir('.'):
    for item in costcode:
        if fnmatch.fnmatch(file, '*_' + str(item) + '_*.txt'):
            print(str(item))
            if fnmatch.fnmatch(file, (costname.__getitem__(costcode.index(item))) + "*" + ".txt"):
                print("already done")
                f.write(file + " is already done.")
                f.write("\n")
            else:
                f.write("old: " + file + " -----> ")
                os.rename(file, (costname.__getitem__(costcode.index(item))) + " " + file)
                f.write("now: " + (costname.__getitem__(costcode.index(item))) + " " + file)
                f.write("\n")
        else:
            print("skipped: " + file + ".")

print(costcode)
print(costname)