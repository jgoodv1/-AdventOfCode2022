#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:05:12 2022

@author: jonathangood
13484
"""

import csv, time

scores, points, win = {"W":6, "D":3, "L":0}, {"X":1, "Y": 2, "Z":3}, {"X":"Z", "Y":"X", "Z":"Y"}
# Look up for Part 1 and 2
translate_a, translate_b = {"A":"X", "B":"Y", "C":"Z"}, {"X":"L", "Y":"D", "Z":"W"}
lose = {v: k for k, v in win.items()}

file = []
with open('input2.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        elf, blank, mine = row[0]
        file.append([elf, mine])

"""
Part 1
"""
start = time.time()
score = 0

for row in file:
    elf, mine = row
    score += points[mine]
    elf = translate_a[elf]

    if elf == mine:
        score += scores["D"]
    elif win[elf] == mine:
        score += scores["L"]
    else:
        score += scores["W"]

# Part 1 Answer
print('Part 1: ', score,'\n')

"""
Part 2
"""
score = 0

for row in file:
    elf, mine = row
    elf = translate_a[elf]
    result = translate_b[mine]
    score += scores[result]

    if result == 'D':
        score += points[elf]
    elif result == 'L':
        score += points[win[elf]]
    else:
        score += points[lose[elf]]

# Part 2 Answer
print('Part 2: ', score,'\nTotal time:', (time.time()-start),' seconds')

