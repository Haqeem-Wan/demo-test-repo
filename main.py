import csv
import math
import time
import pandas as pd
from geopy.distance import geodesic
from fileinput import close
from pprint import pprint

from numpy import array

peopleFile = "people.csv"
ppvFile = "ppv.csv"

people_lat_list = []
people_lon_list = []
ppv_lat_list = []
ppv_lon_list = []
distance_compare_list = []
paired_list = []

def coordinate_distance_formula(lat_1, lon_1, lat_2, lon_2):
    radius = 6371 # Radius of the Earth

    distance_lat = math.radians(float(lat_2) - float(lat_1))
    distance_lon = math.radians(float(lon_2) - float(lon_1))
    a = math.sin(float(distance_lat)/2) * math.sin(float(distance_lat)/2) + math.cos(math.radians(float(lat_1))) * math.cos(math.radians(float(lat_2))) * math.sin(float(distance_lon)/2) * math.sin(float(distance_lon)/2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    d = radius * c

    return d

def read_files_csvreader() :
    with open(peopleFile, 'r') as readFile:
        csvreader = csv.reader(readFile)

        next(csvreader)

        for row in csvreader:
            people_lat_list.append(row[1])
            people_lon_list.append(row[2])

        print("Total no. of rows of people : %d"%(csvreader.line_num))

    with open(ppvFile, 'r') as readFile:
        csvreader = csv.reader(readFile)

        next(csvreader)

        for row in csvreader:
            ppv_lat_list.append(row[1])
            ppv_lon_list.append(row[2])

        print("Total no. of rows of ppv : %d"%(csvreader.line_num))

def read_files_pandas() :
    print("filler")

# --- Start of Method 1: ---

def method_one() :
    start_time = time.time()

    read_files_csvreader()

    i = 0
    j = 0

    #while i <  len(people_lat_list):
    while i <  5:
        while j < len(ppv_lat_list) :
            distance_test = coordinate_distance_formula(people_lat_list[i], people_lon_list[i], ppv_lat_list[j], ppv_lon_list[j])
            distance_compare_list.append(distance_test)

            j += 1

        closest_distance = min(distance_compare_list)

        closest_ppv = distance_compare_list.index(closest_distance)
        
        paired_list.append([i, closest_ppv, closest_distance])
        distance_compare_list.clear()

        j = 0
        i += 1

    pprint(paired_list)

    end_time = time.time()

    print("\nExecution Time (Method 1) : ", (end_time - start_time))

# --- End of Method 1 ---



# --- Start of Method 2:---

def method_two() :
    start_time = time.time()

    read_files_csvreader()

    current_short_distance = 0
    compare_distance = 0
    shortest_index = 0

    #for i in range(0, len(people_lat_list), 1) :
    for i in range(0, 5, 1) :
        current_person = (people_lat_list[i], people_lon_list[i])
        for j in range(0, len(ppv_lat_list), 1) :
            current_ppv = (ppv_lat_list[j], ppv_lon_list[j])
            compare_distance = geodesic(current_person, current_ppv).km
            
            if(compare_distance < current_short_distance and j > 0) :
                current_short_distance = compare_distance
                shortest_index = j
            elif(j == 0) :
                current_short_distance = compare_distance

        closest_ppv = shortest_index
        
        paired_list.append([i, closest_ppv, current_short_distance])
        distance_compare_list.clear()
        current_short_distance = 0

    pprint(paired_list)
    end_time = time.time()

    print("\nExecution Time (Method 2) : ", (end_time - start_time))

# --- End of Method 2 ---



# --- Start of Method 3: ---

def method_three():
    start_time = time.time()

    read_files_pandas()


    end_time = time.time()

    print("\nExecution Time (Method 3) : ", (end_time - start_time))

# --- End of Method 3 ---

# --- Execution Code ---

method_one()                # Haversine formula + While Loop + csvreader
paired_list.clear()         
method_two()                # Geopy + For Loop + csvreader
paired_list.clear()
method_three()            # Numpy + Pandas + dataframes

"""people_lat_numpy_array = array(people_lat_list)
    people_lon_numpy_array = array(people_lon_list)
    ppv_lat_numpy_array = array(ppv_lat_list)
    ppv_lon_numpy_array = array(ppv_lon_list)

    print(people_lat_numpy_array[1])

    for index in range(0, len(people_lat_numpy_array), 1) :
        print([math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2) for x0, y0, x1, y1 in zip(people_lat_numpy_array[index], people_lon_numpy_array[index], ppv_lat_numpy_array, ppv_lon_numpy_array)])"""