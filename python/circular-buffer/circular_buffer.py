#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 20:33:31 2017

@author: ktt
"""

# Buffer must be able to read, write, overwrite, clear
# Reading clears the read items from the buffer
# Also properly raise BufferFullException, BufferEmptyException

import random

class CircularBuffer(object):
    
    def __init__(self, n):
        self.n = n # n is predefined length of buffer
        self.buffer = ['' for _ in range(self.n)] # blank list of len n
        self.cursor = random.randrange(self.n) # buffer starts at random point
    
    def clear(self):
        self.buffer = ['' for _ in range(self.n)]
        
    def write(self, ss):
        if self.buffer[self.cursor] == '':
            self.buffer[self.cursor] = ss
            self.cursor = (self.cursor + 1) % self.n
        else:
            raise BufferFullException
    
    def read(self):
        if self.buffer == ['' for _ in range(self.n)]:
            raise BufferEmptyException
        else:
            if self.buffer[self.cursor] != '':
                out = self.buffer[self.cursor]
                self.buffer[self.cursor] = ''
                return out
            else:
                self.cursor = (self.cursor + 1) % self.n
                return self.read()  # recursively read until data found
    
    def overwrite(self, ss):
        self.buffer[self.cursor] = ss
        self.cursor = (self.cursor + 1) % self.n

class BufferFullException(Exception):
    pass

class BufferEmptyException(Exception):
    pass