# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 13:29:39 2016

@author: Ken
"""

#==============================================================================
#   Write a robot simulator.
#
#   A robot factory's test facility needs a program to verify robot movements.
#   The robots have three possible movements:
#   turn right
#   turn left
#   advance
#
#   Robots are placed on a hypothetical infinite grid, 
#   facing a particular direction (north, east, south, or west) 
#   at a set of {x,y} coordinates, e.g., {3,8}, 
#   with coordinates increasing to the north and east.
#
#   The robot then receives a number of instructions, at which point 
#   the testing facility verifies the robot's new position, 
#   and in which direction it is pointing.
#   
#   The letter-string "RAALAL" means:
#   Turn right
#   Advance twice
#   Turn left
#   Advance once
#   Turn left yet again
#
#   Say a robot starts at {7, 3} facing north.  Then running this stream of 
#   instructions should leave it at {9, 4} facing west.
#==============================================================================

bearing_dict =      {'N'    :   'NORTH',
                     'S'    :   'SOUTH',
                     'W'    :   'WEST',
                     'E'    :   'EAST'}
                     
class Robot(object):
                         
    def __init__(self, bearing='NORTH', x=0, y=0):
        if bearing in bearing_dict.keys():
            self.bearing = bearing_dict[bearing] # To handle NSWE inputs
        else:
            self.bearing = bearing.upper() # Will handle lowercase
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

    def advance(self):
        if self.bearing == 'NORTH':
            self.y += 1
            self.coordinates = (self.x, self.y)
        elif self.bearing == 'SOUTH':
            self.y -= 1
            self.coordinates = (self.x, self.y)
        elif self.bearing == 'EAST':
            self.x += 1
            self.coordinates = (self.x, self.y)
        elif self.bearing == 'WEST':
            self.x -= 1
            self.coordinates = (self.x, self.y)
        else:
            raise ValueError

    def turn_left(self):
        if self.bearing == 'NORTH':
            self.bearing = 'WEST'
        elif self.bearing == 'SOUTH':
            self.bearing = 'EAST'
        elif self.bearing == 'EAST':
            self.bearing = 'NORTH'
        elif self.bearing == 'WEST':
            self.bearing = 'SOUTH'
        else:
            raise ValueError
    
    def turn_right(self):
        if self.bearing == 'NORTH':
            self.bearing = 'EAST'
        elif self.bearing == 'SOUTH':
            self.bearing = 'WEST'
        elif self.bearing == 'EAST':
            self.bearing = 'SOUTH'
        elif self.bearing == 'WEST':
            self.bearing = 'NORTH'
        else:
            raise ValueError
    
    def simulate(self, commands):
        for char in commands:
            if char == 'A':
                self.advance()
            elif char == 'L':
                self.turn_left
            elif char == 'R':
                self.turn_right