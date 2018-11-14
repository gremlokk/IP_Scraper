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
    col_name = str(input("Enter the Column Name To Check IPs: "))
    #col_name = 'IPaddress' 
    
    print("Program Started.\n")

    with open(file) as csvfile:
        readCSV = csv.DictReader(csvfile)#read file
        list_of_ips = [row[col_name] for row in readCSV]#return list of IPs

    for key,value in Counter(list_of_ips).items():
        if int(value) > min_hits:
            print (key + " " + "hits: " + str(value))

    print("\nProgram Ended.")

except:
    print ("Unexpected error:", sys.exc_info()[0])#for debugging purposes
    raise
