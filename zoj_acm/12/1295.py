#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def zoj_1295():
    s = 1
    for line in sys.stdin:
        if s == 1:
            s += 1
            continue

    	print line[-2::-1]

if __name__ == '__main__':
    zoj_1295()
