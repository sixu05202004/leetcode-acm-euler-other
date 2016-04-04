#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
result = [0] * 1000000
result[1] = 1


def collaz(n, j, i=1):
    if n > 1:
        #print n
        #result[n] += 1
        if n % 2:
            i += 1
            collaz(3 * n + 1, j, i)
        elif (n / 2) <= j and n <= j:
            result[j] = result[n / 2] + i
        else:
            i += 1
            collaz(n / 2, j, i)


def pep14():

    for i in range(2, 1000000):
        collaz(i, i)

    maxnum = 0
    j = 0
    for i in xrange(2, 1000000):
        if result[i] > maxnum:
            maxnum = result[i]
            j = i
    return maxnum, j


if __name__ == '__main__':
    start = time.time()
    print pep14()
    print time.time() - start
