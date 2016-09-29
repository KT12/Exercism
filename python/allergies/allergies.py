# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 11:29:55 2016

@author: Ken
"""

#==============================================================================
#   Write a program that, given a person's allergy score, 
#   can tell them whether or not they're allergic to a given item, 
#   and their full list of allergies.
#
#   Using a bitwise operator to compare allergy score and possible allergies.
#==============================================================================

allergen_dict = {'eggs'          :   1, # bin(1) = 0b1
                 'peanuts'       :   2, # bin(2) = 0b10
                 'shellfish'     :   4,
                 'strawberries'  :   8,
                 'tomatoes'      :   16,
                 'chocolate'     :   32,
                 'pollen'        :   64,
                 'cats'          :   128}

class Allergies(object):
    
    def __init__(self, score):
        self.score = score
        lst = [trigger for trigger, num in allergen_dict.items() if num & self.score]
        self.lst = lst
        
    def is_allergic_to(self, allergen):
        self.allergen = allergen
        return bool(allergen_dict[self.allergen] & self.score)