# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 22:53:58 2016

@author: Ken
"""

#==============================================================================
#   Clock needs to be able to:
#   Print HH:MM as a string X
#   Add or subtract in minutes units X
#   Operate independent of date (like a wall clock) X
#   Formatted in military time X
#   Two objects must be comparable X
#   Must be callable X # Not true
#   Must be able to add minutes X
#==============================================================================

class Clock(object):
    def __init__(self, hours, minutes):
        hours_carried = 0
        if 0 <= minutes < 60:
            self.minutes = minutes
        else:
            hours_carried, self.minutes = divmod(minutes, 60)
        self.hours = (hours + hours_carried)%24
        
    def __str__(self):
        return '{:02d}:{:02d}'.format(self.hours, self.minutes)
        # Python 3 str formatting
        # 0 is leading digit, 2 digits, d is for formatting integer
    def __eq__(self,other):
        return self.hours == other.hours and self.minutes == other.minutes
    
    def add(self, num_minutes):
        # adds minutes to existing clock
        hours_carried = 0
        new_minutes = self.minutes + num_minutes
        if 0 <= new_minutes < 60:
            self.minutes = new_minutes
        else:
            hours_carried, self.minutes = divmod(new_minutes, 60)
        self.hours = (self.hours + hours_carried)%24
        return '{:02d}:{:02d}'.format(self.hours, self.minutes)

"""
Originally, I thought a __call__ method was necessary since Clock was a class
 and not a func, but turns out that was wrong.
"""