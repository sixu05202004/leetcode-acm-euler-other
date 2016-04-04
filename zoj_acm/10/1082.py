#!/usr/bin/env python
# -*- coding: utf-8 -*-


def floyd_path(result, n):
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                if result[i][k] + result[k][j] < result[i][j]:
                    result[i][j] = result[i][k] + result[k][j]
    return result


def zoj_1082():
    while True:
        n = int(raw_input())
        if n:
            result = [[float("infinity") for i in range(n + 1)] for j in range(n + 1)]
            for i in range(1, n + 1):
                result[i][i] = 0

            for c in range(1, n + 1):
                line = raw_input().split()
                line = [int(item) for item in line]
                if line[0]:
                    for z in range(line[0]):
                        result[c][line[1 + z * 2]] = line[2 + z * 2]
            floyd_path(result, n + 1)

            q = float("infinity")
            flag = 0
            for i in range(1, n + 1):
                num = 0
                for j in range(1, n + 1):
                    if result[i][j] > num:
                        num = result[i][j]
                if num < q:
                    q = num
                    flag = i
            if q == float("infinity"):
                print "disjoint"
            else:
                print "%d %d" % (flag, q)

        else:
            break

if __name__ == '__main__':
    zoj_1082()