#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    line = line.split()
    line = [int(i) for i in line]
    m = line[1]
    n = line[0]
    while(m % n):
        t = n
        n = m % n
        m = t
    if n == 1:
        print "%10d%10d    Good Choice\n" % (line[0], line[1])
    else:
        print "%10d%10d    Bad Choice\n" % (line[0], line[1])



