#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 10:37:42 2022

@author: jonathangood
"""

def mod(new, test):
    res = 0
    num = str(new)
    for x in range(0, len(num)):
        res = (res * 10 + int(num[x])) % test;
 
    return res;

class Monkey:
    def __init__(self, count, items, operation, test, throw, divide=False):        
        self.count = count  
        self.items = items
        self.operation = operation
        self.test = test
        self.throw = throw
        self.divide = divide

    def checkitems(self):
        for item in self.items:
            new = self.operation(item)
            if self.divide == True:
                new = int(new/3)
            new %= max_worry
            if new % self.test == 0:
               self.throw[0].additem(new)
            else:
               self.throw[1].additem(new)
            self.count += 1
        self.items = []
        
    def additem(self, item):
       self.items.append(item)
              
Monkey0 = Monkey(0, [92, 73, 86, 83, 65, 51, 55, 93], lambda x: x * 5, 11, [])
Monkey1 = Monkey(0, [99, 67, 62, 61, 59, 98], lambda x: x * x, 2, [])
Monkey2 = Monkey(0, [81, 89, 56, 61, 99], lambda x: x * 7, 5, [])
Monkey3 = Monkey(0, [97, 74, 68], lambda x: x + 1, 17, [])
Monkey4 = Monkey(0, [78, 73],lambda x: x + 3, 19, [])
Monkey5 = Monkey(0, [50],lambda x: x + 5, 7, [])
Monkey6 = Monkey(0, [95, 88, 53, 75],lambda x: x + 8, 3, [])
Monkey7 = Monkey(0, [50, 77, 98, 85, 94, 56, 89],lambda x: x + 2, 13, [])

Monkey0.throw = [Monkey3,Monkey4]
Monkey1.throw = [Monkey6,Monkey7]
Monkey2.throw = [Monkey1,Monkey5]
Monkey3.throw = [Monkey2,Monkey5]
Monkey4.throw = [Monkey2,Monkey3]
Monkey5.throw = [Monkey1,Monkey6]
Monkey6.throw = [Monkey0,Monkey7]
Monkey7.throw = [Monkey4,Monkey0]

max_worry = Monkey0.test * Monkey1.test * Monkey2.test  * Monkey3.test * Monkey4.test  * Monkey5.test * Monkey6.test * Monkey7.test

for x in range(0,10000):
    Monkey0.checkitems()
    Monkey1.checkitems()
    Monkey2.checkitems()
    Monkey3.checkitems()
    Monkey4.checkitems()
    Monkey5.checkitems()
    Monkey6.checkitems()
    Monkey7.checkitems()

totals = [Monkey0.count, Monkey1.count, Monkey2.count, Monkey3.count, Monkey4.count, Monkey5.count, Monkey6.count, Monkey7.count]
print(totals)
totals.sort()

print(totals[7] * totals[6])




