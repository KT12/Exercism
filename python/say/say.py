# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:10:24 2016

@author: Ken

Write a program that will take a number from 0 to 999,999,999,999 and 
spell out that number in English.
"""

# Input num should be int type

def say(num):
    dig = len(str(num))
    segs, lead = divmod(dig, 3)
    s = ''
    if num < 0 or  num > 999999999999:
        raise AttributeError
    elif num == 0:
        s = 'zero'
        return s
    
# Below function takes in 3 digit string number, returns the English equivalent
digits = {'9': 'nine',
          '8': 'eight',
          '7': 'seven',
          '6': 'six',
          '5': 'five',
          '4': 'four',
          '3': 'three',
          '2': 'two',
          '1': 'one',
          '0': ''}
          
def hundreds(s_num):
    if s_num == '000':
        return ''
    elif s_num[0] == 0:
        return tens(s_num)
    else:
        return digits[s_num[0]] + ' hundred and' + tens(s_num)

def tens(s_num):
    tens = {'9': 'ninety',
            '8': 'eighty',
            '7': 'seventy',
            '6': 'sixty',
            '5': 'fifty',
            '4': 'forty',
            '3': 'thirty',
            '2': 'twenty',
            '1': 'ten',
            '0': ''}
    teens = {'19': 'nineteen',
             '18': 'eighteen',
             '17': 'seventeen',
             '16': 'sixteen',
             '15': 'fifteen',
             '14': 'fourteen',
             '13': 'thirteen',
             '12': 'twelve',
             '11': 'eleven',
             '10': 'ten'}
    if s_num[1:] == '00':
        return ''
    elif s_num[1] == '1':
        return teens[s_num[1]]
    elif s_num[1] == '0':
        return digits[s_num[2]]
    else:
        return tens[s_num[1]] + '-' + digits[s_num[2]]