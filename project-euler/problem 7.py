#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import time
limit = 100000000
L = [True] * limit
#count = 0

start = time.time()


def seive(x):
    #global count
    for i in xrange(x * 2, limit, x):
        L[i] = False
        #count += 1

map(seive, [2])
map(seive, xrange(3, int(math.ceil(math.sqrt(limit))), 2))



primer = []
for i in xrange(2, limit):
    if L[i]:
        primer.append(i)
print primer[10000]
print time.time() - start
'''
print count
print time.time() - start
'''