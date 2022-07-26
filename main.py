import csv
import math
import time
from fileinput import close
from pprint import pprint
from turtle import distance

import numpy as np
import pandas as pd
from geopy.distance import geodesic

peopleFile = "people.csv"
ppvFile = "ppv.csv"

def haversine_distance_formula(lat_1, lon_1, lat_2, lon_2):
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

        people_lat_list = []
        people_lon_list = []
        ppv_lat_list = []
        ppv_lon_list = []

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

    return people_lat_list, people_lon_list, ppv_lat_list, ppv_lon_list

def read_files_pandas() :
    df_people_reader = pd.read_csv(peopleFile)
    df_ppv_reader = pd.read_csv(ppvFile)

    return df_people_reader, df_ppv_reader

# --- Start of Method 1: ---

def method_one() :
    start_time = time.time()

    people_lat_list, people_lon_list, ppv_lat_list, ppv_lon_list = read_files_csvreader()

    i = 0
    j = 0
    distance_compare_list = []
    paired_list = []

    while i <  len(people_lat_list):
        while j < len(ppv_lat_list) :
            distance_test = haversine_distance_formula(people_lat_list[i], people_lon_list[i], ppv_lat_list[j], ppv_lon_list[j])
            distance_compare_list.append(distance_test)

            j += 1

        closest_distance = min(distance_compare_list)

        closest_ppv = distance_compare_list.index(closest_distance)
        
        paired_list.append([i, closest_ppv, closest_distance])
        distance_compare_list.clear()

        j = 0
        i += 1

    end_time = time.time()

    #pprint(paired_list)

    print("\nExecution Time (Method 1) : ", (end_time - start_time))

# --- End of Method 1 ---



# --- Start of Method 2:---

def method_two() :
    start_time = time.time()

    people_lat_list, people_lon_list, ppv_lat_list, ppv_lon_list = read_files_csvreader()

    current_short_distance = 0
    compare_distance = 0
    shortest_index = 0
    distance_compare_list = []
    paired_list = []

    for i in range(0, len(people_lat_list), 1) :
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

    end_time = time.time()

    #pprint(paired_list)

    print("\nExecution Time (Method 2) : ", (end_time - start_time))

# --- End of Method 2 ---



# --- Start of Method 3: ---

def method_three():
    start_time = time.time()

    df_people_reader, df_ppv_reader = read_files_pandas()

    # records is an arbitrary name that does not matter, used those words due to FutureWarning
    dict_people = df_people_reader.to_dict('records')
    dict_ppv = df_ppv_reader.to_dict('records')

    # Convert to numpy array later
    distance_list = []
    paired_list = []
    people_lat_list = []
    people_lon_list = []
    ppv_lat_list = []
    ppv_lon_list = []

    for row in dict_people :
        people_lat_list.append(row["Lat"])
        people_lon_list.append(row["Lon"])
    
    for row in dict_ppv :
        ppv_lat_list.append(row["Lat"])
        ppv_lon_list.append(row["Lon"])

    for i in range(0, len(people_lon_list), 1) :
        for j in range(0, len(ppv_lon_list), 1) :
            distance_list.append(haversine_distance_formula(people_lat_list[i], people_lon_list[i], ppv_lat_list[j], ppv_lon_list[j]))
        distance_numpy = np.array(distance_list)
        shortest_distance = distance_numpy.min()
        ppv_index = (np.where(distance_numpy == shortest_distance))[0][0]

        paired_list.append([i, ppv_index, shortest_distance])

        distance_list.clear()

    end_time = time.time()

    #pprint(paired_list)

    print("\nExecution Time (Method 3) : ", (end_time - start_time))

# --- End of Method 3 ---

# --- Execution Code ---

method_one()                # Haversine formula + While Loop + csvreader   
#method_two()                # Geopy + For Loop + csvreader
method_three()              # Haversine formula + For Loop + Pandas dataframes + Numpy
