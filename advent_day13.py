#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 07:36:53 2022

@author: jonathangood
"""

signals = []
packets = []
n = 0

f = open("input13.txt", "r")
for x in f:
  line = x.strip()
  if line:
      packets.append(eval(line)) 
      if n == 1:
          signals.append(packets)
          packets = []
          n = 0
      else:
          n+= 1

def compareArrays(a, b):
    
    terminate = None
    
    
    if type(a) != list:
        a = [a]
        #print('Mixed types; convert left to ',str(a), ' and retry comparison')
    if type(b) != list:
        b = [b]
        #print('Mixed types; convert right to ',str(b), ' and retry comparison')
    
    for x in range(0,len(a)):
        
        ax = a[x]
        try:
            bx = b[x]
        except IndexError:
            #print('Right side ran out of items, so inputs are not in the right order')
            return False
        #print('Compare ', str(ax),' vs ', str(bx))
        if type(ax) == int and type(bx) == int:
           if ax == bx:
               continue
           if ax < bx:
               #print('Left side is smaller, so inputs are in the right order')
               return True               
           else:
               #print('Right side is smaller, so inputs are not in the right order')
               return False               
        else:
            terminate = compareArrays(ax, bx)
            if terminate != None:
                return terminate    
    if len(a) == len(b):
        return None
    else:
        return True

def checksignal(a, b):
    result = None
    for x in range(0,len(a)):
        ax = a[x]
        try:
            bx = b[x]
        except IndexError:
            #print('Right side ran out of items, so inputs are not in the right order')
            result =  False
            break
        
        result = compareArrays(ax, bx)
        if result != None:
            break
    #print('Result', result)
    if result == None:
        #print('Left side ran out of items, so inputs are in the right order')
        return True
    else:
        return result

count = 0
allpackets = [[2],[6]]

for i, signal in enumerate(signals, start=1):
    x1, x2 = signal
    #print('== Input ', str(i), ' ==', x1, x2)
    if checksignal(x1,x2):
        count += (i)
    allpackets.append(x1)
    allpackets.append(x2)

print(count)

def bubbleSort(packets):
     
    n = len(packets)
 
    # For loop to traverse through all
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            #is greater than the adjacent element
            if checksignal(packets[j + 1], packets[j]):
                packets[j], packets[j + 1] = packets[j + 1], packets[j]
                 

bubbleSort(allpackets)

print(allpackets)
loc_div_two = allpackets.index([2]) + 1 # Packets are numbered from 1
loc_div_six = allpackets.index([6]) + 1

print( loc_div_two * loc_div_six)


