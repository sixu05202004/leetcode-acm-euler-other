#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def rearrange(n):
    if n <= 2:
        return 1
    else:
        return (n - 2) * rearrange(n - 2) + (n - 1) * rearrange(n - 1)


def zoj_2625():
    for line in sys.stdin:
        str1 = line.split()
        result = rearrange(int(str1[0]))
        print result


def zoj_test():
    while True:
        line = raw_input()
        str1 = line.split()
        result = rearrange(int(str1[0]))
        print result

if __name__ == '__main__':
    zoj_test()
