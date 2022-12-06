#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:27:34 2022

@author: jonathangood
"""

stack_rows = 50
stack_cols = 9
stacks = {}  

def displaystacks():
    for i in range(0, stack_rows):
        print('------------------------------------------------------------------------')
        out = '|'
        for j in range(0, stack_cols):
            out +=   stacks[i,j].ljust(5) + ' | '
        print(out)
     
    print('------------------------------------------------------------------------')

def gettopcrate(row, n):
    for x in range(0, stack_rows):
        crates = []
        crate = stacks[x,row-1]
        if crate != '':
            for y in range(0,n):
                crate = stacks[x+y,row-1]
                crates.append(crate)
                stacks[x+y,row-1] = ''
            return crates
    return crates

def movecrate(row_from, row_to, n):
    moved = 'N'
    offset = 0
    crate_move = gettopcrate(row_from, n)    

    for x in range(0, stack_rows):
        crate = stacks[x,row_to-1]    
        if crate != '':
            for c in crate_move:
                stacks[x-n+offset,row_to-1] = c
                offset+=1
            moved = 'Y'
            break
    if moved == 'N':
        for c in crate_move:
            stacks[stack_rows-n+offset,row_to-1] = c
            offset+=1     
      
for i in range(stack_rows):
    for j in range(stack_cols):
        stacks[(i, j)] = ''  # set initial value to 0
        
row_n = 0

import csv
with open('input5a.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader: 
        col_n = 0
        n = 4
        try:
            chunks = [row[0][i:i+n] for i in range(0, len(row[0]), n)]
        except IndexError as e:
            chunks = ['','','','','','','','','']
        for c in chunks:
            stacks[row_n, col_n] = c.replace(' ','')
            col_n += 1
        row_n += 1

file = []
with open('input5b.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader: 
        move = row[0].replace('move ','').replace(' from ',',').replace(' to ',',').split(',')
        file.append(move)
 
for move in file:
    
    #for x in range(0,int(move[0])):
        #movecrate(int(move[1]),int(move[2]),1)                
    movecrate(int(move[1]),int(move[2]),int(move[0])) 
 
displaystacks()

