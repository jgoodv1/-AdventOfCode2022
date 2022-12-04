#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:46:06 2022

@author: jonathangood
"""

def createarray(values):
    y = int(values.split('-')[0])
    z = int(values.split('-')[1])
    result = []
    
    for x in range(y,z+1):
        result.append(x)
        
    return result

count_a = 0
count_b = 0

import csv
with open('input4.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader: 
        elf1 = createarray(row[0])
        elf2 = createarray(row[1])
        
        overlap = set(elf1).intersection(elf2)
        
        """
        Part 1
        """
        if len(overlap) == len(elf1) or len(overlap) == len(elf2):
            count_a += 1
        """
        Part 2
        """
        if len(overlap) > 0:
            count_b += 1

# Part 1 Answer   
print(count_a)
# Part 2 Answer
print(count_b)
