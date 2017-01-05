# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 22:16:56 2016

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
NORTH, EAST, SOUTH, WEST = range(4)

class Robot(object):
                         
    def __init__(self, bearing=NORTH, x=0, y=0):
        if bearing not in range(0,4):
            raise ValueError
        else:
            self.bearing = bearing
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        elif self.bearing == EAST:
            self.x += 1
        elif self.bearing == WEST:
            self.x -= 1
        else:
            raise ValueError
        self.coordinates = (self.x, self.y)

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4
    
    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4
    
    def simulate(self, commands):
        for char in commands:
            if char == 'A':
                self.advance()
            elif char == 'L':
                self.turn_left()
            elif char == 'R':
                self.turn_right()
            else:
                raise ValueError