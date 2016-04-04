#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    line = raw_input()
    if line == '0.00':
        break
    else:
        total = 0
        s = 0
        while s < float(line):
            s = s + 1.0 / (total + 2)
            total += 1
        print "%d card(s)" % total
