#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 15:51:34 2017

@author: ktt
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 14:28:01 2017

@author: ktt
"""

def numeral(arabic):
        # Returns Roman equivalent of arabic numeral
        # Assumes input is int
        # Out of range num raise error
        
        if arabic > 3000 or arabic < 0:
            raise ValueError
        
        s_arabic = str(arabic)
        places = len(s_arabic)
        
        thous, hunds, tens, ones = None,None,None,None
        
        if places == 4:
            thous, hunds, tens, ones = str(arabic)
        elif places == 3:
            hunds, tens, ones = str(arabic)
        elif places == 2:
            tens, ones = str(arabic)
        elif places == 1:
            ones = str(arabic)
        
        return (thousands(thous) + hundreds(hunds) +
                tens_p(tens) + ones_p(ones))

def thousands(th):
        thous_dict = {'3': 'MMM',
                      '2': 'MM',
                      '1': 'M'}
        if th:
            return thous_dict[th]
        else:
            return ''
    
def hundreds(hh):
        
        hunds_dict = {'0': '',
                      '1': 'C',
                      '2': 'CC',
                      '3': 'CCC',
                      '4': 'CD',
                      '5': 'D',
                      '6': 'DC',
                      '7': 'DCC',
                      '8': 'DCCC',
                      '9': 'CM'}
        if hh:
            return hunds_dict[hh]
        else:
            return ''
    
def tens_p(tn):
        tens_dict = {'0': '',
                     '1': 'X',
                     '2': 'XX',
                     '3': 'XXX',
                     '4': 'XL',
                     '5': 'L',
                     '6': 'LX',
                     '7': 'LXX',
                     '8': 'LXXX',
                     '9': 'XC'}
        if tn:
            return tens_dict[tn]
        else:
            return ''
    
def ones_p(oo):
        ones_dict = {'0': '',
                          '1': 'I',
                          '2': 'II',
                          '3': 'III',
                          '4': 'IV',
                          '5': 'V',
                          '6': 'VI',
                          '7': 'VII',
                          '8': 'VIII',
                          '9': 'IX'}
        if oo:
            return ones_dict[oo]
        else:
            return ''