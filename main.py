import csv

print("Hello world")

peopleFile = "people.csv"
ppvFile = "ppv.csv"

peopleInfoList = []
csvInfoList = []

with open(peopleFile, 'r') as readFile:
    csvreader = csv.reader(readFile)

    csvInfoList = next(csvreader)

    for row in csvreader:
        peopleInfoList.append(row)

    print("Total no. of rows: %d"%(csvreader.line_num))

print('\nFirst 5 rows are:\n')
for row in peopleInfoList[:10]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')
