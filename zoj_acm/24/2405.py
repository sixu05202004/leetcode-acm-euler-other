#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cal_12(n):
    result = []
    while n > 0:
        result.append(n % 12)
        n = n / 12
    return sum(result)


def cal_16(n):
    result = []
    while n > 0:
        result.append(n % 16)
        n = n / 16
    return sum(result)


def zoj_2405():
    for i in range(1000, 10000):
        t = [int(j) for j in str(i)]
        if sum(t) == cal_12(i) and sum(t) == cal_16(i):
            print i

if __name__ == '__main__':
    zoj_2405()
