#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 10:11:23 2022

@author: jonathangood
"""

cycleDict = {"addx":2,"noop":1}
printCycles = [20,60, 100, 140, 180,220]
screen = [41,81,121,161,201,241]

input = []
import csv
with open('input10.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader: 
        input.append(row[0])
        
cycle = 1
signalStrength = 1
totalX = 0
position = 0
screenrow = ''
sprite = [1]
for x in range(0,len(input)):
    
    cmd = input[x][0:4]
  
    for y in range(0, cycleDict[cmd]):
        
        #print('Start cycle ', cycle, ': begin executing ', input[x]) 
        
        if cmd != 'noop' and y == 1:
            l = len(input[x])
            signalStrength += int(input[x][5:l])
        
        if position + 1 in (sprite):
            screenrow+= '#'
        else:
            screenrow+= '.'
        
       # print ('During cycle ',cycle,': CRT draws pixel in position ', position)
       # print('Current CRT row:',screenrow)
        
        cycle += 1
        position += 1
        
        if cycle in screen:
            print(screenrow)
            screenrow = ''
            position = 0
        
        if cycle in printCycles:
           #print(cycle,': ', signalStrength, signalStrength*cycle)
           totalX += signalStrength * cycle
        sprite = range(signalStrength,signalStrength+3)
       # print(sprite)
          
        
        
       
print('Total: ', totalX)