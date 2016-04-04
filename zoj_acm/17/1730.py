#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(raw_input())
for i in range(n):
    line = int(raw_input())
    k = line / 2
    j = line - k
    print k*(k-1)/2 + j*(j-1)/2