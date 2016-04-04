#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    total = 0
    line = raw_input()
    if line == '-1':
        break
    else:
        line = [int(i) for i in line.split()]
        for i in line:
            if i != 0 and i * 2 in line:
                total += 1
        print total
