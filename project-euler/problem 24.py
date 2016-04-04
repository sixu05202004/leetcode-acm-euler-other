#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cycle_length(n):
 6     i = 1
 7     if n % 2 == 0: return cycle_length(n / 2)
 8     if n % 5 == 0: return cycle_length(n / 5)
 9     while True:
10         if (pow(10, i) - 1) % n == 0: return i
11         else: i = i + 1
12
13 m = 0
14 n = 0
15 for d in xrange(1,1000):
16     c = cycle_length(d)
17     if c > m:
18         m = c
19         n = d
20
21 print n