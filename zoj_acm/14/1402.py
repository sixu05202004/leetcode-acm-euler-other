#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    line = raw_input()
    if line == "0":
        break
    else:
        line = [int(i) for i in line.split()]
        flag = 0
        index = 0
        for i in range(1, line[0] + 1):
            sum1 = 0
            sum2 = 0
            for a in range(1, i + 1):
                sum1 += line[a]
            for b in range(line[0], i, -1):
                sum2 += line[b]
            if sum1 == sum2:
                flag = 1
                index = i
                break

        if flag:
            print "Sam stops at position %d and Ella stops at position %d." % (index, index + 1)
        else:
            print "No equal partitioning."