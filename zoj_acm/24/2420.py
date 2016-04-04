#!/usr/bin/env python
# -*- coding: utf-8 -*-

DayOfWeek = {1: 'Sunday',
             2: 'Monday',
             3: 'Tuesday',
             4: "Wednesday",
             5: 'Thursday',
             6: 'Friday',
             0: 'Saturday'
             }


def proc(n):
    years = 2000
    days = 366
    month = 1
    days_month = 31
    while n > days:
        years += 1
        n = n - days
        if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
            days = 366
        else:
            days = 365
    if days == 366:
        flag = 1
    else:
        flag = 0
    while n > days_month:
        month += 1
        n = n - days_month
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days_month = 31
        elif month in [4, 6, 9, 11]:
            days_month = 30
        elif flag == 1:
            days_month = 29
        else:
            days_month = 28

    return years, month, n


def zoj_2420():
    while True:
        line = int(raw_input())
        if line == -1:
            break
        else:
            years, months, days = proc(line + 1)
            week = DayOfWeek.get(line % 7)
            print "%d-%02d-%02d %s" % (years, months, days, week)

if __name__ == '__main__':
    zoj_2420()
