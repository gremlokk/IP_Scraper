'''
Fredrick Ryans
8/16/2018
Version: 1.0

The purpose of this script is to find the number of IP addresses
that may be causing a clients bandwidth to spike in Americommerce.
'''

import csv
import sys
from collections import Counter

try:
    file = str(input("Enter a file path: "))
    min_hits = int(input("Enter a number for the minimum amount of hits to track for an IP address: "))

    print("Program Started.\n")
    
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        list_of_ips = [row[9] for row in readCSV]
    
    for key,value in Counter(list_of_ips).items():
        if int(value) > min_hits:
            print (key + " " + "hits: " + str(value))

    print("\nProgram Ended.")

except:
    print ("Unexpected error:", sys.exc_info()[0])
    raise
