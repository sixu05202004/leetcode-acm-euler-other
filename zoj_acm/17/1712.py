#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    line = raw_input()
    if line == '0':
        break
    else:
        line = [int(i) for i in line]
        line.reverse()
        total = 0
        for i in range(len(line)):
            if line[i]:
                total = total + (2 ** (i + 1) - 1) * line[i]
        print total
