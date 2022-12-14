#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:46:06 2022

@author: jonathangood
"""
import time
start = time.time()

def createarray(values):
    y = int(values.split('-')[0])
    z = int(values.split('-')[1])
    result = []
    
    for x in range(y,z+1):
        result.append(x)
        
    return result

part1 = 0
part2 = 0

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
            part1 += 1
        """
        Part 2
        """
        if len(overlap) > 0:
            part2 += 1

# Part 1 Answer
print('Part 1: ', part1)

# Part 2 Answer
print('Part 2: ', part2,'\nTotal time:', (time.time()-start),' seconds')
