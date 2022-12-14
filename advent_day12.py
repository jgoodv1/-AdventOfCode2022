#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:41:52 2022

@author: jonathangood
"""

import numpy as np
from heapq import heappop, heappush

area_row = 5
area_col = 8

moves = ['U', 'D', 'L', 'R']
lastMoves = {'U':[0,2,3], 'D':[1,2,3], 'L':[0,1,3], 'R':[0,1,3]}
START = (20,0)
TARGET = (20,91)
CHECKROUTE = []

VISITED = {}
AREA = {}

transition_reward, win_state_reward, lose_state_reward = -2, 10, -10


import csv
with open('input12.txt', 'r') as fd:
    reader = csv.reader(fd)
    i = 0
    for row in reader: 
        j = 0
        for mountain in row[0]:
            if mountain == 'S':
                START = (i,j)
                AREA[(i, j)] = 'a'
                CHECKROUTE.append((i,j))
            elif mountain == 'E':
                TARGET = (i,j)
                AREA[(i, j)] = 'z'
            else:
                AREA[(i, j)] = mountain
                if mountain == 'a':
                    CHECKROUTE.append((i,j))
            VISITED[(i, j)] = False
            j += 1
        i += 1
    area_row = i
    area_col = j

class Climber:
    def __init__(self, area, visited, start, target=TARGET):        
        self.state = start  
        self.start = start
        self.target = target
        self.visited = visited
        self.area = area
        

    def nxtPosition(self, action):    
        
        if action == 'U':                
            nxtState = (self.state[0] - 1, self.state[1])                
        elif action == 'D':
            nxtState = (self.state[0] + 1, self.state[1])
        elif action == 'L':
            nxtState = (self.state[0], self.state[1] - 1)
        elif action == 'R':
            nxtState = (self.state[0], self.state[1] + 1)   

        if (nxtState[0] >= 0) and (nxtState[0] <= (area_row-1)):
            if (nxtState[1] >= 0) and (nxtState[1] <= (area_col-1)): 
                return nxtState
        return self.state
        
    def checkMove(self, s):
               
        try:
            score = ord(self.area[s]) - ord(self.area[self.state])
            
            if s == self.state:
                return False
            if score <= 1:
                return True
        except KeyError:
            return False
        
        return False
     
    def getallowedmoves(self):
        allowedmoves = []
        for m in moves:
            S = self.nxtPosition(m)
            if self.checkMove(S):
                allowedmoves.append(S)
                
        return allowedmoves

        
    def findpath(self):
        heap = [(0, self.start[0], self.start[1])]
        
        while True:  
            try:
                steps, i, j = heappop(heap)
            except IndexError:
                break
            
            m = (i,j)
            
            if self.visited[m]:
                continue
            self.visited[m] = True
            
            if m == self.target:
                return steps
            self.state = m

            for move in self.getallowedmoves():
                heappush(heap, (steps+1, move[0], move[1]))                                          
 
copy=VISITED.copy()
Me = Climber(AREA, copy, START, TARGET)

print(Me.findpath())

results = []
for route in CHECKROUTE:
  copy=VISITED.copy()
  New = Climber(AREA, copy, route, TARGET)
  result = New.findpath()
  if result == None:
      continue
  results.append(result)

results.sort()  

print(results)

