#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cal(t, array):
    array.sort()
    if t == 'Faster':
        return array[0]
    if t == "Higher" or "Stronger":
        return array[-1]


def zoj_2970():
    n = int(raw_input())
    for i in range(n):
        t = raw_input()
        s = raw_input()
        line = raw_input().split()
        line = [int(i) for i in line]
        print cal(t, line)

if __name__ == '__main__':
    zoj_2970()
