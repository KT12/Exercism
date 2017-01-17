#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 12:15:47 2017

@author: ktt
"""


from string import ascii_uppercase, digits
import random
from random import choice

class Robot(object):

    def __init__(self):
        random.seed()
        self.name = ''.join([choice(ascii_uppercase), choice(ascii_uppercase),
                            choice(digits),choice(digits),choice(digits)])
        
    def reset(self):
        random.seed()
        self.name = ''.join([choice(ascii_uppercase), choice(ascii_uppercase),
                            choice(digits),choice(digits),choice(digits)])