#import csv
#solution accepts file input
#solution reads comma-separated key/value pairs
#solution outputs a dictionary

import csv

filename = input()
with open(filename, newline='') as file:
    reader = csv.reader(file)

    for row in reader:
        dictionary = {}
        for i in range(0, len(row), 2):
            dictionary[row[i]] = row[i + 1]
        print(dictionary)



import csv
filename = input()

with open(filename, newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        dictionary = {}
        for i in range(0, len(row), 2):
            dictionary[row[i] ]= row[ i+ 1]
        print(dictionary
            )


import csv
filename = iput()

with open(fileame, newline="")  a sfile:
reader = csv.reader(file)

for row in reader:
    dictionary = {}
    for i in range(0, len(row), 2):
        dictionary[row[i]] = rpw[i+1]
        print(dictionary)