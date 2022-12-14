#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 07:48:08 2022

@author: jonathangood
"""

input = []


step_rows = 1000
step_cols = 1000
START = (500,500)
state = {}
statetracker = {}  
tolernce = [-1,0,1]
track = {}

import csv
with open('input9.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader: 
        input.append(row[0])
        

for i in range(0, step_rows):            
    for j in range(0, step_cols):
        statetracker[i,j] = '.'
statetracker[START] = '#'
        
class State:
    def __init__(self, tracking, state=START, tracker=statetracker):        
        self.state = state  
        self.tracker = tracker
        self.tracking = tracking
        self.count = 1

    def nxtPosition(self, actions):    
        nxtState = self.state
        for action in actions:
            if action == 'U':                
                nxtState = (self.state[0] - 1, self.state[1])                
            elif action == 'D':
                nxtState = (self.state[0] + 1, self.state[1])
            elif action == 'L':
                nxtState = (self.state[0], self.state[1] - 1)
            elif action == 'R':
                nxtState = (self.state[0], self.state[1] + 1)   
            self.state = nxtState
        if self.tracker[nxtState] == '.' and self.tracking:
            self.count += 1
            self.tracker[nxtState] = '#' 
        #if self.tracking:
            #self.displaystate()
        return nxtState
    
    def displaystate(self):
        for i in range(0,5):
            print('------------------------')
            out = '|'
            for j in range(0, 6):
                out +=  self.tracker[i,j].ljust(1) + ' | '
            print(out)
         
        print('------------------------')
    
class Agent:
    def __init__(self, tracking):
        self.State = State(tracking)

       
def checkdistance(AgentH, AgentT):
    moves = []
    distV = AgentH.State.state[0] - AgentT.State.state[0]
    distH = AgentH.State.state[1] - AgentT.State.state[1]

    if distV not in tolernce or (distH not in tolernce and distV !=0):
        if distV < 0:
            moves.append('U')
        else:
            moves.append('D')

    if distH not in tolernce or (distV not in tolernce and distH !=0):
        if distH < 0:
            moves.append('L')
        else:
            moves.append('R')
    return moves

def updatestate(AgentH, AgentT):
    moves = checkdistance(AgentH, AgentT)
    return moves
 
TAIL = Agent(True)   
T1 = Agent(False)  
T2 = Agent(False)
T3 = Agent(False)
T4 = Agent(False)
T5 = Agent(False)
T6 = Agent(False)
T7 = Agent(False)
T8 = Agent(False)
HEAD = Agent(False)

for i in input:
   m = i[0]
   n = int(i[2:len(i)])
   for x in range(0,n):
       HEAD.State.nxtPosition([m])
       T1.State.nxtPosition(updatestate(HEAD, T1))
       T2.State.nxtPosition(updatestate(T1, T2))
       T3.State.nxtPosition(updatestate(T2, T3))
       T4.State.nxtPosition(updatestate(T3, T4))
       T5.State.nxtPosition(updatestate(T4, T5))
       T6.State.nxtPosition(updatestate(T5, T6))
       T7.State.nxtPosition(updatestate(T6, T7))
       T8.State.nxtPosition(updatestate(T7, T8))
       TAIL.State.nxtPosition(updatestate(T8, TAIL))
       #print( 'HEAD ', HEAD.State.state, ' TAIL ', TAIL.State.state)

print(TAIL.State.count)


