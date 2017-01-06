#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 14:28:01 2017

@author: ktt
"""

class roman_numerals(object):
    
    def __init__(self):
        # No arguments to instantiate the class
        pass
    
    def numeral(self, arabic):
        # Returns Roman equivalent of arabic numeral
        # Assumes input is int
        # Out of range num raise error
        self.arabic = arabic
        
        if self.arabic > 3000 or self.arabic < 0:
            raise ValueError
        
        self.s_arabic = str(self.arabic)
        self.places = len(self.s_arabic)
        
        self.thous, self.hunds, self.tens, self.ones = None,None,None,None
        
        if self.places == 4:
            self.thous, self.hunds, self.tens, self.ones = str(self.arabic)
        elif self.places == 3:
            self.hunds, self.tens, self.ones = str(self.arabic)
        elif self.places == 2:
            self.tens, self.ones = str(self.arabic)
        elif self.places == 1:
            self.ones = str(self.arabic)
        
        return (self.thousands(self.thous) + self.hundreds(self.hunds) +
                self.tens_p(self.tens) + self.ones_p(self.ones))
    
    def thousands(self, th):
        self.thous_dict = {'3': 'MMM',
                      '2': 'MM',
                      '1': 'M'}
        if self.thous:
            return self.thous_dict[th]
        else:
            return ''
    
    def hundreds(self, hh):
        
        self.hunds_dict = {'0': '',
                      '1': 'C',
                      '2': 'CC',
                      '3': 'CCC',
                      '4': 'CD',
                      '5': 'D',
                      '6': 'DC',
                      '7': 'DCC',
                      '8': 'DCCC',
                      '9': 'CM'}
        if self.hunds:
            return self.hunds_dict[hh]
        else:
            return ''
    
    def tens_p(self, tn):
        self.tens_dict = {'0': '',
                     '1': 'X',
                     '2': 'XX',
                     '3': 'XXX',
                     '4': 'XL',
                     '5': 'L',
                     '6': 'LX',
                     '7': 'LXX',
                     '8': 'LXXX',
                     '9': 'XC'}
        if self.tens:
            return self.tens_dict[tn]
        else:
            return ''
    
    def ones_p(self, oo):
        self.ones_dict = {'0': '',
                          '1': 'I',
                          '2': 'II',
                          '3': 'III',
                          '4': 'IV',
                          '5': 'V',
                          '6': 'VI',
                          '7': 'VII',
                          '8': 'VIII',
                          '9': 'IX'}
        if self.ones:
            return self.ones_dict[oo]
        else:
            return ''