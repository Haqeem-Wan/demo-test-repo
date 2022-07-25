import csv
import math
import time
from fileinput import close

from numpy import array

peopleFile = "people.csv"
ppvFile = "ppv.csv"

people_info_list = []
ppv_info_list = []
distance_compare_list = []
paired_list = []

def coordinate_distance_formula(lat_1, lon_1, lat_2, lon_2):
    lat_distance = float(lat_1) - float(lat_2)
    lon_distance = float(lon_1) - float(lon_2)

    return math.sqrt(pow(lat_distance, 2) + pow(lon_distance, 2)) * 60

def read_files() :
    with open(peopleFile, 'r') as readFile:
        csvreader = csv.reader(readFile)

        next(csvreader)

        for row in csvreader:
            people_info_list.append(row)

        print("Total no. of rows of people : %d"%(csvreader.line_num))

    with open(ppvFile, 'r') as readFile:
        csvreader = csv.reader(readFile)

        next(csvreader)

        for row in csvreader:
            ppv_info_list.append(row)

        print("Total no. of rows of ppv : %d"%(csvreader.line_num))



# --- Start of Method 1: (Slowest Method) ---

def method_one() :
    start_time = time.time()

    for people_row in people_info_list:
        for ppv_row in ppv_info_list:
            distance_test = coordinate_distance_formula(people_row[1], people_row[2], ppv_row[1], ppv_row[2])
            distance_compare_list.append(distance_test)
        
        closest_distance = min(distance_compare_list)

        closest_ppv = ppv_info_list[distance_compare_list.index(closest_distance)][0]
        
        paired_list.append([people_row[0], closest_ppv, closest_distance])
        distance_compare_list.clear()

    end_time = time.time()

    print("\nExecution Time (Method 1) : ", (end_time - start_time))

# --- End of Method 1 ---



# --- Start of Method 2:---

def method_two() :
    start_time = time.time()

    people_numpy_array = array(people_info_list)
    ppv_numpy_array = array(ppv_info_list)

    end_time = time.time()

    print("\nExecution Time (Method 2) : ", (end_time - start_time))

# --- End of Method 2 ---



# --- Start of Method 3: ---

def method_three():
    start_time = time.time()



    end_time = time.time()

    print("\nExecution Time (Method 3) : ", (end_time - start_time))

# --- End of Method 3 ---

# --- Execution Code ---

read_files()
method_one()
method_two()
# method_three()


"""
    print('\nFirst 5 rows are:\n')
    for row in people_info_list[:10]:
        # parsing each column of a row
        row.append("TESTSPACE")
        print(row)
        print('\n')

    for row in people_info_list[:5]:
        for col in row:
            print("%10s"%col,end=" "),
        print('\n')
"""

"""
    Calculate Distance with Distance formula : sqrt[(x1-x2)^2 + (y1-y2)^2]
    Multiply by 60
        This is already the nautical mile distance
    Multiply by  1.852
        This is the kilometer distance
"""
