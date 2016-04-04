#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = int(raw_input())
for i in xrange(num):
    line = raw_input().split()
    line = sum([int(i[::-1]) for i in line])
    line = str(line)[::-1]
    print int(line)
