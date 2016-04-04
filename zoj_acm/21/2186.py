#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2186():
    line = raw_input().split()
    line = [int(i) for i in line]
    result = 0
    for i in line:
        if i <= 168:
            result = i
            break
    if result:
        print "CRASH %d" % result
    else:
        print "NO CRASH"


if __name__ == '__main__':
    zoj_2186()