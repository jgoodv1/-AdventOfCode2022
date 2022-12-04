#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:43:05 2022

@author: jonathangood
"""

total_calories = []
count = 0

import csv
with open('input1.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        if row:
            count += int(row[0])
        else:
            total_calories.append(count)
            count = 0

# Part 1 Answer
print(max(total_calories))

total_calories.sort(reverse=True)

# Part 2 Answer 
print(sum(total_calories[0:3]))
