#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:00:23 2022

@author: jonathangood
"""

packetfound = 'N'

import csv
with open('input6.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader: 
        buffer_sop = []
        buffer_som = []
        count = 1
        datastream = row[0]
        for signal in datastream:
            buffer_sop.append(signal)
            buffer_som.append(signal)
            
            """
            Part 1
            """
            if len(buffer_sop) == 5:
                del buffer_sop[0]
                           
            if len(buffer_sop) == 4 and packetfound == 'N':
                if len(set(buffer_sop)) == 4:
                    print('Start of Packet: ', count)
                    packetfound = 'Y'
            
            """
            Part 2
            """
            if len(buffer_som) == 15:
                del buffer_som[0]
                           
            if len(buffer_som) == 14:
                if len(set(buffer_som)) == 14:
                    print('Start of Message: ', count)
                    break
                    
                
            count += 1