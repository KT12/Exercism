#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 20:33:31 2017

@author: ktt
"""

# Buffer must be able to read, write, overwrite, clear
# Reading clears the read items from the buffer
# Also properly raise BufferFullException, BufferEmptyException

class CircularBuffer(object):
    
    def __init__(self, n):
        self.n = n # n is predefined length of buffer
        self.buffer = ['' for _ in range(self.n)] # creates blank list of len n
    
    def clear(self):
        self.buffer = ['' for _ in range(self.n)]
        return self.buffer
        
    def write(self, ss):
        if '' in self.buffer:
            while ss not in self.buffer:
                for k in range(len(self.buffer)):
                    if self.buffer[k] == '':
                        self.buffer[k] = ss
            self.buffer.sort()
        else:
            raise Exception('BufferFullException')
    
    def read(self):
        if self.buffer == ['' for _ in range(self.n)]:
            raise Exception('BufferEmptyException')
        else:
            for k in self.buffer:
                if k != '':
                    return k