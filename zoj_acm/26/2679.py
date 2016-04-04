#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zoj_2679():
    n = int(raw_input())
    for i in range(n):
        result = 0
        flag = 0
        N = int(raw_input())
        line = raw_input().split()
        line = [int(a) for a in line]
        for t in range(9, 0, -1):
            for j in range(9, -1, -1):
                s = t * 10000 + \
                    line[0] * 1000 + line[1] * 100 + line[2] * 10 + j

                if not s % N:
                    flag = 1
                    result = "%d %d %d" % (
                        t, j, s / N)
                    break
            if flag:
                break
        print result


if __name__ == '__main__':
    zoj_2679()
