#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    line = raw_input()
    if "0 0 0" == line:
        break
    else:
        line = [int(i) for i in line.split()]
        n = line[0]
        d = line[1]
        u = line[2]
        s = 0
        total = 0
        while True:
            s = s + d
            total += 1
            if s >= n:
                break
            s = s - u
            total += 1
        print total