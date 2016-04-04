#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(raw_input())
for i in xrange(n):
    line = int(raw_input())
    s = bin(line)[2:][::-1]
    t = [str(j) for j in xrange(len(s)) if s[j] == "1"]
    print " ".join(t)
