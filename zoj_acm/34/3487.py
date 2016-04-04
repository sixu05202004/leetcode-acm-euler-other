#!/usr/bin/env python
# -*- coding: utf-8 -*-

table = {'1': 'st',
         '2': 'nd',
         '3': 'rd'}
n = int(raw_input())
for i in xrange(n):
    line = raw_input()
    if len(line) == 1:
        if table.get(line):
            print line + table.get(line)
        else:
            print line + "th"
    else:
        if line[-2] == "1":
            print line + "th"
        else:
            if table.get(line[-1]):
                print line + table.get(line[-1])
            else:
                print line + "th"
