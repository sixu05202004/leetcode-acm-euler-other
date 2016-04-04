#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = [0] * 1000001


def cal(n):
    t = sum([int(i) for i in str(n)])
    return t + n

for i in xrange(1, 1000001):
    s = cal(i)
    if s < 1000001:
        num[s] = 1

for i in xrange(1, 1000001):
    if num[i] != 1:
        print i
