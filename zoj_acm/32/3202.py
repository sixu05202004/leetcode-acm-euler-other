#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_3202():
    t = int(raw_input())
    for i in range(t):
        maxnum = 0
        second = 0
        j = 0
        n = int(raw_input())
        line = raw_input()
        line = line.split()
        line = [int(c) for c in line]
        for i in range(n):
            if line[i] > maxnum:
                second = maxnum
                maxnum = line[i]
                j = i + 1
            elif line[i] > second:
                second = line[i]
        print "%d %d" % (j, second)
if __name__ == '__main__':
    zoj_3202()
