#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    result = list()
    flag = 1
    line = [float(i) for i in line.split()]
    for i in xrange(1, len(line) - 1):
        t = abs(line[i] - line[i + 1])
        result.append(t)

    for i in xrange(1, line[0] - 1):
        if i not in result:
            flag = 0
            break
    if flag:
        print "Jolly"
    else:
        print "Not jolly"

while True:
    line = raw_input()
    result = list()
    flag = 1
    line = [int(i) for i in line.split()]
    for i in range(1, len(line) - 1):
        t = abs(line[i] - line[i + 1])
        result.append(t)

    for i in xrange(1, line[0] - 1):
        if i not in result:
            flag = 0
            break
    if flag:
        print "Jolly"
    else:
        print "Not jolly"
