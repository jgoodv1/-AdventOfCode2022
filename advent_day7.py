#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:21:32 2022

@author: jonathangood
"""

cmds = []

import csv
with open('input7.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader: 
        cmds.append(row[0])

backdir = '$ cd ..'

class directory:
    def __init__(self,dirname,size):
        self.dirname = dirname
        self.size = size
    def updatesize(self, size):
        self.size += size
        return size

def totalsizedirectory(dirname, parentdir, files, totals):
    cmdcount = 1
    cmdprocessed = 0
    
    dirname = files[0][4:6]
    del files[0]
    thisdir = directory(dirname, 0)

    for n in range(0, len(files)):
        file = files[n]
        if cmdprocessed > 0:
            cmdprocessed -= 1
        else:   
            if file[0:1] != '$' and file[0:3] != 'dir':
                size = file[0:file.find(' ')]
                thisdir.updatesize(int(size))
            if file[0:4] == '$ cd' and file != backdir: 
                cmdprocessed = totalsizedirectory(file, thisdir, files[n:len(files)], totals)
            if file == backdir:
                break
        cmdcount += 1
    parentdir.updatesize(thisdir.size)
    totals.append(thisdir)
    return cmdcount

    
totals = []
begin = directory('/',0)
y= totalsizedirectory('/', begin, cmds, totals)

"""
Part 1
"""

sumtotal = 0
totaluse = 0
for t in totals:
    if t.size <= 100000:
        sumtotal += t.size
    if t.dirname == ' /':
        totaluse += t.size

print('Part 1 Total: ', sumtotal)

"""
Part 2
"""

freespace =  70000000 - totaluse
requiredspace = 30000000 - freespace

driveoptions = {}
for t in totals:
    if t.size >= requiredspace:
        print(t.dirname, t.size)
        driveoptions.update({t.dirname: t.size})

sorteddrive = sorted(driveoptions.items(), key=lambda x:x[1])

print('Part 2: ', sorteddrive[0])
