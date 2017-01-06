#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 12:36:02 2017

@author: ktt
"""

# Passed all tests using defaultdict instead of list of tuples

from collections import defaultdict

class School():
    
    def __init__(self, name):
        self.name = name
        self.student_dict = defaultdict(set)
        
    def add(self, s_name, g):
        self.student_dict[g].add(s_name)
    
    def grade(self, num):
        return self.student_dict[num]
    
    def sort(self):
        return sorted((g, tuple(sorted(s_name))) for g, s_name in
                      self.student_dict.items())
