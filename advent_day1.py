#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:43:05 2022

@author: jonathangood
"""
import time

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

"""
Part 1
"""
start = time.time()

# Part 1 Answer
part1 = max(total_calories)
print('Part 1: ', part1,'\n')

"""
Part 2
"""
total_calories.sort(reverse=True)

# Part 2 Answer
part2 = sum(total_calories[0:3])
print('Part 2: ', part2,'\nTotal time:', (time.time()-start),' seconds')
