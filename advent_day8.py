#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:59:04 2022

@author: jonathangood
"""

tree_row = 0
tree_col = 0

forest = {}

import csv
with open('input8.txt', 'r') as fd:
    reader = csv.reader(fd)
    i = 0
    for row in reader: 
        j = 0
        for tree in row[0]:
            forest[(i, j)] = tree
            j += 1
        i += 1
    tree_row = i
    tree_col = j
    

def countnotvisible():
    count = 0
    for i in range(0, tree_row - 1):            
        for j in range(1, tree_col-1):
            if not istreevisible(i, j, forest[i,j]):
                count += 1
    return count
        
def countvisible():
    count = (tree_row * tree_col) - countnotvisible()
    return count

def istreevisible(row, col, size):
    visible, count = checkcol(reversed(range(0, row)), col, size)
    if visible == True:
        return True
    
    visible, count = checkcol(range(row+1, tree_row), col, size)
    if visible == True:
        return True
    
    visible, count = checkrow(reversed(range(0, col)), row, size)
    if visible == True:
        return True
    
    visible, count = checkrow(range(col+1, tree_col), row, size)
    return visible
 
def calcscenicscore(row, col, size):
    totalcount = 0
    visible, count = checkcol(reversed(range(0,row)), col, size)
    totalcount = count
    if visible == True:
        return totalcount

    visible, count = checkcol(range(row+1, tree_row), col, size)
    totalcount *= count
    if visible == True:
        return totalcount

    visible, count = checkrow(reversed(range(0, col)), row, size)
    totalcount *= count
    if visible == True:
        return totalcount

    visible, count = checkrow(range(col+1, tree_col), row, size)
    totalcount *= count
    if visible == True:
        return totalcount

    return totalcount

def getmaxsorce():
    maxscore = 0
    for i in range(0, tree_row):            
        for j in range(0, tree_col):
            score = calcscenicscore(i, j, forest[i,j])
            if score > maxscore:
                maxscore = score

    return maxscore
   
def checkrow(range, row, size):
    count = 0
    for c in range:
        count += 1
        if int(forest[row,c]) >= int(size):
            return False, count
    return True, count

def checkcol(range, col, size):
    count = 0
    for r in range:
        count += 1
        if int(forest[r,col]) >= int(size):
            return False, count
    return True, count

print(countvisible())
print(getmaxsorce())




