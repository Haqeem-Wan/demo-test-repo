import csv

print("Hello world")

peopleFile = "people.csv"
ppvFile = "ppv.csv"

peopleInfoList = []
csvInfoList = []

with open(ppvFile, 'r') as readFile:
    csvreader = csv.reader(readFile)

    for row in csvreader:
        peopleInfoList.append(row)

    print("Total no. of rows: %d"%(csvreader.line_num))
