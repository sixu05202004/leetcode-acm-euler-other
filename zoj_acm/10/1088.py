#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def check(n, m):
    s = 0
    for i in range(2, n):
        s = (s + m) % i
    if s == 0:
        return 1
    else:
        return 0


def zoj_1088():
    for line in sys.stdin:
        n = int(line.split()[0])
        if n:
            m = 2
            while 1:
                if check(n, m):
                    print m
                    break
                m += 1
if __name__ == '__main__':
    zoj_1088()
