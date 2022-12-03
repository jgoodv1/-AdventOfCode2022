#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:00:29 2022

@author: jonathangood
"""

def getpriorities(item):
    result = 0
    if item.isupper():
        check = item.lower()
        result += (ord(check) - 96) + 26
    else:
        result += ord(item) - 96
        
    return result
    

file, sets = [], []
result_a, result_b, counter= 0, 0, 0

file = []
import csv
with open('input3.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader: 
        items = row[0]
        file.append(items)

for items in file: 
    x = len(items)
    y = int(x/2)
    rucksack1 = []
    rucksack2 = []

    for z in range(0, y):
        rucksack1.append(items[z])
        
    for z in range(y, x):
        rucksack2.append(items[z])

    dupes = set(rucksack1).intersection(rucksack2)
    for dupe in dupes:
        result_a += getpriorities(dupe)

    counter += 1
    sets.append(items)
    if counter%3 == 0:
        dupes = set(sets[0]).intersection(sets[1], sets[2])
        for dupe in dupes:
            result_b += getpriorities(dupe)
        sets = []
        
print(result_a)
print(result_b)


