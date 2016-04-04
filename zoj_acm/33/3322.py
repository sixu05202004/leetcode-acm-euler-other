#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(raw_input())
for i in xrange(n):
    line = raw_input()
    line = [int(i) for i in line.split()]
    if line[0] > line[3]:
        print "cpcs"
    elif line[0] < line[3]:
        print "javaman"
    elif line[0] == line[3] and line[1] > line[4]:
        print "cpcs"
    elif line[0] == line[3] and line[1] < line[4]:
        print "javaman"
    elif line[0] == line[3] and line[1] == line[4] and line[2] > line[5]:
        print "cpcs"
    elif line[0] == line[3] and line[1] == line[4] and line[2] < line[5]:
        print "javaman"
    else:
        print "same"
