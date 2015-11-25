#!/usr/bin/env python

'''This code will take a .csv file and scan through it, replacing empty fields with x, where x can be defined '''

import csv
import sys

#1. Place each record of a file in a list.
#2. Iterate thru each element of the list and get its length.
#3. If the length is less than one replace with value x.

f = open('output.csv', 'w')

reader = csv.reader(open(sys.argv[1], "rb"))
for row in reader:
    for i, x in enumerate(row):
                if len(x)< 1:
                         x = row[i] = 0
    f.write(','.join(int(x) for x in row))
    f.write('\n')

f.close()