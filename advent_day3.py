#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:00:29 2022

@author: jonathangood
"""
import time
start = time.time()
file, sets = [], []
part1, part2, counter= 0, 0, 0

with open("input3.txt") as fd:
    file = fd.read().strip().split("\n")

def getpriorities(item):
    result = 0
    if item.isupper():
        check = item.lower()
        result += (ord(check) - 96) + 26
    else:
        result += ord(item) - 96

    return result

for items in file:
    """
    Part 1
    """
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
        part1 += getpriorities(dupe)

    """
    Part 2
    """
    counter += 1
    sets.append(items)
    if counter%3 == 0:
        dupes = set(sets[0]).intersection(sets[1], sets[2])
        for dupe in dupes:
            part2 += getpriorities(dupe)
        sets = []

# Part 1 Answer
print('Part 1: ', part1)

# Part 2 Answer
print('Part 2: ', part2,'\nTotal time:', (time.time()-start),' seconds')
