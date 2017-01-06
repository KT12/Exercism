#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 20:56:23 2017

@author: ktt
"""

class Garden(object):

	pp = {"G":"Grass",
    	  "C":"Clover",
    	  "R":"Radishes",
    	  "V":"Violets"}

	ss = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
		"Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

	def __init__(self, diagram, students=ss):
		self.row_1 = diagram.split()[0] #now two lists
		self.row_2 = diagram.split()[1]
		self.ss = sorted(students)

	def plants(self, name):
		self.indices = [2 * self.ss.index(name), 2 * self.ss.index(name)+ 1]
		row_1_plants = []
		row_2_plants = []
		for j in self.indices:
			for k in self.row_1[j]:
				row_1_plants.append(self.pp[k])
		for j in self.indices:
			for k in self.row_2[j]:
				row_2_plants.append(self.pp[k])
		# row_1_plants = [pp[k] for k in self.row_1[j] for j in self.indices]
		# row_2_plants = [pp[k] for k in self.row_2[j] for j in self.indices]
		return row_1_plants + row_2_plants