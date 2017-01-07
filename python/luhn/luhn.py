#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 18:27:20 2017

@author: ktt
"""

class Luhn(object):
    def __init__(self, number=None):
        self.number = number
    
    
    def addends(self):
        num = (str(self.number))[::-1]
        add = []
        for k in range(len(num)):
            if k%2 == 0:
                add.append(int(num[k]))
            else:
                if 2 * int(num[k]) > 9:
                    add.append(2 * int(num[k]) - 9)
                else:
                    add.append(2 * int(num[k]))
        self.add = add
        return add
        
    def checksum(self):
        return sum(self.addends())
                
    def is_valid(self):
        return self.checksum()%10 == 0
    
    @staticmethod
    def create(num):
        if Luhn(num*10).is_valid():
            return num*10
        else:
            c = str(10 - (Luhn(num * 10).checksum()%10))
            return int(str(num) + c)
            