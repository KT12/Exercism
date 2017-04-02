#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:05:02 2017

@author: ktt
"""

# Got stuck on this one for a while

from itertools import cycle


def encode(msg, h):
    positions = pattern(h, len(msg))
    return ''.join(msg[i] for _, i in positions)


def decode(fence, h):
    positions = pattern(h, len(fence))
    rectified = sorted(enumerate(positions), key=lambda t: t[1][1])
    return ''.join(fence[i] for i, _ in rectified)


def pattern(h, w):
    n = 2 * (h - 1)
    positions = (min(x, n - x) for x in cycle(range(n)))
    return sorted(zip(positions, range(w)))
