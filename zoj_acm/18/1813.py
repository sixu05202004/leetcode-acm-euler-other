#!/usr/bin/env python
# -*- coding: utf-8 -*-

p = 3.1415927
l = 5280 * 12
j = 1

while True:
    line = raw_input()
    line = [float(i) for i in line.split()]
    if line[1]:
        result = p * line[0] * line[1] / l
        print "Trip #%d: %.2f %.2f" % (j, result, (result / line[2])*60.0 * 60.0)
    else:
        break
    j+=1