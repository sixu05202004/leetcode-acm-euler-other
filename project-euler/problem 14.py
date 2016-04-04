#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

def collaz(n, result):
    result.append(n)
    if n > 1:
        if n % 2:
            collaz(3 * n + 1, result)
        else:
            collaz(n / 2, result)


def pep14(s):
    result = []
    maxnum = 0
    j = 1
    for i in range(1, s):
        collaz(i, result)
        if len(result) > maxnum:
            maxnum = len(result)
            j = i
        result = []

    return maxnum, j

if __name__ == '__main__':
    start = time.time()
    print pep14(1000000)
    print time.time() - start
