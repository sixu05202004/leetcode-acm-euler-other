#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(raw_input())
for i in range(n):
    line = raw_input()
    line = [float(i) for i in line.split()]
    if line[0] * line[2] > 0 and line[0] == line[2]:
        print "circle"
    elif line[0] * line[2] > 0 and line[0] != line[2]:
        print "ellipse"
    elif line[0] * line[2] < 0:
        print "hyperbola"
    else:
        print "parabola"
