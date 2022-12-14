#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:27:34 2022

@author: jonathangood
"""
import time, csv
start = time.time()

STACK_ROWS = 50
STACK_COLS = 9
STACKS = {}  

def displaystacks():
    global STACKS, STACK_ROWS, STACK_COLS
    for i in range(30, STACK_ROWS):
        print('------------------------------------------------------')
        out = '|'
        for j in range(0, STACK_COLS):
            out +=   STACKS[i,j].ljust(3) + ' | '
        print(out)
     
    print('------------------------------------------------------')

def gettopcrate(row, n):
    global STACKS, STACK_ROWS
    for x in range(0, STACK_ROWS):
        crates = []
        crate = STACKS[x,row-1]
        if crate != '':
            for y in range(0,n):
                crate = STACKS[x+y,row-1]
                crates.append(crate)
                STACKS[x+y,row-1] = ''
            return crates
    return crates

def movecrate(row_from, row_to, n):
    global STACKS, STACK_ROWS
    moved = 'N'
    offset = 0
    crate_move = gettopcrate(row_from, n)    

    for x in range(0, STACK_ROWS):
        crate = STACKS[x,row_to-1]    
        if crate != '':
            for c in crate_move:
                STACKS[x-n+offset,row_to-1] = c
                offset+=1
            moved = 'Y'
            break
    if moved == 'N':
        for c in crate_move:
            STACKS[STACK_ROWS-n+offset,row_to-1] = c
            offset+=1     

# Stacks input
row_n = 0
with open('input5a.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader: 
        col_n = 0
        n = 4
        try:
            chunks = [row[0][i:i+n] for i in range(0, len(row[0]), n)]
        except IndexError:
            chunks = ['','','','','','','','','']
        for c in chunks:
            STACKS[row_n, col_n] = c.replace(' ','')
            col_n += 1
        row_n += 1

# Moves input
file = []
with open('input5b.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader: 
        move = row[0].replace('move ','').replace(' from ',',').replace(' to ',',').split(',')
        file.append(move)
 
"""
Part 1
"""
STACKS_ORGINAL = STACKS.copy()
for move in file:   
    for x in range(0,int(move[0])):
        movecrate(int(move[1]),int(move[2]),1)                

# Part 1 Answer
print('Part 1: ')
displaystacks()

"""
Part 2
"""
STACKS = STACKS_ORGINAL
for move in file:
    movecrate(int(move[1]),int(move[2]),int(move[0])) 

# Part 2 Answer
print('Part 2: ')
displaystacks()
print('Total time:', (time.time()-start),' seconds')    


