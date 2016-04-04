#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2807():
    n = int(raw_input())
    for i in range(n):
        line = raw_input().split()
        line = [int(i) for i in line]
        print sum(line[1:]) - line[0] + 1

if __name__ == '__main__':
    zoj_2807()