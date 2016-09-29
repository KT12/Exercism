# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 02:26:47 2016

@author: Ken
"""
#==============================================================================
#
#   Calculate the date of meetups.
#   
#   Typically meetups happen on the same day of the week.
#
#   Examples are
#
#   the first Monday
#   the third Tuesday
#   the Wednesteenth Wednesday that falls on a -teen
#   
#   Input is year, month, day_of_week, timing
#   Output/return of function should be equal to date(YYYY,MM,DD).
#
#==============================================================================

# Can't quite get the exception to raise correctly.

from datetime import date

import calendar

def meetup_day(year, month, day_of_week, timing):
    m = calendar.monthcalendar(year, month)
    # m[week_idx] will get the week
    # calendar is formatted Monday - Sunday
    # (m[week_idx])[day_idx] will get a particular day
    day_dict = {'Monday' : 0,
                'Tuesday' : 1,
                'Wednesday': 2,
                'Thursday': 3,
                'Friday': 4,
                'Saturday': 5,
                'Sunday': 6}
    day_idx = day_dict[day_of_week.title()]
    timing_dict = {'1st' : 1,
                   'first' : 1,
                   '2nd' : 2,
                   'second': 2,
                   '3rd' : 3,
                   'third' : 3,
                   '4th': 4,
                   'fourth': 4,
                   '5th' : 5,
                   'fifth' : 5,
                   'last': 5,
                   'teenth' : 'teenth'}
    timing_idx = timing_dict[timing.lower()]
    if month == 2 and timing.lower() == 'fifth':
        raise Exception('MeetupDayException', meetup_day, year, month, day_of_week, timing)
    elif timing_idx == 'teenth':
        for teenth in range(13,20):
            if day_idx == calendar.weekday(year, month, teenth):
                return date(year, month, teenth)
    elif timing_idx == 5: # covers 5th and last cases
        if (m[-1])[day_idx]:
            return date(year, month, (m[-1])[day_idx]) # 5th+last day/last week
        else:
            return date(year, month, (m[-2])[day_idx]) # last day/penultimate week
    elif timing_idx == 1:
        if (m[0])[day_idx]:
            return date(year, month, (m[0])[day_idx]) # Maybe 1st day/1st week
        else:
            return date(year, month, (m[1])[day_idx]) # if not first week, 2nd
    else: # need to cover timing_idx 2,3,4
        if (m[0])[day_idx]: # Does month contain day of week in first week?
            return date(year, month, (m[(timing_idx - 1)])[day_idx])
        else:
            return date(year, month, (m[timing_idx])[day_idx])