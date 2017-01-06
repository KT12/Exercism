#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 12:36:02 2017

@author: ktt
"""

class School():
    
    def __init__(self, name):
        self.name = name
        self.student_list = []
        
    def add(self, s_name, g):
        self.student_list.append((g, s_name))
    
    def grade(self, num):
        return tuple(self.student_list[k][1] for k in
                     range(len(self.student_list))
                     if self.student_list[k][0] == num)
    
    def sort(self):
        return sorted(self.student_list)